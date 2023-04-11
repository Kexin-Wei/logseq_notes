- **Transducer -> Beam Former -> Amplitude & Phase Processing -> Post Processing -> B-mode**
  id:: 6359efc4-02d5-4887-a129-800795009926
  ![](/../assets/b_mode_imaging.png) ((635b4a38-dc08-4825-aee7-625d2a080c90))
	- Beam Forming #📑READ
	  id:: 634c0062-08a4-47e0-926c-06bc716743c4
		- ![](/../assets/us_b-mode_before_beamforming.jpg) ((635b4a5d-0536-4dcc-9fcd-72ac672e7f27))
	- Filtering
		- band-pass filtering to **reduce noise outside frequencies of interest**.
		- to select whether **imaging** is done on the **fundamental frequency** (conventional imaging) or the **second harmonic** (harmonic imaging)
	- ## Amplitude Processing
	  > Related to [Envelope Detection](((635b45a5-ef74-446f-bfe9-eaa0d1310280)))
		- Amplitude Detection or Envelope Extraction Process
			- Demodulation: Get a complex signal
				- via **Hilbert transform**
					- Pro:
						- independent of the actual frequency of the operating frequencies
						- independent of the imaging mode (either conventional versus harmonic)
						- independent of changes in the center frequencies with time (e.g., a physical phenomenon in the tissue that results in a change of frequency with the depth of penetration).
					- Con: this operation is more complex compared to the alternative below
				- via **complex rotator** in baseband followed by **low pass filtering to eliminate sidelobes.**
					- Pro: simpler
					- Con: the operating center frequency needs to be known and possibly tracked for changes.
			- Get magnitude of the complex signal, may imply additional **low pass filtering** with decimation or interpolation.
	- ## Post Processing
		- ![](/../assets/us_b-mode_processing_2.png)
		  [[@Diagnostic Radiology Physics: A Handbook for Teachers and Students]]
			- Logarithmic Compression + Scan Conversion
		- Log Compression
			- The maximum dynamic range of the human eye is in the order of **30 dB**. The actual dynamic range of the received signal depends on the **ADC** bits, the **TGC amplifier** used in the front end, and the **depth of penetration**. The signal is compressed to fit the dynamic range used for display (usually **7 or 8 bits**). It is typical to use a log compressor to achieve the desired dynamic range for display. Some parameters in the compression function can be used to adjust brightness.
- Reference
	- [3]
	  id:: 635b4a38-dc08-4825-aee7-625d2a080c90
	  [[@Real-Time Ultrasound Attenuation Imaging of Diffuse Fatty Liver Disease]]
	- [4]
	  id:: 635b4a5d-0536-4dcc-9fcd-72ac672e7f27
	  [[@An IEEE single-precision arithmetic based beamformer architecture for phased array ultrasound imaging system]]