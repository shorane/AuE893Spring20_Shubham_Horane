--------------------------------------------------------------------------------------
			ASSIGNMENT 4: GROUP 6
--------------------------------------------------------------------------------------
Group members: 

1. Shubham Horane
2. Rahil Modi
3. Manikanda Balaji
4. Chase Gurcan
5. Akshay Hole
--------------------------------------------------------------------------------------
Three videos describing each task of this assignment can be found in the following path:

/src/assignment4_obstacleavoidance/videos

The launch files can be found in the path: /src/assignment4_obstacleavoidance/src/launch

The python script files can be found in the path: /src/assignment4_obstacleavoidance/src/nodes
--------------------------------------------------------------------------------------

This assignment package has three launch files: (One for each part)

1. turtlebot3_wallfollowing.launch

- This file initializes the wall_following world in gazebo

- It launches the wall_follower.py file as a node for moving the turtlebot between the two walls and avoiding any collisions with these walls

- The command for executing the above launch file is:

$ roslaunch assignment4_obstacleavoidance turtlebot3_wallfollowing.launch 

*** - The video named 'Wall_Follower' in the videos folder shows this functionality.
----------------------------------------------------------------------------------------

2. turtlebot3_obstaceavoidance.launch

- This file initializes the obstacle_avoidance world.

- This world has several obstacles that the turtlebot must avoid

- This file also launches the wander.py node which executes the desired obstacle avoidance behavior of the turtlebot

- Since the turtlebot has no goal location, it just keeps wandering in the world while avoiding obstacles

- The command for execution of this launch file is:

$ roslaunch assignment4_obstacleavoidance turtlebot3_obstaceavoidance.launch 


*** - The video named 'Wanderer' in the videos folder shows this functionality.

----------------------------------------------------------------------------------------
3. turtlebot3_obstaceavoidance.launch   (same file as part 2)

- The python code wander.py used in part 2 was applied on the turtlebot burger and rested with the help of some boxes places as obstacles in the path of the robot.

- The video named 'Wanderer_RealScenario' in the videos folder shows this functionality.

- The command for execution of this launch file is:

$ roslaunch assignment4_obstacleavoidance turtlebot3_obstaceavoidance.launch


*** - The video named 'Wanderer_RealScenario' in the videos folder shows this functionality.
----------------------------------------------------------------------------------------

Work was divided between two sub-groups within our team:

sub-group #1: Shubham Horane & Chase Gurcan.

- Writing the script for the wall following task
- Tuning the P-controller and the turtlebot parameters like linear speed, angular velocity and threshold distance from the wall to obtain the desired performance
- Implementing the wander.py code on the actual turtlebot burger model and testing its performance using cardboard boxes

sub-group #2: Rahil Modi, Manikanda Balaji, & Akshay Hole.

- Writing the python script for the obstacle avoidance task
- Tuning the parameters for optimum performance like linear speed and angular velocity for optimum performance
- Implementing the wander.py code on the actual turtlebot burger model and testing its performance using cardboard boxes
----------------------------------------------------------------------------------------












