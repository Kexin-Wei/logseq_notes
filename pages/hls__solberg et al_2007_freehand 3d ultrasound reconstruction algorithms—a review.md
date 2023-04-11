file:: [solberg et al_2007_freehand 3d ultrasound reconstruction algorithms—a review.pdf](file://D:/Dropbox/Study/ZoteroFiles/solberg et al_2007_freehand 3d ultrasound reconstruction algorithms—a review.pdf)
file-path:: file://D:/Dropbox/Study/ZoteroFiles/solberg et al_2007_freehand 3d ultrasound reconstruction algorithms—a review.pdf

- Voxel-Based Methods (VBM)
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63bccf33-9fcd-4080-ae40-8eb0536a12a1
- Voxel Nearest Neighbor (VNN)
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63bccf40-7619-4dad-bb78-bf8c6f74abd2
- 1D interpolation (Berg et al. 1999)
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63bccf7f-d45f-40fe-8ce1-2c7db1cad933
- use a tilt scan and present two interpolation methods based on the maximum angle between two enclosing scan planes. If the maximum angle is less than 20°, a linear interpolation orthogonal to a virtual scan plane in the middle of the scan planes are used (Fig. 2a). If the maximum angle is more than 20°, each 2D scan plane is defined with a certain thickness defining the region where it contributes to the interpolation (Fig. 2b). The interpolation in both cases uses a linear weight decreasing with the distance to the scan planes. 
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd00c-29c7-4f70-86f1-3491b2577591
- [:span]
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63bcd01c-44aa-44dd-b8ca-35d6b442bc9a
  hl-type:: area
  hl-stamp:: 1673318427719
- An interpolation from the two nearest surrounding slices is used by Trobaugh et al. (1994).
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd038-38db-4d4a-8b21-b11efbadd558
- traverses the voxels and finds the two nearest 2D slices on each side of the voxel (Fig. 3). A normal is calculated to each of these slices and the four surrounding pixels are bilinearly interpolated in each plane. The final voxel value is calculated as a weighted sum with contributions from the two planes based on the distances from the voxel to the planes.
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd05c-c826-4e45-9fab-437b4713285f
- [:span]
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63bcd084-0f1e-4ed5-9489-a616484164b3
  hl-type:: area
  hl-stamp:: 1673318531312
- Probe Trajectory (PT)
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd0b1-e6af-4836-9d33-5a4b0d7eebf1
- Instead of using an orthogonal projection of the closest2D planes to a point, a probe trajectory is estimated and used for finding the corresponding pixels in the nearest2D planes (Fig. 4).
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd0c5-246b-48ef-a940-e595b0a5450e
- [:span]
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63bcd0ea-7578-45c4-a24f-440cb868a8ff
  hl-type:: area
  hl-stamp:: 1673318633607
- Voxel-based tri-linear interpolation (Thune et al.1996)
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd132-7fd2-4372-93c9-72ef80d29498
- One pixel contributes to one voxel.
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd15f-3e9e-4cbe-b35b-4471300ab70d
- A PBM may consist of two steps: a Distribution Step (DS) and a Hole-Filling Step (HFS).
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bcd2e9-316c-4ce5-8ba1-e634f58dc834
- [:span]
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63bcd60f-d59b-4578-afd7-a0ce4b4129ae
  hl-type:: area
  hl-stamp:: 1673319949963
- [:span]
  ls-type:: annotation
  hl-page:: 9
  hl-color:: yellow
  id:: 63bcd657-3083-4337-9d24-b18b91d56c06
  hl-type:: area
  hl-stamp:: 1673320022364
- The Solus system (Carr et al. 2000) is based on the Stradx system (Prager et al. 1999).
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63bcd66d-4d5e-4be8-916c-c32b406d40b7
- [:span]
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 63bcdef8-cb39-4371-9a3a-2eb28980c707
  hl-type:: area
  hl-stamp:: 1673322231694
- Barry et al. (1997) use a spherical kernel
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63bcdf58-361a-48b0-aa29-f7fd6b9e5e73
- spherical Gaussian kernel (Fig. 7a). 
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63bcdf62-1dbf-481b-ad04-8e63f245b003
- The Point Spread Function of the US system is used as an input to the applicability function used in the Normalized Convolution.
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63bcdf8c-458b-441d-895a-c12758af9b3b
- [:span]
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63bcdfa0-4f26-4eb2-a651-a2207b7fe88c
  hl-type:: area
  hl-stamp:: 1673322399473
- An ellipsoid truncated Gaussian kernel with Gaussian weighting is presented by Ohbuchi et al. (1992).
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63bcdfbd-e14f-497d-ae84-43354a885cf5
- The Radial Basis Function (RBF) interpolation(Rohling et al. 1999) 
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63bcf3e9-2191-4764-98b7-30db54b75f51
- The Rayleigh reconstruction/interpolation with a Bayesian framework (Sanches and Marques 2000) 
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63bcf3ff-d4d8-4aa6-ab24-4dccebb8f7ce
- [:span]
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63bcf43a-2ae7-4ab3-85f0-8a27d8100f47
  hl-type:: area
  hl-stamp:: 1673327673954