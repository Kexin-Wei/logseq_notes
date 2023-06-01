- What is Ultrasound Beam?
  [[@Diagnostic ultrasound: physics and equipment]]
  ![](/../assets/beamforming.png){:height 355, :width 306}
	- When a source generates a sound wave, the way in which the **wave spreads out** as it moves away from the source is determined by the relationship between the **width of the source** (the **aperture**) and the **wavelength** of the wave.
	- If the **aperture** is **smaller** than the **wavelength**, the wave spreads out as it travels (**diverges**), an effect known as **diffraction**
		- This is rather like the wave on the pond, spreading out from the point of entry of a small stone
	- If the **width** of the source is much **greater** than the **wavelength** of the wave, the waves are relatively **flat** (plane) rather than curved and lie **parallel** to the surface of the source
		- Such waves travel in a direction perpendicular to the surface of the source with relatively little sideways spread, i.e. in the form of a parallel-sided beam
	- The curved waves from each propagate outwards and the parts of the curve which are parallel to the surface of the source align to form plane waves. The other, **non-parallel** parts of the curved waves tend to interfere destructively and **cancel out**.
- Scan the Area by Scan Line
	- Source 1
		- ![](/../assets/active_group.png){:height 226, :width 547}
		- each element is usually further ‘sub-diced’ into two or three even narrower elements
		- In order to interrogate a particular scan line, an ‘active group’ of adjacent transducer elements, centred on the required scan line, is used.
		- First, a pulse is transmitted, using say the central 20 elements of the group. This pulse travels along the transmit beam, centred on the scan line. As soon as the pulse has been **transmitted**, elements in a different combination, still centred on the scan line, act together as a **receiving transducer**, defining the receive beam. The number of elements used for **reception** is initially **less** than that used for **transmission**
		- Once all echoes have been received from one scan line, a new active group of elements, centred on the next scan line, is activated
	- [Source 2](https://www.ob-ultrasound.net/somers.html)
		- In order to overcome this, adjacent elements typically 8 to 16 (more in wide-aperture designs), are pulsed simultaneously.
		- In the subgroup of X elements, pulsing of the inner elements is delayed with respect to the outer elements. A focused beam results from the interference of the X small divergent wavelets. The time delays determines the depth of focus for the transmitted beam and can be changed during scanning.
		- The same delay factors are also applied to the X elements during the receiving phase resulting in a dynamic focusing effect on return. In this manner, a single scan line in the real-time image is formed.
		- To generate the next adjacent scan line, another group of X elements is formed by shifting one element position along the transducer array from the previous group. The same pattern is then repeated for this set of X elements and all other sets along the array, in a sequential and repetitive manner.
- Maximal Amplitude at Focus
  ![](/../assets/focus_max_amplitude.png)
- Dynamic Focusing
  ![](/../assets/dynamic_focus.png)
- Grating lobes
  ![](/../assets/grating_lobe.png)
	- Grating lobes can occur with any transducer having regularly spaced elements, such as a **linear** or **curvilinear** array or a phased array (discussed later).
	- In all cases, the **greater the angle** at which a grating lobe occurs, the **weaker** it will be, since each element is less efficient at transmitting or receiving sound waves in directions at large angles to the straight ahead direction.
- Saving Time in Array Transducer
	- Temporal resolution
	- Size of the field of view
	- Image quality (e.g. lateral resolution, contrast resolution, dynamic range)
		- a **reduction in frame rate** occurs if the maximum depth is increased (more time per scan line) or the width of the field of view is increased (more scan lines).
		- Multiple-zone transmit focusing improves the range of depths over which good lateral resolution can be achieved, but this is at the expense of temporal resolution because of the need to remain longer on each scan line while interrogating several zones instead of just one.
		- **Compound scanning** improves image quality through reduced speckle and acoustic noise and by better boundary delineation, but reduces temporal resolution.
- Some Interesting Facts
	- At **greater depths**, the beam becomes **wider**, and **lateral resolution** becomes noticeably **worse**.
	- ultrasound **beams** have **finite width** due to **diffraction** effects and the ultrasound pulse must have **finite duration** in order to define the transmit **frequency**. #📑READ
	- Unfortunately, the **greater** the number of **focal zones**, the longer is spent on each scan line, and so the lower the frame rate.
	- Phased-array scanning systems (discussed next) are particularly well suited to **sector scanning**, but **strongly convex curvilinear** arrays allow manufacturers of linear-array systems to offer **sector** scanning transducers, without having to build in the specialized electronics that phased-array transducers require.
	- The **maximum useful size** of the active element group of a **curvilinear** array is more **limited** than in a **linear** array employing the same-sized elements.
	- However, compared to a linear array, the **phased-array** transducer array is **much shorter** in the scan plane direction, with an **overall aperture** of typically **30** **wavelengths** square.