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