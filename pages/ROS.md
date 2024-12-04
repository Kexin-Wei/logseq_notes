- Node: every program / threading
- Topic & message: how nodes communicate with each other
- Services: one time function
- Ros remap node name from `launch`
	- ![image.png](../assets/image_1686260428021_0.png)
- Package
	- ![image.png](../assets/image_1686260792774_0.png){:height 201, :width 381}
	- dependence
	  ![image.png](../assets/image_1686260853143_0.png)
- Workspace
	- ![image.png](../assets/image_1686261313552_0.png)
- [Quality of Service QoS](https://docs.ros.org/en/foxy/Concepts/About-Quality-of-Service-Settings.html)
- Add source in Ubuntu `.bashrc`
  ```bash
  # ros jazzy evn set up
  source /opt/ros/jazzy/setup.bash # ros command
  source /usr/share/colcon_cd/function/colcon_cd-argcomplete.bash #colcon autocomplete
  source ~/ros2_ws/install/setup.bash # workspace command
  ```
- File structure
	- WS
		- src
			- my_package
				- package.xml
- create c++ or python package
  ```bash
  ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
  ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
  ```
-