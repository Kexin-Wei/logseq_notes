- > To set up VS Code with Mingw
  
  main reference: [VS Code GCC instruction](https://code.visualstudio.com/docs/cpp/config-mingw)
# 1.  Mingw Installation
follow the instruction on [MSYS2](https://www.msys2.org/), including:
1. install `msys.exe`
2. using `pacman` command to install `mingw-w64`
3. add path `C:\msys64\mingw64\bin` in windows `Environment Variables`
# 2.  VS Code Extension Installation
- C/C++, by Microsoft. Core component for C++ development.
- C++ Intellisense. For auto completion, errors prompts.
- CMake. For auto completion of CMakeLists.txt
- CMake Tools, by Microsoft. Official configuration tool, to configure, then build to run.