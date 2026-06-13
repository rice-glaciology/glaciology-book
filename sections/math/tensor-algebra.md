# Vectors, matrices, and tensors

The chapters on ice deformation and flow are written in the language of tensors, because stress, strain rate, and the flow law that links them are quantities that a single number cannot capture. This chapter collects the algebra those chapters use, in one place and from the ground up. It assumes only that the reader has met vectors and matrices, and it builds from them to the operations that recur throughout the book: the symmetric and antisymmetric split that separates straining from rotation, the deviatoric split that separates shape change from pressure, the eigenvalues that give principal stresses and fabric strengths, and the invariants that any physical law must be built from. A reader fluent in continuum mechanics can skip it; everyone else can return to it as a reference. A fuller account is in the appendices of {cite}`greve2009`.

## Scalars, vectors, and tensors

A scalar is a single number that does not depend on the orientation of the coordinate axes: temperature, density, and pressure are scalars. A vector is a quantity with both magnitude and direction, represented in a chosen set of axes by three components, like a velocity $\mathbf{u}$ with components $(u_1,u_2,u_3)$. A second-order tensor is the next step in the sequence. It is the object needed to describe a quantity that relates one vector to another in a way that depends on direction, and it is represented by a three-by-three matrix of nine components $\sigma_{ij}$. The stress tensor is the central example: it takes the orientation of a surface and returns the force per unit area acting on that surface, a vector-to-vector relation that no scalar or single vector could express.

What distinguishes a tensor from an arbitrary matrix of numbers is how its components change when the coordinate axes are rotated. The components themselves are not the physical object; they are its description in one frame, and a different frame gives different numbers for the same tensor. A constitutive law must give the same physical prediction in every frame, and this requirement, developed below as a dependence on invariants, is what makes tensor algebra the right language for mechanics.

## Index notation and the summation convention

Writing tensor equations out component by component is unwieldy, so the book uses index notation. A vector is written $u_i$, meaning the component with $i$ standing for any of $1,2,3$, and a second-order tensor is written $\sigma_{ij}$ with two free indices. The summation convention, due to Einstein, states that whenever an index appears twice in a single term it is summed over its three values, and the summation sign is omitted. Thus

$$
a_i b_i \equiv \sum_{i=1}^{3} a_i b_i = a_1 b_1 + a_2 b_2 + a_3 b_3
$$

is the dot product of two vectors, a scalar, because the repeated index $i$ is summed away and no free index remains. An index that is summed is called a dummy index and can be renamed freely; an index that is not is a free index and must match on both sides of an equation. Two symbols complete the notation. The Kronecker delta $\delta_{ij}$ equals one when $i=j$ and zero otherwise, and is the index form of the identity matrix, so that $\delta_{ij}a_j=a_i$. The matrix-vector product and the matrix-matrix product are then

$$
(\boldsymbol{\sigma}\mathbf{n})_i = \sigma_{ij} n_j,
\qquad
(\mathbf{A}\mathbf{B})_{ik} = A_{ij}B_{jk},
$$

each with the inner index repeated and summed. This compact notation is what lets Cauchy's relation between traction and stress, $t_i=\sigma_{ij}n_j$, be written on one line in {doc}`../ice_flow/stress-and-strain`.

## Symmetry and the splitting of a tensor

The transpose of a tensor exchanges its indices, $(\sigma^{\mathsf T})_{ij}=\sigma_{ji}$, reflecting the matrix across its diagonal. A tensor is symmetric if it equals its transpose, $\sigma_{ij}=\sigma_{ji}$, and antisymmetric if it equals minus its transpose, $\sigma_{ij}=-\sigma_{ji}$, which forces the diagonal of an antisymmetric tensor to vanish. Any tensor can be split uniquely into a symmetric and an antisymmetric part,

$$
A_{ij} = \underbrace{\tfrac12\left(A_{ij}+A_{ji}\right)}_{\text{symmetric}} + \underbrace{\tfrac12\left(A_{ij}-A_{ji}\right)}_{\text{antisymmetric}} ,
$$

```{admonition} Derivation
:class: dropdown
Write the proposed parts as $S_{ij}=\tfrac12(A_{ij}+A_{ji})$ and $W_{ij}=\tfrac12(A_{ij}-A_{ji})$. Their sum is

$$
S_{ij}+W_{ij}=\tfrac12(A_{ij}+A_{ji})+\tfrac12(A_{ij}-A_{ji})=\tfrac12\,(2A_{ij})=A_{ij},
$$

so the decomposition reproduces $A_{ij}$. The first part is symmetric, since exchanging the indices gives $S_{ji}=\tfrac12(A_{ji}+A_{ij})=S_{ij}$, and the second is antisymmetric, since $W_{ji}=\tfrac12(A_{ji}-A_{ij})=-W_{ij}$.

Uniqueness follows from the splitting being forced. Suppose $A_{ij}=S'_{ij}+W'_{ij}$ for any symmetric $S'$ and antisymmetric $W'$. Transposing gives $A_{ji}=S'_{ij}-W'_{ij}$. Adding the two equations yields $S'_{ij}=\tfrac12(A_{ij}+A_{ji})=S_{ij}$, and subtracting yields $W'_{ij}=\tfrac12(A_{ij}-A_{ji})=W_{ij}$. The two parts are therefore the only ones that work.
```

and this innocuous-looking identity carries real physics. Applied to the velocity gradient $\partial u_i/\partial x_j$, the symmetric part is the strain-rate tensor, which measures the rate of stretching and shearing, and the antisymmetric part is the spin tensor, which measures the rate of rigid rotation. Only the symmetric part deforms the material, so only it enters the flow law, a separation made physical in {doc}`../ice_flow/stress-and-strain`. The stress tensor, by contrast, is symmetric from the outset, a consequence of the balance of angular momentum, so it has only six independent components rather than nine.

## Trace and the deviatoric split

The trace of a tensor is the sum of its diagonal components, $\mathrm{tr}(\boldsymbol{\sigma})=\sigma_{ii}=\sigma_{11}+\sigma_{22}+\sigma_{33}$, a scalar because the repeated index is summed. The trace is unchanged by rotation of the axes, so it is the first of the invariants below. A second universal split uses it. Any tensor can be written as the sum of an isotropic part proportional to the identity and a trace-free remainder,

$$
\sigma_{ij} = \underbrace{\tfrac13\,\sigma_{kk}\,\delta_{ij}}_{\text{isotropic}} + \underbrace{\left(\sigma_{ij}-\tfrac13\,\sigma_{kk}\,\delta_{ij}\right)}_{\text{deviatoric}} .
$$

```{admonition} Derivation
:class: dropdown
The identity is established by adding and subtracting the same term, $\sigma_{ij}=\tfrac13\sigma_{kk}\delta_{ij}+(\sigma_{ij}-\tfrac13\sigma_{kk}\delta_{ij})$, so it holds for any tensor. What gives it content is that the remainder is trace free. Take the trace of the deviatoric part by setting $j=i$ and summing,

$$
\sigma_{ii}-\tfrac13\,\sigma_{kk}\,\delta_{ii}=\sigma_{ii}-\tfrac13\,\sigma_{kk}\,(3)=\sigma_{ii}-\sigma_{kk}=0,
$$

where $\delta_{ii}=3$ because the index runs over the three diagonal entries and $\sigma_{ii}$ and $\sigma_{kk}$ are the same scalar under different dummy labels. The first part carries the entire trace, $\mathrm{tr}(\tfrac13\sigma_{kk}\delta_{ij})=\tfrac13\sigma_{kk}\delta_{ii}=\sigma_{kk}$, and the second carries none.
```

For the stress tensor the isotropic part is the pressure, $p=-\tfrac13\sigma_{kk}$, and the trace-free remainder is the deviatoric stress $\tau_{ij}$. The physical point, central to {doc}`../ice_flow/stress-and-strain` and {doc}`../ice_flow/ice-rheology`, is that ice is very nearly incompressible, so the pressure cannot change its shape and does no work in deformation. It is the deviatoric stress alone that drives flow, which is why the flow law relates strain rate to $\tau_{ij}$ and not to the full stress.

## Eigenvalues, eigenvectors, and principal values

For a given tensor there are special directions along which it acts simply, stretching a vector without rotating it. A vector $\mathbf{v}$ is an eigenvector of $\boldsymbol{\sigma}$ with eigenvalue $\lambda$ if

$$
\sigma_{ij}v_j = \lambda\,v_i ,
$$

so that applying the tensor to $\mathbf{v}$ merely scales it by $\lambda$. The eigenvalues are the roots of the characteristic equation $\det(\sigma_{ij}-\lambda\delta_{ij})=0$, a cubic in $\lambda$. A symmetric tensor, which is the only kind that appears in this book, has three real eigenvalues and three mutually perpendicular eigenvectors. For the stress tensor these are the principal stresses and the principal directions: in the frame aligned with the eigenvectors the stress is purely normal, with no shear, and the principal stresses are the normal stresses on those faces. The same idea names the strengths of a crystal fabric. The structure tensor of {doc}`../ice_flow/ice-fabric` is a symmetric tensor whose eigenvalues, summing to one, measure how strongly the crystal axes cluster along each of its three principal directions, so a single-maximum fabric has one eigenvalue near one and an isotropic fabric has all three equal to a third.

## Invariants

Because the components of a tensor depend on the frame, a physical law cannot be built directly from them; it must be built from combinations that do not change under rotation, the invariants. A symmetric tensor has three independent invariants, which can be taken as the coefficients of its characteristic equation or, equivalently, as the trace, the sum of products of pairs of eigenvalues, and the determinant. For a trace-free tensor such as the deviatoric stress the first invariant vanishes, and the most important remaining one is the second invariant, which for the deviatoric stress and the strain rate defines the effective, or equivalent, scalar measures

$$
\tau_E = \sqrt{\tfrac12\,\tau_{ij}\tau_{ij}},
\qquad
\dot\varepsilon_E = \sqrt{\tfrac12\,\dot\varepsilon_{ij}\dot\varepsilon_{ij}} .
$$

These single numbers summarize the overall magnitude of shape-changing stress and of deformation, independent of orientation, and they are exactly the quantities that appear in Glen's flow law in {doc}`../ice_flow/ice-rheology`. A constitutive law written in terms of invariants is guaranteed to respect the requirement that physics not depend on the observer's choice of axes.

## The tensor product and the structure tensor

One construction builds a tensor from two vectors rather than splitting one apart. The tensor product, or outer product, of two vectors is the second-order tensor with components

$$
(\mathbf{a}\otimes\mathbf{b})_{ij} = a_i b_j .
$$

Unlike the dot product, which contracts two vectors to a scalar, the outer product spreads them into a matrix. The outer product of a unit vector with itself, $\mathbf{c}\otimes\mathbf{c}$, projects onto the direction of $\mathbf{c}$, and averaging this projection over a population of crystal orientations gives the second-order structure tensor of {doc}`../ice_flow/ice-fabric`, the compact summary of a fabric. Higher averages, such as $\mathbf{c}\otimes\mathbf{c}\otimes\mathbf{c}\otimes\mathbf{c}$, give the fourth-order tensors that the anisotropic flow law needs.

## Tensor fields and their derivatives

In a glacier the stress, strain rate, and velocity are not single tensors but fields, varying from point to point, and the balance laws involve their spatial derivatives. Two operations recur. The gradient of a scalar field $\phi$ is the vector $\partial\phi/\partial x_i$ pointing in the direction of steepest increase, which appears as the surface-slope term driving the flow. The divergence of a tensor field is the vector $\partial\sigma_{ij}/\partial x_j$, formed by differentiating and summing on the second index, and it measures the net surface force per unit volume exerted on a parcel of ice by its neighbours. The momentum balance of {doc}`../ice_flow/stress-balance` is the statement that this divergence balances gravity, $\partial\sigma_{ij}/\partial x_j+\rho g_i=0$. The divergence theorem, which converts an integral of a divergence over a volume into an integral over its bounding surface, is the tool that turns the force balance on a parcel into the local differential equation, and it is used in that chapter to derive Cauchy's equation of motion. With these operations in hand the deformation chapters can be read in their own notation.
