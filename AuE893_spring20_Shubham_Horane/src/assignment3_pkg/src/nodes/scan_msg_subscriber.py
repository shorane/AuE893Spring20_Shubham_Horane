#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

obstacle = 0 

def callback_scan(msg):
	global obstacle 
	obstacle = 0
	#rospy.loginfo((msg.ranges))
	distance = msg.ranges[359]
	rospy.loginfo(distance)
	if distance < 2:
		rospy.loginfo("obstacle nearby")
		obstacle = 1

if __name__ == '__main__':
	global obstacle
	rospy.init_node('gazebo_scan_sub')
	vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
	scan_sub = rospy.Subscriber('/scan',LaserScan,callback_scan)
	rate = rospy.Rate(10)
	vel_msg = Twist()
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	while not rospy.is_shutdown():
		if obstacle == 1:
			vel_msg.linear.x = 0
			rospy.loginfo("safe")
		vel_pub.publish(vel_msg)
		#rospy.loginfo("velocity publish")
		rate.sleep()
	#vel_msg.linear.x = 0
	#vel_pub.publish(vel_msg)

	
