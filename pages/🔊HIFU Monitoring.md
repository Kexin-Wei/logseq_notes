- Knowledge Base
	- [[Passive Cavitation Detection]]
	- [[@Broadband Ultrasonic Attenuation Estimation and Compensation With Passive Acoustic Mapping]]
		- ((633a4dc3-17bc-404b-ab2d-cb9d1fe69900))
		- ((633a528c-3662-4860-b72f-7caba3c2e0e7))
		- Too hard to understand, need to read PAM Passive Acoustic Mapping first #📑READ
		- PAM algorithms:
			- time exposure acoustics (TEA)
			- robust Capon beamforming (RCB)
		- Array Characterization (Wire scattering filed)
			- Hydrophone $p_\text{hyd}(f, x, z)$ : average 400 times at each scan point on oscilloscope to decrease SNR
			  		1. third order 200 kHz high pass Butterworth filter to remove low frequency noise
			  		2. 20% Tukey Window
			  		3. Fourier Transform $X(f,x,z)$
			  		4. correction for sensitivity, directivity, and preamp gain $G_\text{pre}(f)$ according to
			  	$p_\text{hyd}( f, x, z)=B( f, z)X( f, x, z)/[M_\text{hyd}( f, x, z)G_\text{pre}( f )]$
			  	hydrophone sensitivity $M_\text{hyd}( f, x, z)=M_\text{hyd}( f, \theta)$
			- Array element calibrations $H_{\text{cal}, j} ( f, 0, z)$ <-raw array voltage signals $V_j ( f, 0, z)$
			  		1. third order 200 kHz high pass Butterworth filter to remove low frequency noise
			  		2. 20% Tukey Window
			  		3. $H_{\text{cal}, j} ( f, 0, z) = V_j ( f, 0, z)/p_\text{hyd}( f, x, z)$
		- Cavitation Experiment
		  	1. 20% Tukey window to time domain $v_j(t)$
		  	2. Fourier Transform of windowed array data $[V_j(f)]$
		  	3. Use $H_{\text{cal}, j} ( f, 0, z)$ to get calibrated array response $p_{a, j} ( f ) = V_j ( f )/H_{\text{cal}, j} ( f, \textbf{r}_s )$
	- [[Bubble Activity in Therapeutic Ultrasound Live Workshop]]
- [[Treatment Monitoring]]
- [[Attenuation Assessment]]
- TPU Nonlinear Effect
- Power + Depth -> Thermal Effect: Summarize the animal old data rules