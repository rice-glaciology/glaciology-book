# Ice fabric and anisotropy

Glen's flow law, as written in {doc}`ice-rheology`, treats ice as an isotropic material whose softness is the same in every direction. Real glacier ice is not isotropic. Each ice crystal is highly directional, and as ice deforms its crystals develop a preferred orientation that makes the bulk material flow more easily in some directions than in others. This crystal orientation fabric is a leading control on flow in places such as ice-stream shear margins and ice divides, and it also shapes how radar and seismic waves travel through ice. The chapter draws on the fabric modeling framework of Nicholas Rathmann and colleagues {cite}`rathmann2021`.

## The single crystal

Ice forms hexagonal crystals, each with a single symmetry axis called the c-axis, perpendicular to the basal planes. A crystal deforms most easily by shearing along its basal planes, in the way a deck of cards slides, and it resists deformation in other directions by a large factor, perhaps sixty times stiffer. A single ice crystal is therefore strongly anisotropic, and the direction of its c-axis tells you the direction in which it is hard to deform.

## Fabric and how it develops

A glacier is made of an enormous number of crystals, and what matters for bulk flow is the distribution of their c-axis orientations, known as the crystal orientation fabric. In freshly deposited ice the orientations are nearly random, and the bulk behavior is close to isotropic. As the ice deforms, each crystal rotates so that its c-axis turns away from the direction of extension and toward the direction of compression. Over time this lattice rotation, together with the recrystallization that accompanies it, organizes the orientations into recognizable patterns.

Two patterns are common. Under vertical compression near an ice divide, the c-axes cluster toward the vertical and form a single maximum. Under the simple shear found at the bed and in shear margins, the c-axes also cluster, in a way that aligns the easy-glide basal planes with the plane of shearing. Under horizontal extension the c-axes spread into a girdle. The fabric that develops is a record of the deformation the ice has experienced.

## Anisotropic flow

Once a fabric is present, the ice no longer obeys an isotropic flow law. A single-maximum fabric makes the ice much softer for shear parallel to the aligned basal planes and stiffer for compression along the cluster. The resulting directional enhancement factors can reach values of order ten, which means that ignoring fabric can misrepresent the strain rate by nearly an order of magnitude in the directions that matter most. This is why fabric is important in shear margins, where the concentrated shear both creates a strong fabric and is in turn made easier by it, and near divides, where it affects the age-depth relationship used to interpret ice cores.

Modeling this behavior requires tracking the orientation distribution as the ice flows. A practical approach represents the distribution as a sum of spherical-harmonic components and evolves those components under lattice rotation and recrystallization, from which the bulk anisotropic viscosity can be computed. The specfab framework of {cite}`rathmann2021` does this, and it also predicts the bulk dielectric and elastic properties of the fabric, which connects the deformation directly to what radar and seismic methods can measure.

## Observing fabric

Fabric has traditionally been measured on thin sections cut from ice cores, which show the c-axis orientation of each crystal directly but only at the few sites where cores exist. Because an aligned fabric makes ice electrically and elastically anisotropic, it can also be sensed remotely. Polarimetric radar, which transmits and receives in different polarizations, responds to the dielectric anisotropy set by the fabric, and seismic methods respond to the elastic anisotropy. These geophysical measurements, which the group pursues with multi-element and polarimetric radar, offer a way to map fabric over the wide areas where ice cores are not available, and the fabric models provide the link needed to interpret them.
