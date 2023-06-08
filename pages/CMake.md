- References
	- * [An Introduction to Modern CMake · Modern CMake (cliutils.gitlab.io)](https://cliutils.gitlab.io/modern-cmake/)
	- ** [Effective Modern CMake (github.com)](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)
	- ** https://github.com/ttroy50/cmake-examples/tree/master/01-basic
	- *** https://codevion.github.io/#!cpp/cmake.md
- CMake Project Structure
	- ![image.png](../assets/image_1682986516652_0.png){:height 559, :width 478}
- How to set up a library
	- ```CMake
	  # Sources code provided
	  
	  FILE(GLOB SISL_SOURCES "src/*.c")
	  add_library(sisl ${SISL_SOURCES})
	  
	  target_include_directories(sisl PUBLIC
	      include
	  )
	  ```
	- ```CMake
	  # Sources code provided, include and src include together
	  FILE(GLOB SISL_SOURCES "src/*.c" "include/*.h")
	  add_library(sisl ${SISL_SOURCES})
	  ```
	- ```CMake
	  # Static library
	  
	  add_library(sisl SHARED IMPORTED GLOBAL)
	  target_include_directories(sisl INTERFACE
	      include
	  )
	  set_property(TARGET sisl PROPERTY IMPORTED_IMPLIB ${CMAKE_CURRENT_SOURCE_DIR}/lib/sisl.lib)
	  ```
	- On Windows, a .dll and its .lib import library may be imported together:
		- ```CMake
		  add_library(bar SHARED IMPORTED)
		  set_property(TARGET bar PROPERTY
		             IMPORTED_LOCATION "c:/path/to/bar.dll")
		  set_property(TARGET bar PROPERTY
		             IMPORTED_IMPLIB "c:/path/to/bar.lib")
		  add_executable(myexe src1.c src2.c)
		  target_link_libraries(myexe PRIVATE bar)
		  ````
	- Sometimes, the individual static / imported library just can't work. Need to add to a executable project or library
		- ```CMake
		  cmake_minimum_required(VERSION 3.10)
		  
		  project(lite6RobotDemo)
		  
		  add_executable(lite6RobotDemo main.cpp)
		  
		  target_include_directories(lite6RobotDemo PUBLIC
		  	${CMAKE_CURRENT_SOURCE_DIR}/libs/lite6RobotxArmCxxSDK/include
		  )
		  target_link_libraries(lite6RobotDemo PUBLIC
		  	debug ${CMAKE_CURRENT_SOURCE_DIR}/libs/lite6RobotxArmCxxSDK/lib/Debug/xarm.lib
		  	optimized ${CMAKE_CURRENT_SOURCE_DIR}/libs/lite6RobotxArmCxxSDK/lib/Release/xarm.lib
		  )
		  ```
- Move `*.dll` to build exe directory
	- ```CMake
	  # project EMTrackerDemo, library emtrackerlib
	  add_custom_command(TARGET EMTrackerDemo POST_BUILD
	          COMMAND ${CMAKE_COMMAND} -E copy_if_different
	          $<TARGET_FILE:emtrackerlib> $<TARGET_FILE_DIR:EMTrackerDemo>)
	  
	  # emtrackerlib CMakeLists.txt
	  cmake_minimum_required(VERSION 3.10)
	  
	  add_library(emtrackerlib SHARED IMPORTED GLOBAL)
	  
	  target_include_directories(emtrackerlib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include)
	  
	  if(CMAKE_SIZEOF_VOID_P EQUAL 8)
	      set_property(TARGET emtrackerlib PROPERTY IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/ATC3DG64.dll)
	      set_property(TARGET emtrackerlib PROPERTY IMPORTED_IMPLIB ${CMAKE_CURRENT_SOURCE_DIR}/lib/ATC3DG64.lib)
	  else()
	      set_property(TARGET emtrackerlib PROPERTY IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/ATC3DG.dll)
	      set_property(TARGET emtrackerlib PROPERTY IMPORTED_IMPLIB ${CMAKE_CURRENT_SOURCE_DIR}/lib/ATC3DG.lib)
	  endif()
	  ```