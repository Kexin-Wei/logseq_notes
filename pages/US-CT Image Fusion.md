- **Input**: CT (reference) and US images (moving images)
  **Output**: Transformed CT images
  **Strategy**: full sequence learning
  **Method**:
	- Calculate the distance between outline/contour of CT plane and US
	- Align the US to CT (fixed image) in accordance with the distance map through haudsoff and mean surface distances
	- Register the US images in 3D space