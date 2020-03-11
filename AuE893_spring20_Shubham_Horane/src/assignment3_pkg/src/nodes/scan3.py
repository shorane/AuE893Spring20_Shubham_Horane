#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from math import cos
from math import pi
import time

global distance
# global dist
# dist = 0
# dist = 0
distance = []
# obstacle = 0 			#global variable used as flag for obstacle detection

def callback_scan(msg):		#subscription to scan topic
    # global obstacle 
    # global dist
    # dist = 0
    # obstacle = 0
    rospy.loginfo("Distance to left "+str(msg.ranges[90])+"Distance to right "+str(msg.ranges[270]))
    # global distance = []
    # k = 1.3
    for i in range(240,300):
        distance.append(msg.ranges[i])

    # dist = msg.ranges[270]

    # for j in range(len(distance)):
    #     vel_msg.angular.z += k*(distance(j)*cos((60+j)*pi/180)-0.7)
    # distance_range= []	#list that contains only valid readings
    # for i in range(60,120):
	# 	distance_range.append(msg.ranges[i])
    # length = len(distance_range) #lengh of list containing valid reading
    # index = int(length/2)	     #identifying center element of list	
    # distance = 10     
    # distance = distance_range[index] #center distance 
    # rospy.loginfo("Distance to obstacle "+str(distance))
    # if distance < 0.1:             #checking whether distance is less than threshold
    # 	obstacle = 1         #flag set to 1 indicating obstacle detected


if __name__ == '__main__':
    global dist
    rospy.init_node('gazebo_scan_sub')   #initializing node
    vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10) #publisher to publish velocity
    scan_sub = rospy.Subscriber('/scan',LaserScan,callback_scan) #subscriber for /scan topic
    rate = rospy.Rate(10)	#setting loop rate
    vel_msg = Twist()
    vel_msg.linear.x = 0 #setting x direction velocity to 0.1 and rest to 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    k = 0.25
    while not rospy.is_shutdown():
        for j in range(len(distance)):
            vel_msg.angular.z = -k*(distance[j]*cos((240+j)*pi/180)-0.4)
            # print(dist)
            # vel_msg.angular.z += -k*(dist-0.7)
            vel_msg.linear.x = 0
            vel_pub.publish(vel_msg)
            time.sleep(0.5)
            vel_msg.angular.z = 0
            vel_msg.linear.x = 0.5
            vel_pub.publish(vel_msg)
            time.sleep(0.5)
            # vel_pub.publish(vel_msg)
            rate.sleep()
