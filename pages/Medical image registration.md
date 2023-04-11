title:: Image Registration
> Reference
1. https://www.robots.ox.ac.uk/~jmb/lectures/InformaticsLecture7.pdf
2. Golkar, Ehsan, Ashrani A. Abd Rahni, and Riza Sulaiman. "Comparison of image registration similarity measures for an abdominal organ segmentation framework." _2014 IEEE Conference on Biomedical Engineering and Sciences (IECBES)_. IEEE, 2014.

- # Fundamentals
	- Registration (matching)
	  collapsed:: true
		- Geometric (and Photometric) alignment of one image with another
		- Images may be of same or different types (MR, CT, …) - mono-modality registration vs multi-modality registration
	- Fusion (matching + complete)
	  collapsed:: true
		- No single image modality provides a complete picture in all cases
		- images of different modalities & infer a more comprehensive story than provided by either
	- Fusion  = registration + combination of each own representation
	- [[Homogeneous Transformation]]
- # Categories
	- By Modalities
		- Mono-modality Registration
			- [[Ultrasound Image Registration]]
		- Multi-modality Registration
			- [[US-MRI Image Registration]]
	- By [[Homogeneous Transformation]]
# Purpose
	- map $J(x)$ to $I(x)$ using projection $T$
	- Goal: $T=\text{arg} \min\sum_k \text{sim} (I(x), J[T(x)])$
		- $\text{sim}()$ is the similarity criterion
# Steps
	- [[Feature-based Image Registration Steps]]
	- Transformation of the Moved Image
	- Interpolation of images
	- Similarity Calculation of Moved and Fixed Image
	- Optimization
- # [[Similarity Criterion of Image Registration]]
- # [[Optimization]]
	- Papers
		- ~~[[@A survey of medical image registration – under review]]~~
		- [[@Medical image registration: a review]]
		- Deformable Medical Image Registration: A Survey https://ieeexplore.ieee.org/abstract/document/6522524 #📑READ
		- Fast and Robust Matching for Multimodal Remote Sensing Image Registration https://ieeexplore.ieee.org/abstract/document/8766118 #📑READ
		- Explicit B-spline regularization in diffeomorphic image registration https://www.frontiersin.org/articles/10.3389/fninf.2013.00039/full #📑READ
		- A critical review of image registration methods https://www.tandfonline.com/doi/abs/10.1080/19479831003802790 #📑READ