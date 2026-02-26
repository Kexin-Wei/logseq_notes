- Docker Images and Docker Containers
	- ![image.png](../assets/image_1679013741651_0.png)
- Bridge ( or Network ) connects containers
	- ![image.png](../assets/image_1679014086117_0.png)
	- Connect images to network
		- ![image.png](../assets/image_1679014315722_0.png){:height 235, :width 462}
		- ![image.png](../assets/image_1679014359915_0.png)
	- Bind specific container to another
		- ```bash
		  docker attach client
		  curl http://server:80
		  ```