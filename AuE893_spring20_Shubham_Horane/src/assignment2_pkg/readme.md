## Turtlesim basics

The catkin_ws directory contains several packages in its src folder. The packages having the naming convention like "Assignment_2" are packages for submissions pertaining to the course AuE 893 Spring 2020.

A general convention followed is that python scripts will be stored in the "scripts" folder and cpp files will be stored in the "src" folders of each package.

This workspace contains several packages
_____________________________________________________
-----------------------------------------------------
Assignment 2: Turtlesim basics
-----------------------------------------------------
**1. Circle.py:**
- This code controls the turtlebot and moves it in a circular path. 
- It runs the turtlebot with pre-decided linear and angular velocities.
- The bot stops moving after it completes one circle.
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment2_pkg/Images_Assignment_2/Circle_Screenshot.png" width = "400" height = "400"/>

**2. Square_Open_loop:**
- This code runs the turtlebot in a square of 2x2 units once. 

**3. Square_Closed_loop:**
- This code runs the turtle bot from its starting position to the coordinates (5,5)
- From here the bot sequentially moves along the following coordinates and completes a 3x3 units square:
(8,5); (8,8); (5,8); (5,5)
_____________________________________________________
 
