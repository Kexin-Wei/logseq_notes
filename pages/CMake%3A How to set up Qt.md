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