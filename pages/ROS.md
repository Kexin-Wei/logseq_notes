# Environment set up
	- Add source in Ubuntu `.bashrc`
	  ```bash
	  # ros jazzy evn set up
	  source /opt/ros/jazzy/setup.bash # ros command
	  source /usr/share/colcon_cd/function/colcon_cd-argcomplete.bash #colcon autocomplete
	  source ~/ros2_ws/install/setup.bash # workspace command
	  ```
- # ROS Concepts
	- ## Workspace
		- ![image.png](../assets/image_1686261313552_0.png)
		- [Quality of Service QoS](https://docs.ros.org/en/foxy/Concepts/About-Quality-of-Service-Settings.html)
		- File structure
			- WS
				- src
					- my_package
						- package.xml
	- ## Package
		- ![image.png](../assets/image_1686260792774_0.png){:height 201, :width 381}
		- dependence
		  ![image.png](../assets/image_1686260853143_0.png)
		- create c++ or python package
		  ```bash
		  ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
		  ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
		  
		  colcon build --packages-select A_PACKAGE --symlink-install
		  ```
		- Python package setup
		  collapsed:: true
			- `setup.py`
			  ```python
			  from setuptools import find_packages, setup
			  
			  package_name = "my_py_pkg"
			  
			  setup(
			      name=package_name,
			      version="0.0.0",
			      packages=find_packages(exclude=["test"]),
			      data_files=[
			          ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
			          ("share/" + package_name, ["package.xml"]),
			      ],
			      install_requires=["setuptools"],
			      zip_safe=True,
			      maintainer="kristin",
			      maintainer_email="kristin@todo.todo",
			      description="TODO: Package description",
			      license="TODO: License declaration",
			      tests_require=["pytest"],
			      entry_points={
			          "console_scripts": [ # editing here to add node
			              "my_node = my_py_pkg.my_first_py_node:main",
			              "robot_news_station = my_py_pkg.robot_news_station:main",
			              "a_listener = my_py_pkg.a_listener:main",
			              "number_publisher = my_py_pkg.number_publisher:main",
			              "add_two_ints_server = my_py_pkg.add_two_ints_server:main",
			              "add_two_ints_client_no_oop = my_py_pkg.add_two_ints_client_no_oop:main",
			              "add_two_ints_client = my_py_pkg.add_two_ints_client:main",
			              "hardware_status_publisher = my_py_pkg.hardware_status_publisher:main",
			              "battery_node = my_py_pkg.battery_node:main",
			          ],
			      },
			  )
			  ```
			- `package.xml`
			  ```xml
			  <?xml version="1.0"?>
			  <?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
			  <package format="3">
			    <name>my_py_pkg</name>
			    <version>0.0.0</version>
			    <description>TODO: Package description</description>
			    <maintainer email="kristin@todo.todo">kristin</maintainer>
			    <license>TODO: License declaration</license>
			  
			    // add dependency here for the packages
			    <depend>rclpy</depend>
			    <depend>example_interfaces</depend>
			    <depend>std_msgs</depend>
			    <depend>my_robot_interfaces</depend>
			  
			    <test_depend>ament_copyright</test_depend>
			    <test_depend>ament_flake8</test_depend>
			    <test_depend>ament_pep257</test_depend>
			    <test_depend>python3-pytest</test_depend>
			  
			    <export>
			      <build_type>ament_python</build_type>
			    </export>
			  </package>
			  
			  ```
		- Cpp package setup
			- `CMakeLists.txt`
			  ```CMake
			  ```
	- ## Node
		- every program / threading
		- ```bash
		  # rename a node
		  ros2 run A_PACKAGE A_NODE -r __node:=A_NEW_NAME
		  ros2 node list
		  ros2 node info /A_NODE
		  ```
	- ## Topic
		- & message: how nodes communicate with each other
		- ```bash
		  # topic
		  ros2 topic list
		  ros2 topic info /A_TOPIC
		  ros2 topic hz /A_TOPIC # frequency
		  ros2 topic bw /A_TOPIC # bandwidth
		  
		  # publish directly
		  ros2 topic pub -r 10 /robot_news example_interfaces/msg/String "{data: 'hello from termina'}"
		  
		  # rename a topic
		  ros2 run my_cpp_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=my_news
		  ```
	- ## Services
		- one time function
		- ```bash
		  # service
		  ros2 service list
		  ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts  "{a: 2,b: 4}"
		  ```
	- ## Interface
		- ```bash
		  # interface
		  ros2 show interface show example_interfaces/msg/String
		  ros2 interface show geometry_msgs/msg/Twist
		  ros2 interface package service_msgs
		  ```
	- ## Parameter
		- ```bash
		  # parameter
		  ros2 param get /A_NODE PARAMETER
		  ros2 param set /A_NODE PARAMETER VALUE
		  ```
- # [[ROS & Docker]]
- # ROS in Raspberry Pi
	- [ROS 2 on Raspberry Pi — ROS 2 Documentation: Jazzy documentation](http://docs.ros.org/en/jazzy/How-To-Guides/Installing-on-Raspberry-Pi.html)
- # Tips
	- Ros remap node name from `launch`
		- ![image.png](../assets/image_1686260428021_0.png)