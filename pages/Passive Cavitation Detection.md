- > Goal: Right before treatment, find out the suitable **power**/acoustic pressure
- What is [[Cavitation]]?
- How to Detect Cavitation? 
  Using [[Board Band Noise]](preferred) or [[Hyperechoic Region: scattering by gas or vapor bubbles]]
- Cavitation Detection Methods
  > ((a1ad4214-41f0-4667-b09d-b4d188e55ceb))
	- Indicator of Inertial Cavitation: broadband noise (Root Mean Square)
	  Indicator of Stable Cavitation: subharmonic noise (at half of the fundamental frequency)
- signal processing: raw RF data -> Fourier transform -> spectral analysis -> ?
-
- *Reference 3*
- All sampled waveforms were first transformed to the frequency domain using fast Fourier transform (FFT) routines
- in addition to the nonlinear oscillation of the bubbles, the oscillation of the vessel wall as well as the nonlinearity of the HIFU pulses contributed to the harmonic signals in the frequency domain
- we chose to measure the IC activity by the amount of the broadband noise in a narrow spectral band within a given signal. We chose a frequency window between **3.94 to 4.14 MHz** and calculated the root mean square (RMS) amplitude of the **broadband noise** to minimize the influence of the harmonic peaks (Fig. 4c).
## 2.3.  Synchronization of HIFU and US
*Reference 1*
- the excitation pulse of the 64th element of the imaging probe was used as a **synchronization pulse.**
- The excitation pulse was converted into a transistor-transistor logic (**TTL**)-high pulse, using three pulse generators in series
- The TTL-high pulse was used externally to gate a **frequency generator**
- The passage of the signal from the frequency generator to a **power amplifier** was gated to a specific duration by a computer controlled custom-built relay board.
- This set the HIFU duration to 10 s and synchronized the HIFU exposure with the collection of the cavitation radiofrequency (RF) signal on a digital oscilloscope. The amplified signal was sent to a custom-built electrical matching network (matched to a 50-$\Omega$ load) and then to the HIFU transducer.
# 3.  Harmonic Waves
[ref](https://dsp.stackexchange.com/questions/61908/i-dont-understand-harmonics-why-do-they-happen#:~:text=Harmonics%20%22happen%22%20when%20your%20input,floor%20and%20any%20windowing%20artifacts)
- Harmonics "happen" when your input to an FFT isn't a pure unmodulated sine wave.
- Any unexpected distortion in your input waveform generation (from being exactly identical to mix of sin(wt) + cos(wt)) can be the cause of harmonics appearing in an FFT result (above the noise floor and any windowing artifacts).
- Those harmonics are required to represent the energy of any differences whatsoever between a periodic signal and a perfect sinewave of the same frequency. If harmonics aren't there, then there can't be any differences (assuming a integer periodic input), because a single result bin of an FFT can only represent a pure sinusoid.
  
  *Reference 5*
- Both noninertial and inertial acoustic cavitation events have been shown to generate emissions at subharmonics (f0/ni) and superharmonics (ni f0) of the drive frequency, although it is believed that the violent collapse of inertial cavitation bubbles is the only source of broadband emissions
- As intensity was increased, half harmonic was detected in 0, 60 and 100%, and integrated broadband was detected in 0, 27 and 53% of the exposures in the three regimes.
- Difficulty in detection of broadband emissions may be caused by attenuation of these signals (4 to 12 MHz) in tissue, whereas this is less significant for the half-harmonic emissions.
# 4.  Signal Processing
- Goal: get BBN without harmonic noise
- *Reference 4*
	- First, each signal was **band-pass filtered** in the frequency domain (MATLAB function fir1), with the filter band of **2.3–8.8 MHz**, which corresponds to the sensitive band of the PCD, in order to eliminate the main HIFU harmonic backscattered from the sample as well as high-frequency noise. Since the majority of the focal HIFU waveforms used in this study were significantly nonlinearly distorted, the backscattered harmonics of the HIFU wave dominated the band-pass filtered PCD signal
	- To eliminate the harmonic, ultraharmonic and superharmonic content in the PCD signal, a **notch-shaped comb filter** (notch bandwidth 100 kHz) The bandwidth of 100 kHz is the half-maximum width of the spectral peak at each harmonic, so the comb filter removes the contribution from each harmonic and ultraharmonic.
	  [Harmonic analysis and Fourier Transform](https://terpconnect.umd.edu/~toh/spectrum/HarmonicAnalysis.html)
# 5.  In Vivo vs Ex Vivo
*Reference 4*
the quantitative difference in the cavitation nucleation threshold and cavitation activity metrics between in vivo and ex vivo conditions in the same tissue type has been a subject of long-term debate. Commonly, the cavitation threshold is believed to be **lower** for **ex vivo** tissues, primarily due to the **absence of circulation ex vivo**, and the **presence of higher dissolved gas concentrations** resulting from tissue decomposition, outgassing and potential exposure to air during tissue sample preparation
# 6.  Passive Cavitation Mapping
- # 7.  More in Others Papers
  [[Review of Cavitation Papers]]
# 8.  Reference
1. Hoskins, Peter R., Kevin Martin, and Abigail Thrush, eds. *Diagnostic ultrasound: physics and equipment*. CRC Press, 2019.
2. Rabkin, Brian A., Vesna Zderic, and Shahram Vaezy. "Hyperecho in ultrasound images of HIFU therapy: involvement of cavitation." _Ultrasound in medicine & biology_ 31.7 (2005): 947-956.
3. Chen, Wen-Shiang, et al. "The pulse length-dependence of inertial cavitation dose and hemolysis." _Ultrasound in medicine & biology_ 29.5 (2003): 739-748.
4.  Li, Tong, et al. "Passive cavitation detection during pulsed HIFU exposures of ex vivo tissues and in vivo mouse pancreatic tumors." _Ultrasound in medicine & biology_ 40.7 (2014): 1523-1534.
5. McLaughlan, James, et al. "A study of bubble activity generated in ex vivo tissue by high intensity focused ultrasound." _Ultrasound in medicine & biology_ 36.8 (2010): 1327-1344.
- Reference
	- [[@Diagnostic ultrasound: physics and equipment]]
	  id:: 72dfeeea-9f98-4edd-8b55-0b7584335b21
	- [[@Passive Cavitation Detection during Pulsed HIFU Exposures of Ex Vivo Tissues and In Vivo Mouse Pancreatic Tumors]]
	  id:: a1ad4214-41f0-4667-b09d-b4d188e55ceb
	- [[@Hyperecho in ultrasound images of HIFU therapy: Involvement of cavitation]]
	  id:: 633107ed-bd4e-4493-aed1-1c69926679fc
	- [[@The pulse length-dependence of inertial cavitation dose and hemolysis]]