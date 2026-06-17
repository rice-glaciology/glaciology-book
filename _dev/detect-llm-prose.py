"""Heuristic detector for AI-flavored prose in the glaciology book.

Scans the prose paragraphs of every chapter listed in _toc.yml (markdown files
and the markdown cells of notebooks), skipping code, math, directives and
citations, and scores each paragraph against the specific "Claude/GPT tells"
recorded in the house style notes:

  - balanced aphoristic semicolon pairs ("The mass is nuclear; the behavior is
    electronic.")
  - colon-hinge sentences ("X does Y: the reason is Z")
  - corny / teaser paragraph openers ("worth a pause", "It is worth noting")
  - anthropomorphism of ice, molecules, the bed, "the system"
  - "which ... which ... which" relative-clause chains
  - tricolon / "not just X but Y" / "from X to Y" rhetorical flourishes
  - meta-discourse fillers ("Put concretely", "In other words", "Crucially")
  - em-dash pile-ups
  - overstatement ("the strongest available evidence", "at root", "no new physics")

The score only RANKS candidates. A human (or the model) must read each flagged
paragraph and decide; the regexes over-flag on purpose.

Run from repo root:  python _dev/detect-llm-prose.py [--top N] [--min-score S]
Writes _dev/llm-prose-report.md and prints a summary.
"""
import re, sys, json, glob, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---- gather the files actually in the book -------------------------------
def toc_files():
    toc = (ROOT / "_toc.yml").read_text()
    files = re.findall(r"file:\s*(\S+)", toc)
    out = []
    for f in files:
        for ext in (".md", ".ipynb"):
            p = ROOT / (f + ext)
            if p.exists():
                out.append(p); break
    return out

# ---- pull prose paragraphs out of a markdown string ----------------------
def paragraphs(md, source):
    """Yield (start_line, text) prose paragraphs, skipping code/math/directives."""
    lines = md.split("\n")
    fence = False           # ``` code / directive fence
    mathblock = False       # $$ ... $$
    buf, start = [], 0
    def flush(out):
        nonlocal buf, start
        if buf:
            text = " ".join(buf).strip()
            if text:
                out.append((start + 1, text))
        buf = []
    out = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("```"):
            flush(out); fence = not fence; continue
        if fence:
            continue
        if s == "$$":
            flush(out); mathblock = not mathblock; continue
        if mathblock:
            continue
        # skip standalone block math, directive option lines, headings, html,
        # comments, table rows, image/figure refs, bib, list bullets
        if (not s
                or s.startswith("#") or s.startswith(":") or s.startswith("%")
                or s.startswith("<") or s.startswith("|") or s.startswith(">")
                or s.startswith("$$") or re.match(r"^\s*[-*]\s", ln)
                or re.match(r"^\s*\d+\.\s", ln)
                or s.startswith("{") or s.startswith("(")):
            flush(out); continue
        if not buf:
            start = i
        buf.append(s)
    flush(out)
    return out

def md_from_ipynb(path):
    nb = json.loads(path.read_text())
    cells = []
    for c in nb.get("cells", []):
        if c.get("cell_type") == "markdown":
            cells.append("".join(c.get("source", [])))
    return "\n\n".join(cells)

# ---- scrub inline math / cites / roles so they don't pollute the text -----
def scrub(t):
    t = re.sub(r"\$[^$]*\$", " MATH ", t)
    t = re.sub(r"\{[a-z]+\}`[^`]*`", " REF ", t)   # {cite}`x`, {doc}`y`, {numref}
    t = re.sub(r"`[^`]*`", " CODE ", t)
    return t

# ---- the heuristics ------------------------------------------------------
ANTHRO = (r"\b(wants?|wishes?|seeks?|tries|trying|prefers?|likes?|eager|reluctant|"
          r"refuses?|chooses?|choose|decides?|decide|conspires?|conspire|punish(?:es|ed)?|"
          r"remembers?|knows?|feels?|aware|happy|content|restless|comfortable|lazy|"
          r"struggles?|struggle|suffers?|desires?|wandering|hungry)\b")
ANTHRO_SUBJ = (r"\b(ice|water|molecule|molecules|atom|atoms|electron|electrons|proton|"
               r"protons|crystal|crystals|bond|bonds|defect|defects|glacier|glaciers|"
               r"the bed|the system|the terminus|the front|the ice|the flow|the lattice|"
               r"nature)\b")

META = (r"\b(Put concretely|Put simply|Put another way|In other words|That is to say|"
        r"To put it|Simply put|In essence|In short|Crucially|Importantly|Notably|"
        r"Tellingly|Strikingly|Remarkably|Interestingly|It is worth|worth noting|"
        r"worth remembering|worth a pause|worth watching|worth stepping back|"
        r"It turns out)\b")

OVERSTATE = (r"(strongest available evidence|\bat root\b|\bat heart\b|no new physics|"
             r"without any new|nothing more than|nothing but|the key insight|"
             r"the crucial point|the whole point|the deep(?:er)? (?:reason|point)|"
             r"profound|the remarkable thing|the beauty of|elegantl?y?|the real reason)")

OPENER_CUE = (r"^(One |The simplest|The remarkable|There is a |There is something|"
              r"What is (?:striking|remarkable)|It is worth|It is tempting|"
              r"Remarkably|Strikingly|Crucially|Notice that|Note that|Consider )")

def score_paragraph(text):
    t = scrub(text)
    hits = []
    # split into sentences (rough)
    sents = re.split(r"(?<=[.!?])\s+", t)

    # 1. balanced aphoristic semicolon pair: short parallel halves
    for s in sents:
        if ";" in s:
            a, _, b = s.partition(";")
            aw, bw = len(a.split()), len(b.split())
            if 2 <= aw <= 10 and 2 <= bw <= 11:
                # parallel-ish: both halves start with article/"the"
                if re.match(r"\s*(The|A|An|Its|This|That)\b", a) and \
                   re.match(r"\s*(the|a|an|its|this|that)\b", b.strip(), re.I):
                    hits.append(("aphoristic-semicolon", 3, s.strip()[:90]))

    # 2. colon-hinge sentence (not a list / not before MATH)
    for s in sents:
        m = re.search(r"[a-z]{4,}:\s+[a-z]", s)
        if m and "MATH" not in s[m.start():m.start()+12] and "e.g." not in s and \
           "i.e." not in s and not re.search(r"(following|these|below|two|three|"
           r"are|namely|such as)\b[^:]{0,30}:", s):
            hits.append(("colon-hinge", 2, s.strip()[:90]))

    # 3. corny / teaser opener
    first = sents[0] if sents else ""
    if re.search(OPENER_CUE, first):
        hits.append(("teaser-opener", 2, first.strip()[:90]))
    # stark mini-sentence opener restated by next sentence
    if len(sents) > 1 and 2 <= len(first.split()) <= 6 and first.endswith("."):
        hits.append(("stark-mini-opener", 2, first.strip()[:90]))

    # 4. anthropomorphism (subject near a volitional verb)
    for s in sents:
        if re.search(ANTHRO, s, re.I) and re.search(ANTHRO_SUBJ, s, re.I):
            hits.append(("anthropomorphism", 3, s.strip()[:90]))

    # 5. relative-clause "which ... which ... which" chain
    for s in sents:
        if len(re.findall(r"\bwhich\b", s)) >= 2:
            hits.append(("which-chain", 2, s.strip()[:90]))
    if len(re.findall(r",\s+which\b", t)) >= 3:
        hits.append(("which-chain-para", 2, ""))

    # 6. rhetorical flourishes
    for pat, name in [(r"\bnot just\b[^.]{1,40}\bbut\b", "not-just-but"),
                      (r"\bnot only\b[^.]{1,40}\bbut\b", "not-only-but"),
                      (r"\bis not\b[^.]{1,30}\bbut\b", "is-not-but"),
                      (r"\bfrom\b \w+ \bto\b \w+,", "from-x-to-y"),
                      (r"\bneither\b[^.]{1,30}\bnor\b", "neither-nor")]:
        if re.search(pat, t):
            hits.append((name, 1, ""))

    # 7. meta-discourse filler
    for m in re.finditer(META, t):
        hits.append(("meta-filler", 2, m.group(0)))

    # 8. em-dash pile-up
    nd = t.count("—") + t.count(" -- ")
    if nd >= 3:
        hits.append(("em-dash-pileup", 1, f"{nd} dashes"))

    # 9. overstatement
    for m in re.finditer(OVERSTATE, t, re.I):
        hits.append(("overstatement", 2, m.group(0)))

    # 10. "feedback closes on itself" type imagery
    if re.search(r"(closes on itself|feeds on itself|on its own|takes on a life|"
                 r"runs away with)", t, re.I):
        hits.append(("self-reference-imagery", 2, ""))

    score = sum(w for _, w, _ in hits)
    # density bonus: many distinct tell-types in one paragraph is the real signal
    kinds = len(set(h[0] for h in hits))
    if kinds >= 3:
        score += kinds
    return score, hits

def evaluate_file(path, strict=True):
    """Strict gate for a single draft file (markdown or .ipynb).

    Returns (passed, flagged) where flagged is a list of
    (score, line, paragraph, hits). In strict mode every paragraph with any
    tell at all is reported, and the file PASSES only if nothing is flagged.
    Used by the scheduled enrichment task to gate its own drafts before they
    reach the manuscript.
    """
    p = Path(path)
    md = md_from_ipynb(p) if p.suffix == ".ipynb" else p.read_text()
    threshold = 1 if strict else 3
    flagged = []
    for line, text in paragraphs(md, p):
        if len(text.split()) < 8:
            continue
        sc, hits = score_paragraph(text)
        if sc >= threshold:
            flagged.append((sc, line, text, hits))
    flagged.sort(key=lambda r: -r[0])
    passed = len(flagged) == 0
    print(f"{'PASS' if passed else 'FAIL'}  {path}  "
          f"({len(flagged)} paragraph(s) flagged, strict={strict})")
    for sc, line, text, hits in flagged:
        kinds = ", ".join(sorted(set(h[0] for h in hits)))
        ex = "; ".join(h[2] for h in hits if h[2])
        print(f"  [{sc}] line {line}: {kinds}")
        if ex: print(f"        e.g. {ex[:160]}")
    return passed, flagged

def main():
    # strict single-draft gate:  detect-llm-prose.py --file path/to/draft.md
    if "--file" in sys.argv:
        f = sys.argv[sys.argv.index("--file")+1]
        strict = "--lenient" not in sys.argv
        passed, _ = evaluate_file(f, strict=strict)
        sys.exit(0 if passed else 1)

    top = 60
    minscore = 4
    if "--top" in sys.argv: top = int(sys.argv[sys.argv.index("--top")+1])
    if "--min-score" in sys.argv: minscore = int(sys.argv[sys.argv.index("--min-score")+1])

    rows = []
    for path in toc_files():
        md = md_from_ipynb(path) if path.suffix == ".ipynb" else path.read_text()
        rel = path.relative_to(ROOT)
        for line, text in paragraphs(md, rel):
            if len(text.split()) < 12:   # ignore stubs / one-liners
                continue
            sc, hits = score_paragraph(text)
            if sc >= minscore:
                rows.append((sc, str(rel), line, text, hits))
    rows.sort(key=lambda r: -r[0])

    out = ["# AI-flavored prose report",
           f"\n{len(rows)} paragraphs scored ≥ {minscore}, ranked by score. "
           "Heuristic only — read each before editing.\n"]
    for sc, rel, line, text, hits in rows[:top]:
        kinds = ", ".join(sorted(set(h[0] for h in hits)))
        out.append(f"\n## [{sc}] {rel}:{line}\n")
        out.append(f"*tells:* {kinds}\n")
        ex = [f"`{h[0]}` → {h[2]}" for h in hits if h[2]]
        if ex:
            out.append("\n".join(f"- {e}" for e in ex[:6]) + "\n")
        snippet = text[:600] + ("…" if len(text) > 600 else "")
        out.append(f"\n> {snippet}\n")
    (ROOT / "_dev/llm-prose-report.md").write_text("\n".join(out))

    # console summary
    print(f"scanned {len(toc_files())} files; flagged {len(rows)} paragraphs "
          f"(score >= {minscore})")
    print(f"top {min(top,len(rows))} written to _dev/llm-prose-report.md\n")
    from collections import Counter
    byfile = Counter(r[1] for r in rows)
    for f, n in byfile.most_common(15):
        print(f"  {n:3d}  {f}")

if __name__ == "__main__":
    main()
