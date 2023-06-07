- Hardware Setup
	- Raspberry Pi 4 (or Serv Machine): ubuntu server 20 + lubuntu
	- Dev Machine: VirtualBox Ubuntu 20
- Installation
	- Chose Version on machine
		- Ros 2 Foxy + Citadel
		- ![image.png](../assets/image_1685492561147_0.png)
	- ~~macOS 13 -> [Gazebo Fortress](https://gazebosim.org/docs/fortress)~~
	  collapsed:: true
		- has issue, can't run simulation, give up
	- Dev Machine in VirtualBox
		- How to setup network in VirtualBox
			- [Explanation of the Network Setting in VirtualBox](https://www.nakivo.com/blog/virtualbox-network-setting-guide/)
			- chose bridged network
		- Setup netplan
			- Following [this](https://youtu.be/NW97xLF7CYQ?t=403)
				- ![Screenshot 2023-06-08 at 5.04.15 AM.png](../assets/Screenshot_2023-06-08_at_5.04.15_AM_1686172553273_0.png)
			- Raspberry pi same as right side, beware of the gateway, first three numbers should be same as the address
			- VirtualBox Ubuntu Dev Machine
			  collapsed:: true
				- ```yaml 
				  network:
				    version: 2
				    renderer: NetworkManager
				  
				    ethernets:
				      enp0s3:
				        dhcp4: no
				        addresses: [192.168.50.133/24]
				        gateway4: 192.168.50.1
				        nameservers:
				          addresses: [192.168.50.1]
				  ```
			- run restart netplan command on both sides
				- ```bash
				  sudo netplan generate
				  sudo netplan apply
				  ```
		- Connect from Dev Machine to Raspberry Pi using ssh
			- install openssh: `sudo apt install openssh-server`
			- change ssh setting in Serv Machine: `sudo nvim /etc/ssh/sshd_config`
			- change following parts
			  ```txt
			  #To enable password authentication, uncomment
			  PasswordAuthentication yes
			  
			  #To enable root login, uncomment
			  PermitRootLogin yes
			  
			  #To enable SSH key login, uncomment
			  PubkeyAuthentication yes
			  ```
		-