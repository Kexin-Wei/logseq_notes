- US-US Image Registration
	- **Input data**: 1st US image
	  
	  **Output data**: Subsequent US frames
	  
	  **Registration methods**: Convolutional Neural Network (CNN) based rigid registration and transform matrix alignment
	  
	  **Measurement method**: TRE (target registration error) is the distance between the target landmark and registered landmark. Ideally it should be 0.
	  
	  **World coordinate**: focus point of US (Pointbase Reg)
	  
	  **Ground truth**: first frame of US images
	  
	  **Image registration**: all the US frames will be registered to the first frame (ground truth)
	  
	  **Landmark (L1)**:  reference point (the first automatically selected point for delineating the points of interest for tracking.
	  
	  **Point-of-interest (red dot)**: manually choose the point for the treatment region (will be verified by clinicians (may remove and add more points).