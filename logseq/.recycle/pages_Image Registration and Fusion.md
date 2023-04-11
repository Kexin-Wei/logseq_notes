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
- # Image Registration
  > Reference
  1. https://www.robots.ox.ac.uk/~jmb/lectures/InformaticsLecture7.pdf
  2. Golkar, Ehsan, Ashrani A. Abd Rahni, and Riza Sulaiman. "Comparison of image registration similarity measures for an abdominal organ segmentation framework." _2014 IEEE Conference on Biomedical Engineering and Sciences (IECBES)_. IEEE, 2014.
	- [[Intro of Image Registration]]
	- [[Similarity Criterion of Image Registration]]
	- [[Optimization]]
	- Papers
		- ~~[[@A survey of medical image registration – under review]]~~
		- [[@Medical image registration: a review]]
		- Deformable Medical Image Registration: A Survey https://ieeexplore.ieee.org/abstract/document/6522524 #📑READ
		- Fast and Robust Matching for Multimodal Remote Sensing Image Registration https://ieeexplore.ieee.org/abstract/document/8766118 #📑READ
		- Explicit B-spline regularization in diffeomorphic image registration https://www.frontiersin.org/articles/10.3389/fninf.2013.00039/full #📑READ
		- A critical review of image registration methods https://www.tandfonline.com/doi/abs/10.1080/19479831003802790 #📑READ
- # Image Fusion
	- [[Categories of  Image Fusion]]
	- [[Methods of Image Fusion]]
		- > [[@A Review : Image Fusion Techniques and Applications]]
		- IHS Transform
		- Principal Component Analysis
		- Pyramid Techniques
		- High Pass Filtering
		- Wavelet Transform
		- Artificial Neural Network
		- Discrete Cosine Transform
	- Application
		- Cancer staging
		- **Biopsy planning**
		- **Radiotherapy treatment planning**
		- Quantitative assessment of treatment response
		- Pre-surgical assessment of other conditions, e.g. epilepsy
		- As an effective communication tool when reporting to clinical meetings, referring physicians or to patients
		- Whenever multiple data sources may be better assessed together
	- Papers
		- [[@A Review : Image Fusion Techniques and Applications]]
		- ~~No method mentioned [[@Real-Time Image Fusion Involving Diagnostic Ultrasound]]~~
		- [[@Medical image fusion: A survey of the state of the art]]
	- Fusion Platforms and Softwares
		-