- Cavitation Detection Equipment
	- Talk 1: Passive Cavitation Detector
	  collapsed:: true
		- Experiment Setting up
		  ![](/../assets/pcd_detector.png)
		- PCD pulse response speed
		  ![](/../assets/pcd_response.png)
		- PCD type from Sonic Concepts
		  collapsed:: true
		  ![](/../assets/pcd_type.png)
			- focused
			- ring-shaped
	- Talk 2: Receiving and Processing Passive Signal
	  collapsed:: true
		- US with and without Bubble Noise
		  ![](/../assets/bubble_us.png)
		- window
		  collapsed:: true
		  ![](/../assets/windows.png)
		  ![](/../assets/windows_compare.png)
			- Hamming window
			- Blackman-Harris window
		- Comb Filter for Harmonics
		  ![](/../assets/harmonics_filter.png)
		- Alternative processing
		  collapsed:: true
			- Wavelet Transform
			- Single Value Decomposition
		- Estimating Emitted Cavitation Power
		  collapsed:: true
			- PCD focus is not at cavitation
	- Talk 3: Considerations for Calibrated Cavitation Monitoring
	  collapsed:: true
		- ![](/../assets/harmonic_ultra.png)
		- Beamforming
		  collapsed:: true
			- Point Spread Function (PSF)
			  ![](/../assets/single_element_pcd.png)
	- Talk 4: Transcranial Cavitation Monitoring
	  collapsed:: true
		- mentioned a paper of high-resolution ultrasound image used in brain, which can see clear bubbles in vessel/pipes
	- Talk 5: Clinical Implementation of Single-element PCD
	  collapsed:: true
		- Harmonic shape
		  ![](/../assets/inertial_frequency.png)
		- Harmonic shape
		  ![](/../assets/inertial_frequency2.png)
		- ![](/../assets/transducer_pcd.png)
	- Talk 6: ExAblate Cavitation Detection
	  collapsed:: true
		- Target: Brain
		- PCD number 0->2->8
		  ![](/../assets/pcd_location.png)
		- BBN
		  ![](/../assets/stable_vs_inertial.png)
- Cavitation Localization and Mapping
	- Talk 1: Passive Acoustic Mapping for Cavitation Imaging: From Where the Bubble Tolls
	  collapsed:: true
		- Prior work investigated the synchronous investigation of cavitation with single-element PCDs synchronously with conventional B-mode imaging and found that substantial cavitation could **exist long before** it was detected on a B-mode image
		  ![](/../assets/cavitation_no_b_mode.png)
		- passive cavitation detection was necessary for the detection of clinically relevant cavitation activity, and that the use of multi-element arrays used as passive detectors could enable mapping of cavitation in real time with increased SNR compared to single-element systems.
		- PAM localizes sources of non-linearity in general, and cavitating bubbles in particular, through the application of coherence metrics applied to passively received signals across several detectors
		  ![](/../assets/pam.png)
		  ![](/../assets/pam_development.png)
		- Basis for PAM: Time Exposure Acoustics (TEA-PAM) 10:30
		- Echo Focusing
	- Talk 2: Localisation, Mapping and Quatification for Bubble Activity in Transcranial and transverterbral Applications
	  collapsed:: true
		- 3 hydrophones localise cavitation in 2D
		- Bubble-based Phase Correction
	- Talk 3: Active and Passive Cavitation Localisation and Mapping (including Histotripsy)
	  collapsed:: true
		- ![](/../assets/active_passive_cavitaion_method.png)
		- B-mode Imaging
		  ![](/../assets/boiling_histotripsy_b_mode.png)
		- Doppler Imaging
		  ![](/../assets/doppler_imaging_bubble.png)
		- Bubble has to be bigger than speckle to see
		- ![](/../assets/pam_settingup.png)
	- Talk 4: Monitoring of Kidney Stone and DVT Threpies
	  collapsed:: true
		- Twinkling Artifact Improves kidney stone sensitivities
		- PCD with B-mode
		  ![](/../assets/pcd_b_mode.png)
		- ![](/../assets/stable_inertial_cavitation_nanodroplet.png)
		- Combined photoacoustic and B-mode imaging of microbubble mediated sonothrombolysis allows for better monitoring
		- Doppler ultrasound with phase change nanodroplets has been used to evaluate clot boundaries and monitor dissolution
		- Integrated therapy-monitoring systems are being designed and tested to improve cavitation monitoring in DVT
	- Talk 5: Feedback Control Methods on Microbubble-enhanced Ultrasound Therapy
	  collapsed:: true
		- ![](/../assets/why_feedback_microbubble.png)
		  ![](/../assets/feedback_control_challenge.png)
		  ![](/../assets/mainflow_feedback_control.png)
		  ![](/../assets/openloop_control_harmonic.png)
		  ![](/../assets/openloop_control_ultraharmonic.png)
		  ![](/../assets/openloop_control_subharmonic.png)
		  ![](/../assets/openloop_control_subharmonic2.png)
		  ![](/../assets/openloop_control_combine.png)
		- ![](/../assets/closeloop_control_harmonic.png)
		  ![](/../assets/closeloop_control_microbubble.png)
		  ![](/../assets/closeloop_control_pam.png)
		  ![](/../assets/sum_cavitation_control.png)
- Cavitation Thresholds and Dose
	- Talk 1: Cavitation Dosimetry with Passive Acoustic Mapping
	  collapsed:: true
		- ![](/../assets/cav_threshold_relation.png)
	- Talk 2: Intrinsic Threshold Histotripsy: Cavitation Thresholds, Bubble Cloud Dynamics, and Ablation using Single Cycle Histotripsy Pulses
	  collapsed:: true
		- ![](/../assets/cav_threshold_histotripsy.png)
		  ![](/../assets/cav_threshold_water_threshold.png)
		  ![](/../assets/cav_threshold_tissue_threshold.png)
		  ![](/../assets/cav_threshold_cloud_size.png)
		  ![](/../assets/cav_threshold_cloud_density.png)
		  ![](/../assets/cav_threshold_instrinic_threshold_sum.png)
	- Talk 3: Threshold and Cavitation-based Manipulation for Blood-Brain Barrier Opening (BBBO)
	  collapsed:: true
		- ![](/../assets/cav_threshold_subharmonic.png)
	- Talk 4: Thresholds of Thrombolysis and Drug Delivery
	  collapsed:: true
		- ![](/../assets/cav_threshold_predict_inertial.png)
		  ![](/../assets/cav_threshold_predict_stable.png)
		  ![](/../assets/cav_threshold_predict_sum.png)
	- Talk 5: Bubble Cluster Thresholds, Dynamics, and Ablation with Multicycle Histotripsy Modalities
	  collapsed:: true
		- Shock nonlinear waveform produces the bubbles
		  ![](/../assets/cav_threshold_shock_wave.png)
		  ![](/../assets/cav_threshold_tissue_stiffness.png)
		  ![](/../assets/cav_threshold_prf.png)
		  ![](/../assets/cav_threshold_time_to_boiling.png)
		  ![](/../assets/cav_threshold_ablation_hifu.png)
		- Still unknown: threshold in vivo
- Cavitation Agents
	- Talk 1: Pros and Cons of Microbubbles as Cavitation Agents for Therapeutic Ultrasound
	  collapsed:: true
		- ![](/../assets/agent_pro.png)
		  ![](/../assets/agent_con.png)
	- Talk 2: Pros and Cons of Cavitation Agents for Therapeutic Ultrasound
	  collapsed:: true
		- Aiming at drug delivery to brain
		- Requirements:
		  collapsed:: true
			- stable
			- safe
			- convenient
			- extravasable
			- functionalisable
		- Parameters:
		  collapsed:: true
			- Size
			- Coating
			- Core
	- Talk 3: Microbubbles as Cavitation Agents for BBB Opening
	  collapsed:: true
		- Aiming at vascular ultrasound therapeutic
	- Talk 4: SonoTran Particles as Cavitation Agents for Drug Delivery
	  collapsed:: true
		- ![](/../assets/agent_cavitation_characteristic.png)
		  ![](/../assets/agent_tri_function_probe.png)
	- Discussion
	  collapsed:: true
		- Mechanical Index as indicator? better indicator is needed but complicated process
		- report more details in paper about US pulse width, duty and etc. not just pressure and frequency
		- seems still no quantifying methods for magnitude of signal of monitoring
- Clinical Experiences and Regulatory Considerations
	- Talk 1: Detecting, Mapping, and Quantifying Bubble Activity in Therapeutic Ultrasound
	  collapsed:: true
		- closed-loop feedback
		  collapsed:: true
			- MRI
			- Hydrophone
			- US Feedback
			  ![](/../assets/us_feedback.png)
	- Talk 2: Clinical Experience with Histotripsy
	  collapsed:: true
		- Thermal Ablation
	- Talk 3: Clinical Experience from the Engineer / Physicist Viewpoint 
	  collapsed:: true
		- 8 cavitation receivers
		- narrow-band for sub-harmonic
		- 2 broadband for calculation spectral integration
	- Talk 4: Regulatory Consideration for Cavitation Detection in Therapeutic Ultrasound
	  collapsed:: true
		- ![](/../assets/cavitation_methods.png)
		  ![](/../assets/bench_invivo.png)
- Summary and Working Session
	- Stable cavitation should be measured in terms of average energy and inertial cavitation should be calculated with reference to occurrences and amplitude, not averages.
	- James:
		- BBN is what he used to detect inertial cavitation
		- BBN yes, inertial cavitation yes. But BBN no, inertial cavitation unknown, due to the phase calibration of transducer