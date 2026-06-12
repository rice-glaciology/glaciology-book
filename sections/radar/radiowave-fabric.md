# Radio-wave propagation in anisotropic ice

The previous chapters described fabric as a product of deformation and as a control on flow. Fabric also has an electromagnetic signature, and that signature is what lets radar measure fabric over large areas where no ice core exists. The reason is that radio waves travel through ice at a speed that depends on their polarization relative to the fabric, a property called birefringence. This chapter develops that link, building on the dielectric properties of ice set out in {doc}`em-waves` and following the wave-propagation notes of {cite}`rathmann_notes`, and it is the basis of modern polarimetric radar surveys of fabric.

## Ice as an anisotropic dielectric

Radio waves are governed by Maxwell's equations. In ice, with no free charge or current, they combine into a wave equation for the electric field,

$$
\nabla\times\nabla\times\mathbf{E} = -\frac{1}{c^2}\,\mu_r\,\boldsymbol{\epsilon}_r\cdot\frac{\partial^2 \mathbf{E}}{\partial t^2},
$$

where the relative permittivity $\boldsymbol{\epsilon}_r$ is a tensor because ice is electrically anisotropic. A single ice crystal is uniaxial: its permittivity takes one value, $\epsilon_a$, for fields perpendicular to the c-axis and a different value, $\epsilon_c$, for fields parallel to it. The difference $\Delta\epsilon = \epsilon_c - \epsilon_a$ is small, a few percent of the mean, but it is the quantity that makes the measurement possible.

## The bulk permittivity carries the fabric

When the radar wavelength is much longer than the grain size, the wave responds to the average permittivity of many grains. Averaging the single-crystal permittivity over the distribution of c-axis orientations gives the bulk permittivity of the polycrystal,

$$
\boldsymbol{\epsilon} = \bar\epsilon\,\mathbf{I} + \Delta\epsilon\left(\langle\mathbf{c}^2\rangle - \tfrac{1}{3}\mathbf{I}\right),
$$

where $\langle\mathbf{c}^2\rangle$ is the second-order structure tensor, the orientation average of the outer product of the c-axis with itself. This tensor is the compact description of the fabric. Its three eigenvalues $\lambda_x,\lambda_y,\lambda_z$ sum to one and measure how strongly the c-axes cluster toward each principal axis. For perfectly isotropic ice $\langle\mathbf{c}^2\rangle = \tfrac{1}{3}\mathbf{I}$, the anisotropic term vanishes, and the bulk permittivity is the scalar $\bar\epsilon\,\mathbf{I}$. Any departure from isotropy shows up directly as anisotropy in $\boldsymbol{\epsilon}$.

## Fast and slow waves

Looking for plane-wave solutions turns the wave equation into an eigenvalue problem whose eigenvalues are the permitted wave speeds and whose eigenvectors are the permitted polarizations. For a radar looking straight down, the two relevant solutions are waves polarized horizontally along the two fabric principal axes, with eigenvelocities

$$
V_i = \frac{1}{\sqrt{\mu\,(\epsilon_a + \lambda_i\,\Delta\epsilon)}}, \qquad i = x,y.
$$

A wave polarized along the axis where the c-axes cluster more strongly, the larger $\lambda_i$, travels more slowly. The two horizontal polarizations therefore propagate as a fast wave and a slow wave. This is the birefringence: a single radar pulse splits, in effect, into two polarizations that drift apart in time as they go deeper.

## From travel-time difference to fabric

It is convenient to work with the slowness $S = 1/V$, since travel time is slowness integrated along the path. The two-way travel-time difference between the two horizontally polarized waves, from the surface at $H$ down to depth $z$ and back, is the integral of the difference in their slownesses. Expanding about an isotropic reference state, this reduces to a simple and useful result,

$$
\Delta t(z) \approx \frac{\Delta S^2}{S_{\text{iso}}}\int_H^{z}\left(\lambda_x(z') - \lambda_y(z')\right)\,\mathrm{d}z',
$$

where $S_{\text{iso}}$ is the slowness of isotropic ice and $\Delta S^2 = \mu\,\Delta\epsilon$ measures the single-crystal anisotropy. The travel-time difference between orthogonally polarized radio waves is, to first order, proportional to the depth-integrated difference between the two horizontal fabric eigenvalues.

By measuring how the travel-time difference between orthogonal polarizations grows with depth and differentiating with respect to depth, one recovers the horizontal fabric anisotropy $\lambda_x - \lambda_y$ as a function of depth. Phase-sensitive systems such as ApRES measure this difference through the phase of the returns, and multi-element and polarimetric radars measure it across the full polarization plane. The fabric recovered this way can then be compared with the fabric that deformation models such as specfab predict, and fed back into the anisotropic flow law of {doc}`../ice_flow/ice-fabric`, closing the loop between how fabric forms, how it is observed, and how it shapes flow.
