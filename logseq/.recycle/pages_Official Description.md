- Segmentation modules in Slicer core:
  collapsed:: true
	- [Segmentations](https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html): Adjust display options, manage segment representations and layers, copy/move segments between segmentations, convert between segmentation and models and labelmap volumes, export to files.
	- [Segment Editor](https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html): Create and edit segmentations from images using manual (paint, draw, …), semi-automatic (thresholding, region growing, interpolation, …) and automatic tools. A number of editor effects are built into the Segment Editor module and many more are provided by extensions (in “Segmentations” category in the Extensions Manager).
	- [Segment statistics](https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html): Computes intensity and geometric properties for each segment, such as volume, surface, minimum/maximum/mean intensity, oriented bounding box, sphericity, etc. See more information in.
- Extensions for creating/editing segmentations:
  collapsed:: true
	- [SegmentEditorExtraEffects](https://github.com/lassoan/SlicerSegmentEditorExtraEffects): Adds 8 more effects to Segment Editor.
	- [SurfaceWrapSolidify](https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify): fill in internal holes in a segmented image region or retrieve the largest cavity inside a segmentation.
	- [MONAILabel](https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabel): AI-based segmentation of various organs using MONAILabel.
	- [TotalSegmentator](https://github.com/lassoan/SlicerTotalSegmentator): AI-based fully automatic segmentation of 104 structures in whole-body CT images.
	- [DensityLungSegmentation](https://github.com/pzaffino/SlicerDensityLungSegmentation): AI-based fully automatic lung segmentation.
	- [HDBrainExtraction](https://github.com/lassoan/SlicerHDBrainExtraction): AI-based fully automatic skull stripping in brain MRI images.
	- [NVIDIA-AIAA](https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin): AI-based fully automatic segmentation of several organs. Segmentation is performed on a remote server.
	- [RVesselX](https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation): Semi-automatic liver parenchyma and vessels segmentation.
- Extensions for analyzing and processing segmentations:
  collapsed:: true
	- [Segment comparison](https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison): Compute similarity between two segments based on metrics such as Hausdorff distance and Dice coefficient.
	- [Segment registration](https://github.com/SlicerRt/SegmentRegistration) (provided by SegmentRegistration extension): Compute rigid or deformable transform that aligns two selected segments.
	- [SegmentMesher](https://github.com/lassoan/SlicerSegmentMesher): Creating volumetric (tetrahedral) meshes from segmentations.
	- [OpenAnatomy](https://github.com/PerkLab/SlicerOpenAnatomy): Export segmentations or model hierarchies for external viewers in glTF or OBJ format.
	- [Sandbox](https://github.com/PerkLab/SlicerSandbox): provides importer for Osirix ROI and SliceOmatic segmentation files.