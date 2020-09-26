## ASSIGNMENT 5: GROUP 6

NOTE: To add this package to your own workspace, copy [this](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing) folder to the src folder of your workspace and run the below command in the package directory.
```
catkin_make
```

NOTE: for this implementation, you must already be connected to a turtlebot via ssh, and any teleop operations shold be turned off before running the files of this package. The setup instructions for the turtlebot robot can be found [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

The launch files can be found in the [launch](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/launch) folder.

The python script files can be found in the [nodes](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/nodes) folder

--------------------------------------------------------------------------------------
### NOTE: CAMERA ADDITION TO TURTLEBOT3 BURGER IN GAZEBO

For the simulation part of this assignemnt in gazebo, the turtlebot3 burger model was used in keeping with the trend of using the actual model provided to the group for real life implementation. Hence, the camera configuration settings were added to the burger model .xacro files in the below path (where catkin_ws is the name of the workspace where the relevatn turtlebot3 packages are installed):
```
/catkin_ws/src/turtlebot3/turtlebot3_description
```
for runnning the below (part 1a) files correctly, the following two files in the above path must be added (replace existing files with below files):
```
turtlebot3_burger.gazebo.xacro
turtlebot3_burger.urdf.xacro
```
These files can be found in this repository in the [camera_in_burger](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/camera_in_burger)

### NOTE: CAMERA CALIBRATION

This was accomplished by using the following commands after setting up the camera on the turtlebot3 burger robot:
The prefix 'pi@raspberrypi$' means the corresponding command must be run after doing ssh into the turtlebot raspberry pi computer.
```
$ roscore
```
```
pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch
```
```
$ rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw 
$ rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.0245 image:=/raspicam_node/image_raw camera:=/raspicam_node
```
(the square side dimension (0.0245) was obtained after printing the calibration checkerboard on an A4 sheet. This sheet was used for calibrating the camera. Instructions were followed as per instructions on [this page](http://wiki.ros.org/camera_calibration))

**This assignment package has three launch files: (for parts 1a, 1b and 2):**

**1a. filename: "1a_follow_line.launch"**

- This file initializes the line following world in gazebo
- It launches the line follower python script as a node for detecting and following the yellow path in the given simulation world in gazebo
- The command for executing the above launch file is:
```
$ roslaunch assignment5_trackingandfollowing 1a_follow_line.launch 
```
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/videos/AuE893-Assignment-5-Part-1a-Line.gif" height="400" />

**1b. filename: "1b_follow_line.launch"**

- This part shows the practical implementation of the line following functionality shown in the above part
- This requires setting up a turtlebot3 burger robot with a raspberry pi camera v2 
- The bot must be setup as a slave in a ROS network where a remote computer is the ROS master
- The following commands must be executed before runnning the above launch file (each command in a new terminal):

note: the prefix 'pi@raspberrypi$' means the corresponding command must be run after doing ssh into the turtlebot raspberry pi computer.
```
$ roscore
```
```
pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch
```
```
$ rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw
```
- Finally, the launch file can be executed: 
```
$ roslaunch assignment5_trackingandfollowing 1b_follow_line.launch 
```
- The final launch file starts the line following node that allows the bot to follow white lines in a moderately lit environment.
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/videos/TB-line-follower.gif" height="400" />

**3."2_continuous_detection_and_bot_moving.launch"**

- This part enables the turtlebot3 burger to detect and follow a defined Apriltag code around a room.
- For this assignment, only 1 tag was required to accomplish the requirements, hence tag id 7 was used.
- This task required the installation of the relevant apriltag packages in the catkin workspace. These packages can be found in the following github pages:
```
[https://github.com/AprilRobotics/apriltag_ros](https://github.com/AprilRobotics/apriltag_ros)
[https://github.com/AprilRobotics/apriltag](https://github.com/AprilRobotics/apriltag)
```
(instructions for installing each package are mentioned in the corresponding Readme.md files on the github pages and were followed. Both packages were successfully installed)

- The tags.yaml file present in the [config](https://github.com/shorane/ROS_Autonomous_TurtleBot/tree/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/config) folder contains the decription of the tag with id no.7. This file is must be placed in the path ```/apriltag_ros/config``` where the apriltag_ros package is installed in your corresponding workspace.

- After above configuration, the following commands must be executed before runnning the main launch file (each command in a new terminal):

note: the prefix 'pi@raspberrypi$' means the corresponding command must be run after doing ssh into the turtlebot raspberry pi computer.
```
$ roscore
```
```
pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch
```
```
$ rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw
```
- Finally, the launch file can be executed: 
```
$ roslaunch assignment5_trackingandfollowing 2_continuous_detection_and_bot_moving.launch 
```
- Holding the apriltag with id 7 in front of the bot at a distance will result in the bot following the tag. The bot will stop at a distance of 0.3 meters from the tag if the tag is held in one place for long enough. Due to camera lag, the detection faces minor issues at times.
<img src="https://github.com/shorane/ROS_Autonomous_TurtleBot/blob/master/AuE893_spring20_Shubham_Horane/src/assignment5_trackingandfollowing/videos/TB_apriltag.gif" height="400" />
