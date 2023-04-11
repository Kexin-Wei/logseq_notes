- Translation  (3 unknowns)
  collapsed:: true
	- $$T_{translation} = \vec v$$
- Rigid transformation = translation + rotation (6 unknowns)
  collapsed:: true
	- $$T_{rigid}(\mathbf{v}) = R\mathbf{v} + t = \begin{bmatrix}R & t\\ \mathbf{0}^T& 1\end{bmatrix}$$
- Scaling transformation = translation + rotation + scale (9 unknowns)
  collapsed:: true
	- $$S_{scale} = \text{diag}(s_x, s_y, s_z, 1)$$
	  $$T = S_{scale}T_{rigid}$$
- Affine transformation = translation + rotation + scale + shear (15 unknowns)
  collapsed:: true
	- $$S_{shear} = Sh_x Sh_ySh_z$$
	  $$Sh_x = \begin{bmatrix} 1 & s_{x,y} & s_{x,z} & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}$$
	  $$Sh_y=\begin{bmatrix}1 & 0 & 0 & 0 \\s_{y,x} & 1 & s_{y,z} & 0 \\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{bmatrix}$$
	  $$Sh_z = \begin{bmatrix}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ s_{z,x} & s_{z,y} & 1 & 0\\0 & 0 & 0 & 1\end{bmatrix}$$
	  $$T=S_{shear}S_{scale}T_{rigid}$$
- Deformation
  collapsed:: true
	- [[Image Non-Rigid Registration]]