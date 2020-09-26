## ASSIGNMENT 6: Finite-State Machine implementation for autonomous module switching

NOTE: To add this package to your own workspace, copy [this](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/turtlebot3_auefinals_pkg) folder to the src folder of your workspace and run the below command in the package directory.
```
catkin_make
```

Three videos describing each task of this assignment can be found in the following path:
/src/turtlebot3_auefinals_pkg/videos

The launch files can be found in the [launch](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/turtlebot3_auefinals_pkg/launch) folder

The python script files can be found in the [nodes](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/turtlebot3_auefinals_pkg/nodes) folder.


### NOTE: CAMERA ADDITION TO TURTLEBOT3 BURGER IN GAZEBO

Camera is not available by default in the TurtleBot burger model defined in Gazebo. The process to add camera to this model has been outlined [here](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing)

### This assignment package has one launch file for all required tasks:

filename: "final_launch.launch"

- This file initializes the following nodes:

1. The auefinal world

2. The standing person which will be used for leg tracking

3. The person teleop window

4. Leg detection package

5. Tiny yolo package

6. Main integrated python script for the requirements of the final project: 

NOTE: This componenet of the launch file has been commented to allow for the world and the several nodes load up correctly. This node can be run manually after everything has loaded to ensure that the bot starts moving only after it can be seen in the world.

7. hector slam navigation package (arg value can be changed to run the other packages if they are installed in your system)


- The command for executing the above launch file is:
```
$ roslaunch turtlebot3_auefinals_pkg final_launch.launch 
```
- The command to run the integrated node is : 
```
$ rosrun turtlebot3_auefinals_pkg aue_final.py 
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/turtlebot3_auefinals_pkg/videos/Media1.gif" height="400" />













