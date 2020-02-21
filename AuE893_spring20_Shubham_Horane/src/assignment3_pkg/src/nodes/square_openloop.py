#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pi
#from numpy import np

def move():
    # Starts a new node
    rospy.init_node('ros_basics_tuts', anonymous=True)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    #Receiveing the user's input
    print("Your robot will now move in a square. Be patient and enjoy!")

    # below variables help execute the desired path with desired speeds
    side_length = 2
    turn_angle = pi/2
    sides = 4
    x_speed = 0.2
    ang_speed = 0.2

    # Initializing all speed values
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0



    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = float(rospy.Time.now().to_sec())
        current_distance = 0
        current_angle = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < side_length):

            #Setting the required translational speed
            vel_msg.linear.x = x_speed
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_distance= (vel_msg.linear.x)*(t1-t0)
        
        #After one side length is traversed, stops the robot and prepares for turning
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        #Publish
        velocity_publisher.publish(vel_msg)

        sides = sides - 1
        if sides<1: break


        while(current_angle < (turn_angle)):

            #Setting the required angular speed
            vel_msg.angular.z = ang_speed
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t2=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_angle= (vel_msg.angular.z) * (t2-t1)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        #Publish
        velocity_publisher.publish(vel_msg)
    print("Square Complete! Thank you for your patience!")
    











if __name__ == '__main__':
    try:
        #Testing our function
        move()
        
    except rospy.ROSInterruptException: pass
