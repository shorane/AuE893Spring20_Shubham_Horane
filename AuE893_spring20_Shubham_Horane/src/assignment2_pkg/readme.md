## Assignment 2: Turtlesim basics

NOTE: TO add this package to your own workspace, copy [this](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment2_pkg) folder to the src folder of your workspace and run the below command in the package directory.
```
$ catkin_make
```
You must also have the [turtle_sim package](http://wiki.ros.org/turtlesim) pre-installed. Now, run the turtlesim application:
```
$ rosrun turtlesim turtlesim_node
```

**1. Circle.py:**
- This code controls the turtlebot and moves it in a circular path. 
- It runs the turtlebot with pre-decided linear and angular velocities.
- The bot stops moving after it completes one circle.
- To run this program, run the below command in the package directory while the above-mentioned turtlesim program is running:
```
$ rosrun assignment2_pkg circle.py
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment2_pkg/Images_Assignment_2/Circle_Screenshot.png" height = "400"/>

**2. Square_Open_loop:**
- This code runs the turtlebot in a square of 2x2 units once. 
- To run this program, run the below command in the package directory while the above-mentioned turtlesim program is running:
```
$ rosrun assignment2_pkg square_openloop.py
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment2_pkg/Images_Assignment_2/Square_Open_loop_Screenshot.png" height = "400"/>


**3. Square_Closed_loop:**
- This code runs the turtle bot from its starting position to the coordinates (5,5)
- From here the bot sequentially moves along the following coordinates and completes a 3x3 units square:
(8,5); (8,8); (5,8); (5,5)
- To run this program, run the below command in the package directory while the above-mentioned turtlesim program is running:
```
$ rosrun assignment2_pkg square_closedloop.py
```

<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment2_pkg/Images_Assignment_2/Square_Closed_loop_Screenshot.png" height = "400"/>
_____________________________________________________
 
