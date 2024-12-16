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
		  collapsed:: true
			- `CMakeLists.txt`
			  ```CMake
			  cmake_minimum_required(VERSION 3.8)
			  project(my_cpp_pkg)
			  
			  set(CMAKE_CXX_STANDARD 17)
			  set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
			  
			  if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
			    add_compile_options(-Wall -Wextra -Wpedantic)
			  endif()
			  
			  # find dependencies!!!!
			  find_package(ament_cmake REQUIRED)
			  find_package(rclcpp REQUIRED)
			  find_package(example_interfaces REQUIRED)
			  find_package(std_msgs REQUIRED)
			  find_package(std_srvs REQUIRED)
			  find_package(my_robot_interfaces REQUIRED)
			  
			  if(BUILD_TESTING)
			    find_package(ament_lint_auto REQUIRED)
			    # the following line skips the linter which checks for copyrights
			    # comment the line when a copyright and license is added to all source files
			    set(ament_cmake_copyright_FOUND TRUE)
			    # the following line skips cpplint (only works in a git repo)
			    # comment the line when this package is in a git repo and when
			    # a copyright and license is added to all source files
			    set(ament_cmake_cpplint_FOUND TRUE)
			    ament_lint_auto_find_test_dependencies()
			  endif()
			  
			  # !!!! add node here
			  add_executable(my_cpp_node src/my_first_cpp_node.cpp)
			  ament_target_dependencies(my_cpp_node rclcpp)
			  
			  add_executable(robot_news_station src/robot_news_station.cpp)
			  ament_target_dependencies(robot_news_station rclcpp example_interfaces)
			  
			  # !!! dont forget to install
			  install(TARGETS 
			    my_cpp_node
			    robot_news_station
			    DESTINATION lib/${PROJECT_NAME}
			  )
			  ament_package()
			  
			  ```
			- `package.xml`
			  ```:wxml
			  <?xml version="1.0"?>
			  <?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
			  <package format="3">
			    <name>my_cpp_pkg</name>
			    <version>0.0.0</version>
			    <description>TODO: Package description</description>
			    <maintainer email="kristin@todo.todo">kristin</maintainer>
			    <license>TODO: License declaration</license>
			  
			    <buildtool_depend>ament_cmake</buildtool_depend>
			  
			    // add package dependencies here
			    <depend>rclcpp</depend>
			    <depend>my_robot_interfaces</depend>
			    <depend>example_interfaces</depend>
			    <depend>turtlesim</depend>
			  
			    <test_depend>ament_lint_auto</test_depend>
			    <test_depend>ament_lint_common</test_depend>
			  
			    <export>
			      <build_type>ament_cmake</build_type>
			    </export>
			  </package>
			  
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
		- Create service interface (msg the same)
		  collapsed:: true
			- package tree
				- ```bash
				  ├── CMakeLists.txt
				  ├── package.xml
				  ├── msg
				  │   ├── HardwareStatus.msg
				  │   └── LedStatus.msg
				  └── srv
				      ├── ComputeRectangleArea.srv
				      └── SetLed.srv
				  ```
			- `CMakeLists.txt`
				- ```CMake
				  cmake_minimum_required(VERSION 3.8)
				  project(my_robot_interfaces)
				  
				  if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
				    add_compile_options(-Wall -Wextra -Wpedantic)
				  endif()
				  
				  # find dependencies
				  find_package(ament_cmake REQUIRED)
				  # uncomment the following section in order to fill in
				  # further dependencies manually.
				  # find_package(<dependency> REQUIRED)
				  find_package(rosidl_default_generators REQUIRED) # !!! add this package here
				  
				  
				  if(BUILD_TESTING)
				    find_package(ament_lint_auto REQUIRED)
				    # the following line skips the linter which checks for copyrights
				    # comment the line when a copyright and license is added to all source files
				    set(ament_cmake_copyright_FOUND TRUE)
				    # the following line skips cpplint (only works in a git repo)
				    # comment the line when this package is in a git repo and when
				    # a copyright and license is added to all source files
				    set(ament_cmake_cpplint_FOUND TRUE)
				    ament_lint_auto_find_test_dependencies()
				  endif()
				  
				  # !!! add service here
				  rosidl_generate_interfaces(${PROJECT_NAME}
				    "msg/HardwareStatus.msg"
				    "msg/LedStatus.msg"
				    "srv/ComputeRectangleArea.srv"
				    "srv/SetLed.srv"
				  )
				  # !!! add this line
				  ament_export_dependencies(rosidl_default_runtime)
				  
				  ament_package()
				  
				  ```
				- `package.xml`
				  ```xml
				  <?xml version="1.0"?>
				  <?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
				  <package format="3">
				    <name>my_robot_interfaces</name>
				    <version>0.0.0</version>
				    <description>TODO: Package description</description>
				    <maintainer email="wkx611@outlook.com">kristin</maintainer>
				    <license>TODO: License declaration</license>
				  
				    <buildtool_depend>ament_cmake</buildtool_depend>
				    
				    // !!! add these three packages here
				    <build_depend>rosidl_default_generators</build_depend>
				    <exec_depend>rosidl_default_runtime</exec_depend>
				    <member_of_group>rosidl_interface_packages</member_of_group>
				  
				    <test_depend>ament_lint_auto</test_depend>
				    <test_depend>ament_lint_common</test_depend>
				  
				    <export>
				      <build_type>ament_cmake</build_type>
				    </export>
				  </package>
				  
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