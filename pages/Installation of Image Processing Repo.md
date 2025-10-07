- [GitRepo - ImageProcessingOpenCV](https://github.com/Kexin-Wei/ImageProcessingOpenCV)
- Follow the `README.md` in Git Repo
- In a docker way
  id:: 641be390-ce93-48f0-80fc-ccc2546e712b
	- **Create a Dockerfile**: Create a new directory for your project, and inside that directory, create a `Dockerfile` with the following content, which sets up a Docker image based on Ubuntu 20.04, installs the required packages, and builds OpenCV from source.
		- ```bash
		  # Use the official Ubuntu image as the base
		  FROM ubuntu:20.04
		  
		  # Set environment variables to avoid interactive prompts during package installation
		  ENV DEBIAN_FRONTEND=noninteractive
		  
		  # Update the package index and install required packages
		  RUN apt-get update && apt-get install -y \
		      build-essential \
		      cmake \
		      git \
		      libgtk2.0-dev \
		      pkg-config \
		      libavcodec-dev \
		      libavformat-dev \
		      libswscale-dev \
		      python3-dev \
		      python3-numpy \
		      libtbb2 \
		      libtbb-dev \
		      libjpeg-dev \
		      libpng-dev \
		      libtiff-dev \
		      libdc1394-22-dev
		  
		  # Download and build OpenCV
		  RUN cd ~ && \
		      git clone https://github.com/opencv/opencv.git && \
		      git clone https://github.com/opencv/opencv_contrib.git && \
		      cd opencv && \
		      mkdir build && \
		      cd build && \
		      cmake -D CMAKE_BUILD_TYPE=Release \
		            -D CMAKE_INSTALL_PREFIX=/usr/local \
		            -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
		            .. && \
		      make -j$(nproc) && \
		      make install && \
		      ldconfig
		  
		  # Set the default command to run a Bash shell
		  CMD ["bash"]
		  ```
	- **Build the Docker image**: In the terminal, navigate to the directory containing the Dockerfile and build the Docker image using the following command: `docker build -t ubuntu-20-opencv .`
	- **Run the Docker container**: Run the Docker container using the following command: `docker run -it --rm ubuntu-20-opencv`
	- Mount local directory to docker container: `docker run -it --name c11 -v /Users/yourusername/GitRepos/ImageProcessingOpenCV/:/gitrepo vac611/ubuntu-20-opencv`
		- in winodws, you need to use `docker run -it -v "D:/GitRepos/MotionTrackingOpenCV":/gitrepo vac611/ubuntu-20-opencv:v1.1-pycv` #windows
	- Add opencv python linkage (rebuild opencv) and update image: the default python package path is somehow wrong and we need to modify it by using `PYTHON3_PACKAGES_PATH=/usr/lib/python3.8/dist-packages` in [this post](https://rodosingh.medium.com/using-cmake-to-build-and-install-opencv-for-python-and-c-in-ubuntu-20-04-6c5881eebd9a)