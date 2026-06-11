# Analytical ice-sheet solutions

The shallow-ice approximation of {doc}`shallow-ice` reduced the flow of an ice sheet to a single equation for its thickness. In a handful of idealized cases that equation can be solved in closed form, and the solutions are worth the effort for three reasons: they give an independent check on numerical models, they are cheap to evaluate, and they show directly how the shape of an ice sheet depends on its rheology, its size, and its mass balance. This chapter derives three of them, the viscous Vialov profile, the perfect-plastic profile, and the modification by glacial isostasy, following the analytical lectures of {cite}`hewitt_karthaus` together with {cite}`nye1952,vialov1958`.

## The steady viscous profile

Consider an ice sheet on a flat bed, with no sliding, spreading symmetrically from a central divide at $x=0$ to a margin at $x=L$, fed by a uniform balance rate $\dot b$. In steady state the thickness does not change, so the depth-integrated mass balance of {doc}`shallow-ice` reduces to a statement that the ice flux grows linearly away from the divide,

$$
\frac{\partial}{\partial x}\!\left(\bar u H\right)=\dot b
\quad\Longrightarrow\quad
\bar u H = \dot b\,x .
$$

With the bed flat the surface equals the thickness, $s=H$, and the shallow-ice expression for the depth-averaged velocity gives the flux

$$
\bar u H = \frac{2A(\rho_i g)^n}{n+2}\,H^{\,n+2}\left(-\frac{\partial H}{\partial x}\right)^{n},
$$

where the slope is negative on the flank so the bracket is positive. Setting the two expressions for the flux equal,

$$
H^{\,n+2}\left(-\frac{\partial H}{\partial x}\right)^{n}=\frac{(n+2)\,\dot b}{2A(\rho_i g)^n}\,x .
$$

Taking the $n$th root and recognizing the left side as a derivative,

$$
H^{(n+2)/n}\left(-\frac{\partial H}{\partial x}\right)
=-\frac{n}{2(n+1)}\frac{\mathrm{d}}{\mathrm{d}x}\,H^{\,2(n+1)/n}
=\left[\frac{(n+2)\dot b}{2A(\rho_i g)^n}\right]^{1/n}x^{1/n},
$$

and integrating inward from the margin, where $H(L)=0$, gives the Vialov profile,

$$
H(x)=\left[\frac{2(n+2)^{1/n}}{(2A)^{1/n}\rho_i g}\right]^{\!\frac{n}{2(n+1)}}\dot b^{\,\frac{1}{2(n+1)}}\,L^{1/2}
\left[1-\left(\frac{x}{L}\right)^{\!\frac{n+1}{n}}\right]^{\!\frac{n}{2(n+1)}},
\qquad 0<x<L .
$$

The shape is the smooth dome familiar from any cross-section of Greenland or East Antarctica, steep at the margin and nearly flat at the divide. The result it teaches is in the exponents. The central thickness scales as $L^{1/2}$, so a wider ice sheet is thicker in proportion to the square root of its span, and only as $\dot b^{\,1/2(n+1)}$, a very weak dependence on the balance rate. Doubling the snowfall thickens the ice sheet by only a few percent. An ice sheet's height is set by how far it spreads, not by how much it snows.

## The perfect-plastic profile

A complementary idealization treats ice not as a viscous fluid but as a perfectly plastic solid, the limit $n\to\infty$ of Glen's law in which the ice deforms freely once the stress reaches a yield value $\tau_i$ and not at all below it. This is the oldest analytical model {cite}`nye1952`. If the bed everywhere supports exactly the yield stress, then the shallow-ice driving stress equals $\tau_i$,

$$
-\rho_i g\,H\,\frac{\partial s}{\partial x}=\tau_i .
$$

With a flat bed, $s=H$, and the product $H\,\partial H/\partial x$ is half the derivative of $H^2$, so the equation becomes

$$
\frac{\partial}{\partial x}\!\left(H^{2}\right)=-\frac{2\tau_i}{\rho_i g}
\quad\Longrightarrow\quad
\left|\nabla\!\left(H^{2}\right)\right|=\frac{2\tau_i}{\rho_i g}.
$$

The square of the thickness falls off linearly, so integrating inward from the margin gives

$$
H(x)=H_0^{1/2}\,(L-x)^{1/2},
\qquad
H_0=\frac{2\tau_i}{\rho_i g}\approx 20\ \mathrm{m}.
$$

This is the parabolic, or more precisely the elliptical, profile that lies behind the rule of thumb that an ice sheet a thousand kilometres in span stands a few thousand metres high. Because $H^2$ has a constant gradient, the shape is exactly that of a heap of dry sand or sugar poured onto a table, which is why a pile of sugar in the outline of Antarctica reproduces the real surface so well. The profile depends only on the yield stress and the span, not at all on the accumulation, which makes it a useful first estimate of the thickness of a former ice sheet whose extent is known from its moraines but whose climate is not. The price of the simplicity is the unphysical cusp at the divide, where the slope is infinite; the viscous profile rounds it off.

## Glacial isostasy

Both profiles assumed a rigid bed, but the weight of an ice sheet depresses the crust into the mantle beneath. The simplest account treats the crust as floating in local isostatic balance, so that the bed sinks in proportion to the ice load,

$$
b=b_0-\frac{\rho_i}{\rho_m}\,H,
$$

with $\rho_m$ the mantle density. The surface elevation that drives the flow is then a reduced fraction of the thickness,

$$
s=b+H=b_0+r_m H,
\qquad
r_m=1-\frac{\rho_i}{\rho_m}\approx 0.7 .
$$

Only about seventy percent of any added thickness raises the surface; the rest is taken up by depressing the bed. Repeating the perfect-plastic derivation with this softened surface slope, $-\rho_i g\,H\,\partial s/\partial x=\tau_i$ with $s=r_m H$, gives a thicker ice sheet for the same span,

$$
H(x)=r_m^{-1/2}H_0^{1/2}(L-x)^{1/2},
\qquad
s(x)=r_m^{1/2}H_0^{1/2}(L-x)^{1/2}.
$$

The factor $r_m^{-1/2}\approx 1.2$ on the thickness is the signature of isostasy: an ice sheet sitting in the bowl it has pressed into the crust holds appreciably more ice than the same ice sheet on a rigid bed, because it must grow thicker to raise its surface to the slope that balances the driving stress. This matters for reconstructing the volume, and hence the sea-level contribution, of the great ice sheets of the past, and the slow rebound of the crust after they melted is still measured today. The viscous response of the mantle, which makes that rebound lag the unloading by thousands of years, is a refinement on the instantaneous balance assumed here, and it returns with the prognostic modelling.
