- {{renderer :tocgen2}}
- # CMake Project
	- CMake Project Structure
		- ![image.png](../assets/image_1682986516652_0.png){:height 559, :width 478}
	- A simple Project CMake
		- ```cmake
		  cmake_minimum_required(VERSION 3.12)
		  
		  set(PROJECT_NAME MyProject)
		  project(${PROJECT_NAME} LANGUAGES CXX)
		  
		  set(CMAKE_CXX_STANDARD 17)
		  set(CMAKE_CXX_STANDARD_REQUIRED ON)
		  set(CMAKE_AUTOMOC ON) # if use qt
		  
		  # path in system package
		  find_package(Qt6 REQUIRED COMPONENTS 
		      Core
		      Widgets
		  )
		  
		  # unknown path package
		  set(spdlog_DIR "${CMAKE_SOURCE_DIR}/lib/spdlog/lib/cmake/spdlog")
		  find_package(spdlog REQUIRED)
		  
		  # add source files
		  file(GLOB_RECURSE ${PROJECT_NAME}_SRC "src/*.cpp" "src/*.cxx" "src/*.c")
		  file(GLOB_RECURSE ${PROJECT_NAME}_HEADERS "include/*.h" "include/*.hpp")
		  
		  add_executable(${PROJECT_NAME} main.cpp
		      ${${PROJECT_NAME}_SRC}
		      ${${PROJECT_NAME}_HEADERS}
		  )
		  
		  target_link_libraries(${PROJECT_NAME} PRIVATE
		      Qt6::Core
		      Qt6::Widgets
		      spdlog::spdlog
		  )
		  
		  # to use <> to include
		  target_include_directories(${PROJECT_NAME} PRIVATE
		      ${CMAKE_SOURCE_DIR}/lib/spdlog/include
		      ${CMAKE_SOURCE_DIR}/include
		  )
		  ```
- # CMake Library
	- [[CMake: How to set up Qt]]
	- [[CMake: How to set up VTK]]
	- Sources code provided
	  collapsed:: true
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
	- Static Library
	  collapsed:: true
		- ```CMake
		  # Static library
		  
		  add_library(sisl SHARED IMPORTED GLOBAL)
		  target_include_directories(sisl INTERFACE
		      include
		  )
		  set_property(TARGET sisl PROPERTY IMPORTED_IMPLIB ${CMAKE_CURRENT_SOURCE_DIR}/lib/sisl.lib)
		  ```
		- ```CMake
		  # static library
		  
		  set(LIBRARY_TARGET_NAME qvtk)
		  set(${LIBRARY_TARGET_NAME}_HDR
		  )
		  set(${LIBRARY_TARGET_NAME}_SRC
		  )
		  
		  add_library(${LIBRARY_TARGET_NAME} STATIC ${${LIBRARY_TARGET_NAME}_HDR} ${${LIBRARY_TARGET_NAME}_SRC})
		  
		  set_target_properties(${LIBRARY_TARGET_NAME} PROPERTIES
		      PUBLIC_HEADER "${${LIBRARY_TARGET_NAME}_HDR}"
		  )
		  target_include_directories(${LIBRARY_TARGET_NAME} PUBLIC 
		  "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
		  )
		  
		  target_link_libraries(${LIBRARY_TARGET_NAME} PUBLIC 
		  
		  )
		  ```
	- Special Cases
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
		- Set lib for windows and linux separately
			- ```CMake
			  cmake_minimum_required(VERSION 3.10)
			  
			  add_library(xarm SHARED IMPORTED GLOBAL)
			  
			  target_include_directories(xarm INTERFACE
			      ${CMAKE_CURRENT_SOURCE_DIR}/include
			  )
			  
			  # set lib for windows and linux
			  if(WIN32)
			      set_target_properties(xarm PROPERTIES
			          IMPORTED_LOCATION_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/lib/Debug/xarm.dll
			          IMPORTED_LOCATION_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/lib/Release/xarm.dll
			      )
			  elseif(UNIX)
			      set_target_properties(xarm PROPERTIES
			          IMPORTED_LOCATION_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/lib/Debug/libxarm.so
			          IMPORTED_LOCATION_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/lib/Release/libxarm.so
			      )
			  endif()
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
- # CMake Rare Cases
	- [[_declspec(dllexport) and _declspec(dllimport)]]
- # Tool
	- [cpm-cmake/CPM.cmake: 📦 CMake's missing package manager. A small CMake script for setup-free, cross-platform, reproducible dependency management. (github.com)](https://github.com/cpm-cmake/CPM.cmake)
- References
  collapsed:: true
	- * [An Introduction to Modern CMake · Modern CMake (cliutils.gitlab.io)](https://cliutils.gitlab.io/modern-cmake/)
	- ** [Effective Modern CMake (github.com)](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)
	- ** https://github.com/ttroy50/cmake-examples/tree/master/01-basic
	- *** https://codevion.github.io/#!cpp/cmake.md