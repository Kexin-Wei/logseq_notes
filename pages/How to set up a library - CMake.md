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
- ```CMake
  # static library
  cmake_minimum_required(VERSION 3.12)
  
  set(CMAKE_CXX_STANDARD 17)
  
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
- Set lib for windows and linux seperately
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
- How to set up #Qt
	- ```CMake
	  cmake_minimum_required(VERSION 3.12)
	  
	  set(CMAKE_CXX_STANDARD 17)
	  
	  set(LIBRARY_TARGET_NAME visualization)
	  
	  set(CMAKE_AUTOUIC ON)
	  set(CMAKE_AUTOMOC ON)
	  set(CMAKE_AUTORCC ON)
	  
	  find_package(Qt5 REQUIRED COMPONENTS Core Widgets Gui)
	  
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
	  
	  target_link_libraries(${LIBRARY_TARGET_NAME} 
	      Qt5::Core
	      Qt5::Widgets
	      Qt5::Gui
	  )
	  ```
- How to set up #VTK
	- ```CMake
	  cmake_minimum_required(VERSION 3.12)
	  
	  set(CMAKE_CXX_STANDARD 17)
	  
	  set(LIBRARY_TARGET_NAME visualization)
	  
	  find_package(VTK COMPONENTS 
	    vtkCommonColor
	    vtkCommonCore
	    vtkCommonDataModel
	    vtkFiltersCore
	    vtkFiltersGeometry
	    vtkFiltersModeling
	    vtkIOImage
	    vtkIOGeometry
	    vtkImagingCore
	    vtkInteractionImage
	    vtkInteractionStyle
	    vtkInteractionWidgets
	    vtkRenderingContextOpenGL2
	    vtkRenderingCore
	    vtkRenderingFreeType
	    vtkRenderingGL2PSOpenGL2
	    vtkRenderingOpenGL2
	  )
	  
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
	  
	  target_link_libraries(${LIBRARY_TARGET_NAME} 
	      ${VTK_LIBRARIES}
	  )
	  ```