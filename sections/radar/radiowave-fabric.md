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

```{admonition} Derivation
:class: dropdown

A single uniaxial crystal with c-axis direction $\mathbf c$ (a unit vector) has the permittivity tensor

$$
\boldsymbol\epsilon_{\text{crystal}} = \epsilon_a\,\mathbf I + \Delta\epsilon\,\mathbf c\,\mathbf c,
$$

where $\Delta\epsilon = \epsilon_c - \epsilon_a$. The check is direct: for a field along the c-axis the projection $\mathbf c\mathbf c$ acts as the identity and the response is $\epsilon_a + \Delta\epsilon = \epsilon_c$; for a field perpendicular to $\mathbf c$ the projection gives zero and the response is $\epsilon_a$.

When the wavelength is long compared with the grain size, the wave samples the volume average of the single-crystal permittivity over the c-axis orientation distribution. Averaging term by term,

$$
\boldsymbol\epsilon = \langle\boldsymbol\epsilon_{\text{crystal}}\rangle = \epsilon_a\,\mathbf I + \Delta\epsilon\,\langle\mathbf c\,\mathbf c\rangle = \epsilon_a\,\mathbf I + \Delta\epsilon\,\langle\mathbf c^2\rangle,
$$

where $\langle\mathbf c^2\rangle \equiv \langle\mathbf c\,\mathbf c\rangle$ is the second-order structure tensor. To put this in the form with the mean permittivity $\bar\epsilon$ out front, add and subtract $\tfrac13\Delta\epsilon\,\mathbf I$. The trace of $\langle\mathbf c^2\rangle$ is one (because $\mathbf c$ is a unit vector, $\mathrm{tr}\,\mathbf c\mathbf c = |\mathbf c|^2 = 1$), so its isotropic part is $\tfrac13\mathbf I$. Writing

$$
\boldsymbol\epsilon = \underbrace{\left(\epsilon_a + \tfrac13\Delta\epsilon\right)}_{\bar\epsilon}\mathbf I + \Delta\epsilon\left(\langle\mathbf c^2\rangle - \tfrac13\mathbf I\right),
$$

identifies $\bar\epsilon = \epsilon_a + \tfrac13\Delta\epsilon = \tfrac13(2\epsilon_a+\epsilon_c)$ as the orientation-averaged permittivity and isolates the anisotropic, traceless part. For isotropic ice $\langle\mathbf c^2\rangle = \tfrac13\mathbf I$ and the second term vanishes, as stated.
```

where $\langle\mathbf{c}^2\rangle$ is the second-order structure tensor, the orientation average of the outer product of the c-axis with itself. This tensor is the compact description of the fabric. Its three eigenvalues $\lambda_x,\lambda_y,\lambda_z$ sum to one and measure how strongly the c-axes cluster toward each principal axis. For perfectly isotropic ice $\langle\mathbf{c}^2\rangle = \tfrac{1}{3}\mathbf{I}$, the anisotropic term vanishes, and the bulk permittivity is the scalar $\bar\epsilon\,\mathbf{I}$. Any departure from isotropy shows up directly as anisotropy in $\boldsymbol{\epsilon}$.

## Fast and slow waves

Looking for plane-wave solutions turns the wave equation into an eigenvalue problem whose eigenvalues are the permitted wave speeds and whose eigenvectors are the permitted polarizations. For a radar looking straight down, the two relevant solutions are waves polarized horizontally along the two fabric principal axes, with eigenvelocities

$$
V_i = \frac{1}{\sqrt{\mu\,(\epsilon_a + \lambda_i\,\Delta\epsilon)}}, \qquad i = x,y.
$$

```{admonition} Derivation
:class: dropdown

Take the fabric principal axes as coordinate axes, so the structure tensor is diagonal, $\langle\mathbf c^2\rangle = \mathrm{diag}(\lambda_x,\lambda_y,\lambda_z)$, and from the bulk-permittivity result the permittivity tensor is diagonal too,

$$
\boldsymbol\epsilon = \mathrm{diag}(\epsilon_a+\lambda_x\Delta\epsilon,\ \epsilon_a+\lambda_y\Delta\epsilon,\ \epsilon_a+\lambda_z\Delta\epsilon).
$$

Seek a plane wave travelling vertically (down the $z$ axis), $\mathbf E = \mathbf E_0\,e^{\mathrm i(kz-\omega t)}$. Substituting into the wave equation and using $\nabla\!\cdot\!\mathbf E=0$ to drop the $\nabla(\nabla\!\cdot\!\mathbf E)$ term for the transverse (horizontal) components, the operator $\nabla^2$ gives $-k^2$ and $\partial^2/\partial t^2$ gives $-\omega^2$, so for each horizontal component $i = x,y$,

$$
k^2 E_{0i} = \mu\,\omega^2\,(\epsilon_a + \lambda_i\Delta\epsilon)\,E_{0i}.
$$

This is an eigenvalue problem: a wave polarized purely along $\hat x$ or purely along $\hat y$ is an eigenvector, with wavenumber

$$
k_i = \omega\sqrt{\mu\,(\epsilon_a + \lambda_i\Delta\epsilon)}.
$$

The phase velocity is $V_i = \omega/k_i$, giving

$$
V_i = \frac{1}{\sqrt{\mu\,(\epsilon_a + \lambda_i\Delta\epsilon)}},\qquad i=x,y,
$$

the printed result. The larger eigenvalue $\lambda_i$, the stronger the c-axis clustering along that axis, raises the effective permittivity and lowers the speed, so that polarization is the slow wave and the other is the fast wave.
```

A wave polarized along the axis where the c-axes cluster more strongly, the larger $\lambda_i$, travels more slowly. The two horizontal polarizations therefore propagate as a fast wave and a slow wave. This is the birefringence: a single radar pulse splits, in effect, into two polarizations that drift apart in time as they go deeper.

## From travel-time difference to fabric

It is convenient to work with the slowness $S = 1/V$, since travel time is slowness integrated along the path. The two-way travel-time difference between the two horizontally polarized waves, from the surface at $H$ down to depth $z$ and back, is the integral of the difference in their slownesses. Expanding about an isotropic reference state, this reduces to a simple and useful result,

$$
\Delta t(z) \approx \frac{\Delta S^2}{S_{\text{iso}}}\int_H^{z}\left(\lambda_x(z') - \lambda_y(z')\right)\,\mathrm{d}z',
$$

```{admonition} Derivation
:class: dropdown

The slowness of each polarization is $S_i = 1/V_i = \sqrt{\mu(\epsilon_a + \lambda_i\Delta\epsilon)}$. Travel time is slowness integrated along the path, so the one-way travel-time difference between the two horizontal polarizations from depth $z$ to the surface at $H$ is $\int (S_x - S_y)\,\mathrm dz'$, and the two-way difference is twice that. The quantity needed is the difference $S_x - S_y$.

Because the single-crystal anisotropy $\Delta\epsilon$ is small compared with $\epsilon_a$, expand the slowness about the isotropic reference $S_{\text{iso}} = \sqrt{\mu\,\epsilon_a}$ to first order in $\lambda_i\Delta\epsilon$:

$$
S_i = \sqrt{\mu\,\epsilon_a}\,\sqrt{1 + \frac{\lambda_i\Delta\epsilon}{\epsilon_a}} \approx S_{\text{iso}}\left(1 + \frac{\lambda_i\,\Delta\epsilon}{2\epsilon_a}\right).
$$

The difference between the two polarizations is then

$$
S_x - S_y \approx S_{\text{iso}}\,\frac{(\lambda_x-\lambda_y)\,\Delta\epsilon}{2\epsilon_a} = \frac{\mu\,\Delta\epsilon}{2\,S_{\text{iso}}}\,(\lambda_x-\lambda_y),
$$

using $S_{\text{iso}}/\epsilon_a = \mu/S_{\text{iso}}$ (from $S_{\text{iso}}^2 = \mu\epsilon_a$). Writing $\Delta S^2 \equiv \mu\,\Delta\epsilon$ for the single-crystal anisotropy and integrating along the path from $H$ to $z$, and folding the two-way factor and the order-unity numerical factor into the definitions as in {cite}`rathmann_notes`,

$$
\Delta t(z) \approx \frac{\Delta S^2}{S_{\text{iso}}}\int_H^{z}\left(\lambda_x(z') - \lambda_y(z')\right)\,\mathrm dz',
$$

the printed result. The travel-time splitting between orthogonal polarizations is, to first order, proportional to the depth-integrated horizontal fabric anisotropy $\lambda_x-\lambda_y$, which is what makes it invertible for fabric.
```

where $S_{\text{iso}}$ is the slowness of isotropic ice and $\Delta S^2 = \mu\,\Delta\epsilon$ measures the single-crystal anisotropy. The travel-time difference between orthogonally polarized radio waves is, to first order, proportional to the depth-integrated difference between the two horizontal fabric eigenvalues.

By measuring how the travel-time difference between orthogonal polarizations grows with depth and differentiating with respect to depth, one recovers the horizontal fabric anisotropy $\lambda_x - \lambda_y$ as a function of depth. Phase-sensitive systems such as ApRES measure this difference through the phase of the returns, and multi-element and polarimetric radars measure it across the full polarization plane. The fabric recovered this way can then be compared with the fabric that deformation models such as specfab predict, and fed back into the anisotropic flow law of {doc}`../ice_flow/ice-fabric`, closing the loop between how fabric forms, how it is observed, and how it shapes flow.
