# Coordinate
	- Reference
		- [Coordinate systems - Slicer Wiki](https://www.slicer.org/wiki/Coordinate_systems)
		- [Medical Image Coordinate Systems - MATLAB & Simulink (mathworks.com)](https://www.mathworks.com/help/medical-imaging/ug/medical-image-coordinate-systems.html)
	- **world**, **anatomical** and the **image coordinate system**
		- ![09ba26b4-2f6c-43f3-b08c-e632232bf715.jpeg](../assets/09ba26b4-2f6c-43f3-b08c-e632232bf715_1721709021047_0.jpeg)
		- World coordinate system:
			- Cartesian coordinate system
			- Every model (e.g. a MRI scanner or a patient) inside has its own coordinate system
		- Anatomical coordinate system
			-
	-
- # DICOM
	- Reference
		- The DICOM Homepage: [https://dicom.nema.org/](https://dicom.nema.org/)
		- DICOM on wikipedia: [https://en.wikipedia.org/wiki/DICOM](https://en.wikipedia.org/wiki/DICOM)
	- ## Tags
		- Look up tag
			- Clean and simple DICOM tag browser: [https://dicom.innolitics.com](https://dicom.innolitics.com/)
			- A useful tag lookup site: [http://dicomlookup.com/](http://dicomlookup.com/)
			- A hyperlinked version of the standard: [https://web.archive.org/web/20180624030937/http://dabsoft.ch/dicom/](https://web.archive.org/web/20180624030937/http://dabsoft.ch/dicom/)
		- ### Spacing Between Slices (0018, 0088)
			- different vendors use the **same** dicom tags for addressing different things. For instance, the attribute Spacing Between Slices (0018, 0088) means two **different** things depending on the vendor
			  [MRI Acronyms - Options - MR-TIP.com](https://www.mr-tip.com/serv1.php?type=cam&sub=1)
			  ![image.png](../assets/image_1699603683103_0.png)
			- [Slice cross-talk - Questions and Answers ​in MRI (mriquestions.com)](https://mriquestions.com/cross-talk.html)
			  ![image.png](../assets/image_1699603724651_0.png)
		- ### Slice thickness (0018,0050)
			- should not use *spacing between slices (0018,0088)* and *slice location (0020,1041)*
			  [[Insight-users] Slice spacing of DICOM series (itk.org)](https://itk.org/pipermail/insight-users/2008-November/027903.html)
			  ![image.png](../assets/image_1699605145869_0.png)
			- [Slice position and accuracy - Questions and Answers ​in MRI (mriquestions.com)](https://mriquestions.com/slice-parameters.html)
			  [Tag (0018,0050) Slice Thickness does not correspond to what I calculate in the image - Support - 3D Slicer Community](https://discourse.slicer.org/t/tag-0018-0050-slice-thickness-does-not-correspond-to-what-i-calculate-in-the-image/27438)
			  ![image.png](../assets/image_1699931070817_0.png)
			- Slice distance calculation [How to calculate space between dicom slices for MPR? - Stack Overflow](https://stackoverflow.com/questions/14930222/how-to-calculate-space-between-dicom-slices-for-mpr)
			  ![image.png](../assets/image_1699605530451_0.png){:height 322, :width 397}