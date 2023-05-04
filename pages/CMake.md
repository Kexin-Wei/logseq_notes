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