file:: [audet_dennis_2006_mesh adaptive direct search algorithms for constrained optimization.pdf](file://D:/Dropbox/Study/ZoteroFiles/audet_dennis_2006_mesh adaptive direct search algorithms for constrained optimization.pdf)
file-path:: file://D:/Dropbox/Study/ZoteroFiles/audet_dennis_2006_mesh adaptive direct search algorithms for constrained optimization.pdf

- MADS extends the Generalized Pattern Search (GPS) class by allowing local exploration, called polling, in an asymptotically dense set of directions in the space of optimization variables.
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c777-4338-4f66-8d7f-29d0ceacac02
- The main GPS convergence result is to identify limit points ˆx, where the Clarke generalized derivatives are nonnegative in a finite set of directions, called refining directions.
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c799-1c2d-4f8e-8dc4-63b7d7e1d411
- The main result of this paper is that the MADS algorithms can generate an asymptotically dense set of refining directions.
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c800-4dff-490b-be2f-34ae5646c6a5
- For LTMADS, an implementable instance of MADS, the refining directions are dense in the hypertangent cone at ˆx with probability1. 
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c846-c8f1-4771-9c77-9bc35ee328e5
- In the unconstrained case, where Ω = Rn, this new class of algorithms occupies a position somewhere between the Generalized Pattern Search (GPS) class [22], as organized in [6], and the Coope and Price frame-based methods [10].
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c8f3-a91f-4e86-b12d-c4f31984a805
- MADS algorithms are frame-based methods
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c923-d529-41b3-8b86-da706d823f57
- they are specifically aimed at ensuring an asymptotically dense set of polling directions.
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c944-c027-4698-ae19-9ce4f708326f
- The convergence analysis here is based on Clarke’s calculus [8] for nonsmooth functions. 
  ls-type:: annotation
  hl-page:: 1
  hl-color:: yellow
  id:: 63c0c958-cfaa-4fc9-8f48-a8f0df041b10
- MADS produces unconstrained limit points at which the Clarke derivatives are nonnegative for every direction in Rn.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63c0c9f3-b338-4694-a4fc-6ada05ad396c
- Besides the advantages for the unconstrained case of an asymptotically dense set of refining directions, MADS can also treat a wide class of nonlinear constraints by the “barrier” approach.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63c0ca03-533f-42d6-a879-910a936368d6
- MADS is an iterative algorithm where at each iteration a finite number of trial points are generated, and the infeasible trial points are discarded. 
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63c0cc8c-1069-4211-a248-45b220b6abdf
- Each of these trial points lies on the current mesh, constructed from a finite set of nD directions D ⊂ Rn scaled by a mesh size parameter ∆m k ∈ R+
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63c0cca2-859f-460e-9318-17df3a46f15c
- Defining the mesh this way ensures that all previously visited points lie on the mesh, and that new trial points can be selected around any of them using the directions in D. 
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63c0ccf0-4a6c-42e5-8b77-0cef4a364f86
- The objective of the iteration is to find a trial mesh point with a lower objective function value than the current incumbent value fΩ(xk).
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63c0cdb3-d50f-4dbe-bebf-6ca691056713
- The evaluation of fΩ at a trial point x is done as follows.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0ced3-2786-482e-bcbb-c927362a4eac
- if x ∈ Ω, then f (x) is evaluated.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0cedc-1a56-4cda-8f64-6591d6b921b0
- Each iteration is divided into two steps.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0cee9-c66b-450e-8450-2b0a8f311b12
- The first, called the SEARCH step, has the same flexibility as in GPS. It allows evaluation of fΩ at any finite number of mesh points. 
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0cefa-b84e-4884-82f3-6147379403a2
- When an improved mesh point is generated, then the iteration may stop, or it may continue if the user hopes to find a better improved mesh point.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0d08e-5751-4f2b-8db2-1383ea83b63d
- Coarsening the mesh when improvements in fΩ are obtained can speed convergence.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0d0a9-1267-4ddf-ad3b-5104dc489a4b
- second step, called the POLL, is invoked before terminating the iteration.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0d0be-550c-4e7a-b9b6-8c8a7f75fab0
- The mesh size parameter ∆m k+1 is reduced to increase the mesh resolution,
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0d181-06c0-410e-a766-7e587a7db6c8
- MADS frame is constructed using a current incumbent solution xk (called the frame center) and the poll and mesh size parameters ∆p k and ∆m k to obtain a positive spanning set of directions Dk. Unlike GPS, generally the MADS set of directions Dk is not a subset of D.
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63c0d1eb-2b88-4ed0-92fd-185b583e5913
- If the POLL step fails to generate an improved mesh point then the frame is called a minimal frame, and the frame center xk is said to be a minimal frame center. This leads to mesh refinement. 
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63c0d214-9b52-4925-b91d-f179ea5fbe25
- [:span]
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63c0d26d-74fd-4ef4-ac36-df9a71350574
  hl-type:: area
  hl-stamp:: 1673581164865
- poll size parameter ∆p k ∈ R+ for iteration k.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63c0d341-6b4c-44eb-a6e1-b86b2ca9ba3c
- [:span]
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63c0d3c9-e032-46ba-8c66-7c6cb4cedf96
  hl-type:: area
  hl-stamp:: 1673581512846
- [:span]
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63c0d586-26a8-4ade-838a-0398bcb5c54c
  hl-type:: area
  hl-stamp:: 1673581957401
- [:span]
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63c0d58f-6ae7-4fa9-928a-05413bdc3b73
  hl-type:: area
  hl-stamp:: 1673581966852
- To each mesh size parameter ∆m k , we assign an integer ` = − log4(∆m k ) ∈ N so that ∆m k = 4−`.
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63c0f129-c5aa-4ade-830d-2394443aa634
- [:span]
  ls-type:: annotation
  hl-page:: 15
  hl-color:: yellow
  id:: 63c0f1a3-b17f-4e3e-a14d-8144e33dfa07
  hl-type:: area
  hl-stamp:: 1673589153847