- FIR Filter
  $$y[n] = \sum^M_{k=0}b_kx[n-k]$$
	- Order: $M$
	- Length: $L=M+1$
	- FIR system
	  systems for which the impulse response has finite duration
	  impulse response= filter coefficients
	  $h[k]=b_k$
	  $\text{Output}=h[k]*\text{Input}$
	  ->convolution= filter definition
	  ![](/../assets/convolution.png)
- FIR Properties
	- Pro
		- require no feedback of output, simple implementation
		- always stable, if $|x|\le B_x$ ->$|y|\le\sum^N_{k=0}|a_k|B_x$
		- can easily designed to be linear phase by making the coefficient sequence symmetric
	- Con
		- Requires more taps and computational power is required compared to an IIR filter with similar sharpness or selectivity, especially for low frequency cut-offs.
- Design Methods
	- Window design method
	- Frequency sampling method
	- Weighted least squares design
	- Linear programming
	- Parks-McClellan method
	- Equiripple FIR filters design
- Filter Specification
  ![](/../assets/filter_specification.png)
- Window Method
	- Ideal low-pass filters have in nite length of duration.
	- Windowing is truncating the ideal low pass impulse response.
	- Windowed impulse response is not ideal but an approximation
	- There are different types of windows.
	- Ideal Filters
	  collapsed:: true
		- Low-pass filter
		- High-pass filter
		- Band-pass filter
		  ![](/../assets/band_pass.png)
		- Band-stop filter
		- Multi-level Frequency Filter
		- Hilbert Transformer
		  ![](/../assets/hilbert.png){:height 318, :width 487}
		- Differentiator
	- Window Types
		- Rectangular
		  ![](/../assets/rectangular.png){:height 306, :width 486}
		- Bartlett
		- Hann
		- Hamming
		- Blackman
		  ![](/../assets/blackman.png){:height 222, :width 380}
	- Linear Programming Method
	  Linear programming is optimization
		- linear cost function
		- linear constraints