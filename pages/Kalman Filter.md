- Classic Kalman Filter
	- ![Kalman Filter](Kalman_Filter.pdf)
	- [轻松理解卡尔曼滤波 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/444977764)
	- ![](/../assets/kalman_filter.png)
	- Fundamental
		- [alpha - beta - gamma filter](https://www.kalmanfilter.net/alphabeta.html)
		- [1d](https://www.kalmanfilter.net/kalman1d.html)
		- [2d, acceleration as input](https://machinelearningspace.com/2d-object-tracking-using-kalman-filter/)
		- [2d, acceleration as state](https://www.kalmanfilter.net/multiExamples.html)
		- [Equation Overview](https://www.kalmanfilter.net/multiSummary.html)
	- Derivation
		- [COVARIANCE EXTRAPOLATION EQUATION](https://www.kalmanfilter.net/covextrap.html)
		- [THE KALMAN GAIN](https://www.kalmanfilter.net/kalmanGain.html)
		- [SIMPLIFIED COVARIANCE UPDATE EQUATION](https://www.kalmanfilter.net/simpCovUpdate.html)
- ![Nonlinear Kalman Filter](Nonlinear_Kalman_Filter.pdf)
	- Extended Kalman Filter
		- ![](/../assets/kalman_filter_extended.png){:height 467, :width 427}
		- linearization at the specific point
		  $F = \frac{\partial f}{\partial x} | _{x_{k,k-1},u_k}$
		  $H = \frac{\partial h}{\partial x}|_{x_{k,k-1}}$
	- [Unscented Kalman Filter]( https://gregorygundersen.com/blog/2020/11/19/unscented-transform/)
		- ![](/../assets/kalman_filter_ekf_ukf.png)
		- ![](/../assets/kalman_filter_unscented.png)
- Multi Sensor Fusion
	- [一文理清卡尔曼滤波，从传感器数据融合开始谈起 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/158737818)