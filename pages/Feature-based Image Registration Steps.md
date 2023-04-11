- > http://staff.utia.cas.cz/sroubekf/papers/EUSIPCO_07_fusion_tut.pdf
- Feature Detection
  collapsed:: true
	- Feature defination:
	  1. Distinctive and detectable objects
	  2. Physical interpretability
	  3. Frequently spread over the image
	  4. Enough common elements in all images
	  5. Robust to degradations
	- Methods
		- Area-based methods - windows
		- Feature-based methods (higher level info)
			- Distinctive points
				- 1. line intersections
				  2. max curvature points
				  3. inflection points
				  4. centers of gravity
				  5. local extrema of wavelet transform
			- Corners
				- 1. image derivatives (Kitchen-Rosenfled, Harris)
				  2. intuitive approaches (Smith-Brady)
			- Lines
			  :LOGBOOK:
			  CLOCK: [2022-12-30 Fri 10:15:17]
			  :END:
				- 1. line segments (roads, anatomic structures)
				  2. contours
				  3. edge detectors ( Canny, Maar, wavelets)
			- Regions
				- 1. closed- boundary objects (lakes, fields, shadows)
				  2. level sets
				  3. segmentation methods
			- invariant regions with respect to assumed degradation scale
				- 1. virtual circles (Alhichri & Kamel) affine
				  2. based on Harris and edges (Tuytelaars&V Gool) affine
				  3. maximally stable extremal regions (Matas et al.)
- Feature matching
  collapsed:: true
	- Match pattern
		- feature
		- intensity
	- Area-based methods: similarity measures calculated directly from the image graylevels
		- image correlation
		- image differences
		- phase correlation
		- mutual information
	- Feature-based methods: symbolic description of the features matching in the feature space (classification)
	- Examples
		- Area-based methods:
			- CROSS-CORRELATION
			- PYRAMIDAL REPRESENTATION
			- PHASE CORRELATION
			- LOG-POLAR TRANSFORM
			- RTS PHASE CORRELATION
			- MUTUAL INFORMATION
		- Feature-based methods:
			- COMBINATORIAL - GRAPH
			- COMBINATORIAL - CLUSTER
			- FEATURE SPACE MATCHING
- Transform model estimation
  collapsed:: true
	- > http://staff.utia.cas.cz/sroubekf/papers/EUSIPCO_07_fusion_tut.pdf
	- Global functions
		- similarity
		- affine
		- projective transform
		- low-order polynomials
	- Local functions
		- piecewise affine
		- piecewise cubic
		- thin-plate splines
		- radial basis functions
- Image resampling and transformation
  collapsed:: true
	- trade-off between accuracy and computational complexity
	- forward method
	- backward method
	- Interpolation method
		- bilinear
		- spline
	- Transform method
		- rigid
		- affine
		- spline warps
- Accuracy Evaluation
  collapsed:: true
	- Localization error
	- Matching error
	- Alignment error