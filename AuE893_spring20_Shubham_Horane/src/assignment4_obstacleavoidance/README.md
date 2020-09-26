## ASSIGNMENT 4: GROUP 6

NOTE: TO add this package to your own workspace, copy [this](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment4_obstacleavoidance) folder to the src folder of your workspace and run the below command in the package directory.
```
$ catkin_make
```

The launch files can be found in the [launch](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment4_obstacleavoidance/src/launch) folder

The python script files can be found in the [nodes](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment4_obstacleavoidance/src/nodes) folder

This assignment package has three launch files:

**1. turtlebot3_wallfollowing.launch**

- This file initializes the wall_following world in gazebo
- It launches the wall_follower.py file as a node for moving the turtlebot between the two walls and avoiding any collisions with these walls
- The command for executing the above launch file is:
```
$ roslaunch assignment4_obstacleavoidance turtlebot3_wallfollowing.launch 
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment4_obstacleavoidance/videos/Wall-Gazebo.gif" height="400" />

**2. turtlebot3_obstaceavoidance.launch**

- This file initializes the obstacle_avoidance world.
- This world has several obstacles that the turtlebot must avoid
- This file also launches the wander.py node which executes the desired obstacle avoidance behavior of the turtlebot
- Since the turtlebot has no goal location, it just keeps wandering in the world while avoiding obstacles
- The command for execution of this launch file is:
```
$ roslaunch assignment4_obstacleavoidance turtlebot3_obstaceavoidance.launch 
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment4_obstacleavoidance/videos/Gazebo-wanderer.gif" height="400" />

**3. turtlebot3_obstaceavoidance.launch   (same file as part 2)**

- The python code wander.py used in part 2 was applied on the turtlebot burger and rested with the help of some boxes places as obstacles in the path of the robot.
- The video named 'Wanderer_RealScenario' in the videos folder shows this functionality.
- The command for execution of this launch file is:
```
$ roslaunch assignment4_obstacleavoidance turtlebot3_obstaceavoidance.launch
```

<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment4_obstacleavoidance/videos/TB_wanderer.gif" height="400" />










