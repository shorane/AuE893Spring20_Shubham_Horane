## ASSIGNMENT 3: TurtleBot basic movement in Gazebo

NOTE: To add this package to your own workspace, copy [this](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment2_pkg) folder to the src folder of your workspace and run the below command in the package directory.
```
$ catkin_make
```

This package comtains basic movement examples of the TurtleBot Burger robot in Gazebo.

The [launch](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment3_pkg/src/launch) folder contains the launch files

The [nodes](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment3_pkg/src/nodes) folder contains the scripts

The [worlds](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment3_pkg/src/worlds) folder contains the gazebo world files.

This assignment package has two launch files:

**1. move.launch**

- This file initializes an empty world in gazebo
- It launches nodes for moving the robot in a circlular or square motion depending on the argument provided while executing the launch command.
- The command for execution with circular motion is: 
```
$ roslaunch assignment3_pkg move.launch code:=circle
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment3_pkg/videos/AuE893-Assignment-3-Part-1-circl.gif" height="400" />

- The command for execution with open loop square motion is: 
```
$ roslaunch assignment3_pkg move.launch code:=square
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment3_pkg/videos/AuE893-Assignment-3-Part-1-squar.gif" height="400" />

**2. turtlebot3_wall.launch**

- This file initializes a world based on the empty world environment.

- This world has a wall in the path of the turtlebot

- This file also launches the python node which executed the desired wall detection and stopping behavior of the turtlebot

- The command for execution of this launch file is:
```
$ roslaunch assignment3_pkg turtlebot3_wall.launch
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment3_pkg/videos/AuE893-Assignment-3-Part-2-scann.gif" height="400" />











