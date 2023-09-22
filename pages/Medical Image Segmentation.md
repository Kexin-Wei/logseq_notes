# Dataset
	- Brain
		- [2012 MICCAI Multi-Atlas Labeling Challenge Data](http://www.neuromorphometrics.com/2012_MICCAI_Challenge_Data.html)
			- 30 manually labeled MRI brain scans, 25 unique subjects, 5 subjects scanned twice.
	- [[Prostate MRI dataset]]
	  id:: 64238f0e-d27f-42c4-8f37-ab486ddffd02
- # Segmentation Algorithm
	- Region Grow
		- [Segmentation/segmentation_methods.ipynb at main · gilzeevi25/Segmentation (github.com)](https://github.com/gilzeevi25/Segmentation/blob/main/segmentation_methods.ipynb)
- # Segmentation Tool #👩‍💻software
	- Manually Segmentation Software #👩‍💻software
	  collapsed:: true
		- ~~[MedSeg (amazonaws.com)](http://htmlsegmentation.s3.eu-north-1.amazonaws.com/index.html)~~
		- ~~[BioImage Suite Web](https://bioimagesuiteweb.github.io/webapp/)~~
		- [Files · master · Kenneth Philbrick / rilcontour · GitLab](https://gitlab.com/Philbrick/rilcontour/tree/master)
		  id:: 641ab9a9-6067-4e77-832d-7066cfbd32c1
		- [The Medical Imaging Interaction Toolkit (MITK) - mitk.org](https://www.mitk.org/wiki/The_Medical_Imaging_Interaction_Toolkit_(MITK))
		- 3D Slicer
		- ITK-Snap
		- [Demo (deepinfer.org)](http://www.deepinfer.org/models/prostate-segmenter/)
		  collapsed:: true
			- Only 1 type of MRI is segmented, mainly the centre part (50%)
			- Using docker, each time only one image and need a new container
			- ![image.png](../assets/image_1680253719469_0.png)
			-
	- ![AStar UCAnet](../assets/ISCAS_2023_UCAnet.pdf)
	  collapsed:: true
		- ![image.png](../assets/image_1680231283494_0.png)
	- [[SAM Segment Anything Model]]
	- [[TotalSegmentator]]
	- [[Train your own dataset using nnUNet]]
	- [Biomedisa](https://biomedisa.de/)
		- for biology not medical
	- [Github - SALMON: based on MONai](https://github.com/davidiommi/Pytorch--3D-Medical-Images-Segmentation--SALMON)
		- based on Monai label, hard to implement
	- [Github - SAML](https://github.com/liuquande/SAML)
		- shaped better, potential alternative
	- [Github MedSAM](https://github.com/bowang-lab/MedSAM)
		- seem only good for box
	- [Github dcmqi](https://qiicr.gitbook.io/dcmqi-guide/use-cases/prostate)
	- [GitHub - OscarPellicer/prostate_lesion_detection: Model for the detection, segmentation, and classification of prostate lesions from mpMRI, using ProstateX data and Retina U-Net](https://github.com/OscarPellicer/prostate_lesion_detection)
	- [GitHub - OnofreyLab/prostate_atlas_segm_miccai2022: Atlas-based Semantic Segmentation of Prostate Zones - MICCAI 2022](https://github.com/OnofreyLab/prostate_atlas_segm_miccai2022/tree/main)
	- [GitHub - amanbasu/3d-prostate-segmentation: Segmentation of prostate from MRI scans](https://github.com/amanbasu/3d-prostate-segmentation)
	- [GitHub - sulaimanvesal/ProstateMRISegmentation: PyTorch Implementation for: Deep Learning-Based Model For Prostate-MRI Segmentation](https://github.com/sulaimanvesal/ProstateMRISegmentation)