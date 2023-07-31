- # Set environment variables
  collapsed:: true
	- bash script 
	  ```bash
	  export nnUNetPath=$PWD/../nnUNet_dataset
	  export nnUNet_raw_data_base=$nnUNetPath/nnUNet_raw_data_base
	  export nnUNet_preprocessed=$nnUNetPath/nnUNet_preprocessed
	  export RESULTS_FOLDER=$nnUNetPath/nnUNet_trained_models
	  ```
	- Powershell
	  ```powershell
	  
	  $Env:nnUNet_raw = "C:/Users/fabian/nnUNet_raw"
	  $Env:nnUNet_preprocessed = "C:/Users/fabian/nnUNet_preprocessed"
	  $Env:nnUNet_results = "C:/Users/fabian/nnUNet_results"
	  ```
	- cmd
	  ```shell
	  set nnUNet_raw=C:/Users/fabian/nnUNet_raw
	  set nnUNet_preprocessed=C:/Users/fabian/nnUNet_preprocessed
	  set nnUNet_results=C:/Users/fabian/fabian/nnUNet_results
	  ```
	- To verify
		- bash: `echo ${nnUNet_raw}`
		- powershell: `echo $Env:[variable_name]`
		- cmd.exe: `echo %[variable_name]%`
	-
- # Dataset Construction
	- formats are supported:
		- NaturalImage2DIO: .png, .bmp, .tif
		- NibabelIO: .nii.gz, .nrrd, .mha
		- NibabelIOWithReorient: .nii.gz, .nrrd, .mha. This reader will reorient images to RAS!
		- SimpleITKIO: .nii.gz, .nrrd, .mha
		- Tiff3DIO: .tif, .tiff. 3D tif images! Since TIF does not have a standardized way of storing spacing information, nnU-Net expects each TIF file to be accompanied by an identically named .json file that contains three numbers (no units, no comma. Just separated by whitespace), one for each dimension.
	-
- [[Training nnUNet version 1]]
  id:: 64c76179-a332-41f6-8366-0d12dcc3f614