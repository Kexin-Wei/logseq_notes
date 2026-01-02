- #Concepts
	- Docker Images and Docker Containers
		- ![image.png](../assets/image_1679013741651_0.png)
	- Bridge ( or Network ) connects containers
	  collapsed:: true
		- ![image.png](../assets/image_1679014086117_0.png)
		- Connect images to network
		  collapsed:: true
			- ![image.png](../assets/image_1679014315722_0.png){:height 235, :width 462}
			- ![image.png](../assets/image_1679014359915_0.png)
		- Bind specific container to another
			- ```bash
			  docker attach client
			  curl http://server:80
			  ```
- # Docker in Windows 11 Pro
	- ## Enable Windows feature
	  collapsed:: true
		- red for windows container
		- green for linux container
		- ![image.png](../assets/image_1730206360300_0.png)
	- Move Docker to Other Places
		- [Reference]([How to Change Docker Data Root Path on Windows 10](https://kontext.tech/article/1216/how-to-change-docker-data-root-path-on-windows-10))
		- 1. move distro
		  ```bash
		  wsl -l -v
		  wsl --shutdown docker-desktop
		  wsl --export docker-desktop E:\docker-desktop\docker-desktop.tar
		  wsl --unregister docker-desktop
		  wsl --import docker-desktop E:\docker-desktop\distro E:\docker-desktop\docker-desktop.tar --version 2
		  ```
		- 2. move linux container `data-root`
		- 3. move windows container `data-root` to same folder
	-
- # Docker in VS Code
	- [Tutorial: Get started with Docker apps in Visual Studio Code | Microsoft Learn](https://learn.microsoft.com/en-us/visualstudio/docker/tutorials/docker-tutorial?WT.mc_id=vscode_docker_aka_helppanel)
	- [VS Code Docker Extension - YouTube](https://www.youtube.com/playlist?list=PLReL099Y5nRf3XEK2f8G8FpMi3XSGPcSZ)
	- [Docker extension for Visual Studio Code](https://code.visualstudio.com/docs/containers/overview)
- # Docker examples
	- ((641be390-ce93-48f0-80fc-ccc2546e712b))
- # Docker and CUDA and WSL
	- [ashishpatel26/Cuda-installation-on-WSL2-Ubuntu-20.04-and-Windows11: Cuda installation on WSL2 Ubuntu 20.04 and Windows11](https://github.com/ashishpatel26/Cuda-installation-on-WSL2-Ubuntu-20.04-and-Windows11)
	-
	-