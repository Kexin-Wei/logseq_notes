- [2.2. Degrees of Freedom of a Robot](https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-2-degrees-of-freedom-of-a-robot/#:~:text=Grubler's%20formula%20tells%20us%2C%203,because%20there's%20a%20closed%20loop.)
- ![image.png](../assets/image_1689402357721_0.png){:height 186, :width 355}
	- m = 3 for 2D, m=6 for 3D
	- N: no of links
	- J: no of joints
	- IMPORTANT: independent joints
- Example
	- ![Application-2: Schematic of a two-DOF robotic arm in 2D space | Download  Scientific Diagram](https://www.researchgate.net/publication/322412560/figure/fig1/AS:668978112385031@1536508219685/Application-2-Schematic-of-a-two-DOF-robotic-arm-in-2D-space.jpg){:height 297, :width 363}
	  id:: 64b23f3a-e979-4877-9518-a7db8c8c7e11
		- DoFs = 3*(3-1-2)+2 = 2
	- ![image.png](../assets/image_1689405251183_0.png)
- Solution of complex robot system
	- ![AppendixACalculationoftheNumberofDegreesofFreedomofRobotswithClosedChains.pdf](../assets/AppendixACalculationoftheNumberofDegreesofFreedomofRobotswithClosedChains_1689403149849_0.pdf)
	- For the robot above, this applies
		- ![image.png](../assets/image_1689403695069_0.png){:height 417, :width 429}
	- DoFs = 9 - 3*3+3 = 3 -> 3 motors can control it
	  collapsed:: true
		- Leg 1: Tz, Rx, Ry
		- Leg 2: Tz, Rx, Ry
		- Leg 3: Tz, Ry, Rx