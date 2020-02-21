#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

obstacle = 0 			#global variable used as flag for obstacle detection

def callback_scan(msg):		#subscription to scan topic
	global obstacle 
	obstacle = 0
	distance_range= []	#list that contains only valid readings
	for i in msg.ranges:
		if i < 10:	#to take the valid readings from scan topic
			distance_range.append(i) 
	length = len(distance_range) #lengh of list containing valid reading
	index = int(length/2)	     #identifying center element of list	
	distance = 10     
	distance = distance_range[index] #center distance 
	rospy.loginfo("Distance to obstacle "+str(distance))
	if distance < 1:             #checking whether distance is less than threshold
		obstacle = 1         #flag set to 1 indicating obstacle detected

if __name__ == '__main__':
	global obstacle
	rospy.init_node('gazebo_scan_sub')   #initializing node
	vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10) #publisher to publish velocity
	scan_sub = rospy.Subscriber('/scan',LaserScan,callback_scan) #subscriber for /scan topic
	rate = rospy.Rate(10)	#setting loop rate
	vel_msg = Twist()
	vel_msg.linear.x = 0.1 #setting x direction velocity to 0.1 and rest to 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	while not rospy.is_shutdown():
		if obstacle == 1:		#control when obstacle is detected
			vel_msg.linear.x = 0	#x direction velocity set to 0 when obstacle is detected
			#rospy.loginfo("safe")
		vel_pub.publish(vel_msg)	#publishing velocity command
		rate.sleep()


	
