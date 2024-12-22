# Environment set up
	- Add source in Ubuntu `.bashrc`
	  ```bash
	  # ros jazzy evn set up
	  source /opt/ros/jazzy/setup.bash # ros command
	  source /usr/share/colcon_cd/function/colcon_cd-argcomplete.bash #colcon autocomplete
	  source ~/ros2_ws/install/setup.bash # workspace command
	  ```
- # [[ROS Concepts]]
- # ROS Visualization
	- run urdf demo
		- ```bash
		  ros2 launch urdf_tutorial display.launch.py model:=/opt/ros/jazzy/share/urdf_tutorial/urdf/08-macroed.urdf.xacro 
		  ```
		- Models, TFs
	- visualize TFs
		- ```bash
		  # install package
		  sudo apt install ros-jazzy-tf2-tools
		  
		  # run when demo running
		  ros2 run tf2_tools view_frames # generate frams.gv and pdf in current diretory
		  ```
	- ```bash
	  ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro a_car.urdf)"
	  ros2 run joint_state_publisher_gui joint_state_publisher_gui
	  ```
- # [[ROS & Docker]]
- # ROS in Raspberry Pi
	- [ROS 2 on Raspberry Pi — ROS 2 Documentation: Jazzy documentation](http://docs.ros.org/en/jazzy/How-To-Guides/Installing-on-Raspberry-Pi.html)
- # Tips
	- Ros remap node name from `launch`
		- ![image.png](../assets/image_1686260428021_0.png)