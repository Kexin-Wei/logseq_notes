- Intro
- Autonomous Car Level - SAE J3016
  [[@A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles]] 
  0. all human
  1. adaptive cruise control, anti-lock braking system, electronic stabilty control
  2. hazard-minimizing longitudinal/ lateral control, emergency braking
  3. full autonomy under certain condition, but human take control when in danger
  4. full autonomy under certain condition, can replace human at some cases
  5. fully autonomous
- Decision making
	- On-board sensors
		- LIDAR
		- camera
		- GPS/INS
		- odometry(angle)
- Hierachical Decision Making System
  ![this](/../assets/slc_pic1.png)
	- Route Planning
		- Dijkstra
		- A*
	- Behavioral Layer: local driving task under rules and planned route
		- Input
			- other traffic participants
			- road conditions
			- signals from infrastructure
		- driving manual -> finite sets of actions -> finite state machine
		- uncertainty of behaviour -> predictive planning/ probabilistic planning formalisms
			- Probabilistic planning formalism : Markov Decision Process(MDP)
	- Motion Planning
		- cruise-in-lane, change-lane, turn-right -> continous path through the environment
		- static and dynamic obstacles -> collision-free trajectory <- travel time + discomfort
		- Path planning ==Table of Algos==
			- Variational methods
				- rapid convergence to local optimum
			- Graph-search methods
				- not easy to local minima
				- but only a finite set of optimal path
			- Incremental search methods
				- build tree with nodes growing
				- until reach the goal
				     2. Trajectory planning
			- TP in dynamic env = generalized PP in static env
	- Control system: correct errors of motion planning