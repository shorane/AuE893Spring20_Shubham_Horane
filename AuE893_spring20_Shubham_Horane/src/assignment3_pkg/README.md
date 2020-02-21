--------------------------------------------------------------------------------------
			ASSIGNMENT 3: GROUP 6
--------------------------------------------------------------------------------------
Group members: 

1. Shubham Horane
2. Rahil Modi
3. Manikanda Balaji
4. Chase Gurcan
5. Akshay Hole
--------------------------------------------------------------------------------------
Three videos describing each task of this assignment can be found in the following path:

/src/assignment3_pkg/videos

The launch files can be found in the path: /src/assignment3_pkg/src/launch

The python script files can be found in the path: /src/assignment3_pkg/src/nodes

The gazebo world files can be found in the path: /src/assignment3_pkg/src/worlds
--------------------------------------------------------------------------------------

This assignment package has two launch files: (One for each part)

1. move.launch

- This file initializes an empty world in gazebo

- It launches nodes for moving the robot in a circlular or square motion depending on the argument provided while executing the launch command.

- The command for execution with circular motion is: 

$ roslaunch assignment3_pkg move.launch code:=circle

- The command for execution with open loop square motion is: 

$ roslaunch assignment3_pkg move.launch code:=square
----------------------------------------------------------------------------------------

2. turtlebot3_wall.launch

- This file initializes a world based on the empty world environment.

- This world has a wall in the path of the turtlebot

- This file also launches the python node which executed the desired wall detection and stopping behavior of the turtlebot

- The command for execution of this launch file is:

$ roslaunch assignment3_pkg turtlebot3_wall.launch
----------------------------------------------------------------------------------------

Work was divided between two sub-groups within our team:

sub-group #1: Shubham Horane & Chase Gurcan.

- Writing python script for circle and square motion
- Preparing launch file with argument functionality for executing desired file.

sub-group #2: Rahil Modi, Manikanda Balaji, & Akshay Hole.

- Writing python script for object detection and response
- Preparing new world in Gazebo with a wall-like obstacle
- Preparing launch file for opening the world and executing the python script
----------------------------------------------------------------------------------------












