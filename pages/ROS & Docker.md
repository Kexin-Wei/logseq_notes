- [Setup ROS 2 with VSCode and Docker [community-contributed] — ROS 2 Documentation: Jazzy documentation](http://docs.ros.org/en/jazzy/How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container.html)
- Install docker
	- ```bash
	  sudo apt install docker.io git python3-pip
	  # either
	  pip3 install vcstool
	  # or
	  sudo apt install python3-vcstool
	  
	  echo export PATH=$HOME/.local/bin:$PATH >> ~/.bashrc
	  source ~/.bashrc
	  sudo groupadd docker
	  sudo usermod -aG docker $USER
	  newgrp docker
	  ```
	- check docker `docker run hello-world`
	- start docker service `sudo systemctl start docker`
- Configure workspace
	- ```bash
	  cd ~/
	  mkdir ros2_ws
	  cd ros2_ws
	  mkdir src
	  ```
	- create `.devcontainer` folder with two files, `devcontainer.json` and `Dockerfile`
		- ```
		  ws
		  ├── .devcontainer
		  │   ├── devcontainer.json
		  │   └── Dockerfile
		  ├── src
		      ├── package1
		      └── package2
		  ```
		- ```json
		  // devcontainer.json
		  {
		      "name": "ROS 2 Development Container",
		      "privileged": true,
		      "remoteUser": "YOUR_USERNAME",
		      "build": {
		          "dockerfile": "Dockerfile",
		          "args": {
		              "USERNAME": "YOUR_USERNAME"
		          }
		      },
		      "workspaceFolder": "/home/ws",
		      "workspaceMount": "source=${localWorkspaceFolder},target=/home/ws,type=bind",
		      "customizations": {
		          "vscode": {
		              "extensions":[
		                  "ms-vscode.cpptools",
		                  "ms-vscode.cpptools-themes",
		                  "twxs.cmake",
		                  "donjayamanne.python-extension-pack",
		                  "eamodio.gitlens",
		                  "ms-iot.vscode-ros"
		              ]
		          }
		      },
		      "containerEnv": {
		          "DISPLAY": "unix:0",
		          "ROS_AUTOMATIC_DISCOVERY_RANGE": "LOCALHOST",
		          "ROS_DOMAIN_ID": "42"
		      },
		      "runArgs": [
		          "--net=host",
		          "--pid=host",
		          "--ipc=host",
		          "-e", "DISPLAY=${env:DISPLAY}"
		      ],
		      "mounts": [
		         "source=/tmp/.X11-unix,target=/tmp/.X11-unix,type=bind,consistency=cached",
		         "source=/dev/dri,target=/dev/dri,type=bind,consistency=cached"
		      ],
		      "postCreateCommand": "sudo rosdep update && sudo rosdep install --from-paths src --ignore-src -y && sudo chown -R $(whoami) /home/ws/"
		  }
		  ```
		- ```Dockerfile
		  FROM ros:ROS_DISTRO
		  ARG USERNAME=USERNAME
		  ARG USER_UID=1000
		  ARG USER_GID=$USER_UID
		  
		  # Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
		  RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi
		  
		  # Create the user
		  RUN groupadd --gid $USER_GID $USERNAME \
		      && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
		      #
		      # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
		      && apt-get update \
		      && apt-get install -y sudo \
		      && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
		      && chmod 0440 /etc/sudoers.d/$USERNAME
		  RUN apt-get update && apt-get upgrade -y
		  RUN apt-get install -y python3-pip
		  ENV SHELL /bin/bash
		  
		  # ********************************************************
		  # * Anything else you want to do like clean up goes here *
		  # ********************************************************
		  
		  # [Optional] Set the default user. Omit if you want to keep the default as root.
		  USER $USERNAME
		  CMD ["/bin/bash"]
		  ```