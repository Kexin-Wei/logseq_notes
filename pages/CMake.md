- * [An Introduction to Modern CMake · Modern CMake (cliutils.gitlab.io)](https://cliutils.gitlab.io/modern-cmake/)
- ** [Effective Modern CMake (github.com)](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)
- ** https://github.com/ttroy50/cmake-examples/tree/master/01-basic
- CMake Project Structure
	- ![image.png](../assets/image_1682986516652_0.png){:height 559, :width 478}
- How to set up a library
	- ```CMake
	  FILE(GLOB SISL_SOURCES "src/*.c")
	  add_library(sisl ${SISL_SOURCES})
	  
	  target_include_directories(sisl PUBLIC
	      include
	  )
	  ```
	- Or
	  ```CMake
	  FILE(GLOB SISL_SOURCES "src/*.c" "include/*.h")
	  add_library(sisl ${SISL_SOURCES})
	  ```