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
		  ```