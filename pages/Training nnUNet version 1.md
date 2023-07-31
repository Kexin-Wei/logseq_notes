- ## Training examples
	- [Example 1 - prostate](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/inference_example_Prostate.md)
	- [Example 2 - liver](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/training_example_Hippocampus.md)
	- [Training Benchmark](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/expected_epoch_times.md)
- ## [1. How to run nnU-Net on a new dataset](https://github.com/MIC-DKFZ/nnUNet#how-to-run-nnu-net-on-a-new-dataset)
	- Install software: Python3, Pytorch, `pip install nnunet`
	- Windows can use bash shell: [Set up Paths of the dataset](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/setting_up_paths.md)
		- ```bash
		  #! /usr/bin/env bash
		  export nnUNetPath=$PWD/../nnUNet_train
		  export nnUNet_raw_data_base=$nnUNetPath/nnUNet_raw_data_base
		  export nnUNet_preprocessed=$nnUNetPath/nnUNet_preprocessed
		  export RESULTS_FOLDER=$nnUNetPath/nnUNet_trained_models
		  ```
- ## 2. Prepare dataset
	- [Dataset Conversion for MSD dataset](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_conversion.md)
	  collapsed:: true
		- MSD: [Medical Segmentation Decathlon](http://medicaldecathlon.com/)
		- Need to modify path for bash shell and **windows** platform, see [Github repo](https://github.com/Kexin-Wei/nnUNet)
		  collapsed:: true
			- ```python
			  def split_4d_nifti(filename, output_folder, add_zeros=False):
			      img_itk = sitk.ReadImage(filename)
			      dim = img_itk.GetDimension()
			      if sys.platform.startswith("win32"): # fix bash and windows path issue. replace / to \\
			          file_base = filename.split("\\")[-1]
			      else:
			          file_base = filename.split("/")[-1] 
			      ...
			      else:
			          for i, t in enumerate(range(img_npy.shape[0])):
			                  img = img_npy[t]
			                  img_itk_new = sitk.GetImageFromArray(img)
			                  img_itk_new.SetSpacing(spacing)
			                  img_itk_new.SetOrigin(origin)
			                  img_itk_new.SetDirection(direction)
			                  if sys.platform.startswith("win32"): # fix bash and windows path issue. replace / to \\
			                      sitk.WriteImage(img_itk_new, join(output_folder, file_base[:-7] + "_%04.0d.nii.gz" % i).replace("/","\\")) 
			                  else:
			                      sitk.WriteImage(img_itk_new, join(output_folder, file_base[:-7] + "_%04.0d.nii.gz" % i))             
			  ```
	- From other dataset
	  collapsed:: true
		- [data_format_inference.md](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/data_format_inference.md)
	- `dataset.json`
	  collapsed:: true
		- **NEW:** There now is a utility with which you can generate the dataset.json automatically. You can find it [here](https://github.com/MIC-DKFZ/nnUNet/blob/master/nnunet/dataset_conversion/utils.py) (look for the function `generate_dataset_json`). See [Task120](https://github.com/MIC-DKFZ/nnUNet/blob/master/nnunet/dataset_conversion/Task120_Massachusetts_RoadSegm.py) for an example on how to use it. And read its documentation!
			- [Task120_Massachusetts_RoadSegm.py](https://github.com/MIC-DKFZ/nnUNet/blob/master/nnunet/dataset_conversion/Task120_Massachusetts_RoadSegm.py)
			- [Task076_Fluo_N3DH_SIM.py](https://github.com/MIC-DKFZ/nnUNet/blob/master/nnunet/dataset_conversion/Task076_Fluo_N3DH_SIM.py)
			- [Task075_Fluo_C3DH_A549_ManAndSim.py](https://github.com/MIC-DKFZ/nnUNet/blob/master/nnunet/dataset_conversion/Task075_Fluo_C3DH_A549_ManAndSim.py)
		- File example
			- ```json
			  { 
			   "name": "PROSTATE", 
			   "description": "Prostate transitional zone and peripheral zone segmentation",
			   "reference": "Radboud University, Nijmegen Medical Centre",
			   "licence":"CC-BY-SA 4.0",
			   "relase":"1.0 04/05/2018",
			   "tensorImageSize": "4D",
			   "modality": { 
			     "0": "T2", 
			     "1": "ADC"
			   }, 
			   "labels": { 
			     "0": "background", 
			     "1": "PZ", 
			     "2": "TZ"
			   }, 
			   "numTraining": 32, 
			   "numTest": 16,
			   "training":[{"image":"./imagesTr/prostate_16.nii.gz","label":"./labelsTr/prostate_16.nii.gz"},{"image":"./imagesTr/prostate_04.nii.gz","label":"./labelsTr/prostate_04.nii.gz"},...], 
			   "test": ["./imagesTs/prostate_08.nii.gz","./imagesTs/prostate_22.nii.gz","./imagesTs/prostate_30.nii.gz",...]
			   }
			  ```
- ## 3. Train Dataset
	- [Command explanation in Github](https://github.com/MIC-DKFZ/nnUNet#model-training)
	- ```bash
	  nnUNet_train 3d_fullres nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz
	  
	  # e.g.
	  nnUNet_train 3d_fullres nnUNetTrainerV2 Task005_Prostate 3 --npz
	  
	  ```
- ## 4. Predict Dataset
	- [Command explanation in Github](https://github.com/MIC-DKFZ/nnUNet#run-inference)
	- ```bash
	  nnUNet_predict -i INPUT_FOLDER -o OUTPUT_FOLDER -t TASK_NAME_OR_ID -m CONFIGURATION --save_npz
	  
	  # e.g.
	  nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_raw_data/Task005_Prostate/imagesTs/ -o OUTPUT_DIRECTORY -t 5 -m 3d_fullres
	  ```