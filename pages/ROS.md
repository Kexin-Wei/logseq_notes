# Install
	- follow the document of the corresponding version
	- install colcon
		- ```bash
		  sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
		  curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
		  sudo apt update
		  sudo apt install python3-colcon-common-extensions
		  ```
	- install gazebo
		- ```bash
		  sudo apt install ros-humble-gazebo* # humble only, Jazzy look online
		  ```
	- Multiple version ROS
		- ![image.png](../assets/image_1737189364274_0.png)
- # Environment set up
	- Add source in Ubuntu `.bashrc`
	  ```bash
	  # ros2
	  source /opt/ros/humble/setup.bash
	  source /usr/share/colcon_cd/function/colcon_cd-argcomplete.bash
	  source ~/ros2_ws/install/setup.bash
	  
	  # gazebo
	  source /usr/share/gazebo/setup.bash
	  
	  # nav2
	  export TURTLEBOT3_MODEL=waffle
	  export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp # a fix
	  ```
- # [[ROS Concepts]]
- # [[ROS Visualization]]
- # [[ROS & Docker]]
- # [[ROS2 & Navigation 2]]
- # ROS2 & Moveit2
	- [Installation Tutorial for Humble](https://moveit.picknik.ai/humble/doc/tutorials/getting_started/getting_started.html#)
	- https://moveit.picknik.ai/humble/doc/tutorials/tutorials.html
- # ROS in Raspberry Pi
	- [ROS 2 on Raspberry Pi — ROS 2 Documentation: Jazzy documentation](http://docs.ros.org/en/jazzy/How-To-Guides/Installing-on-Raspberry-Pi.html)
- # Tips
	- Ros remap node name from `launch`
		- ![image.png](../assets/image_1686260428021_0.png)