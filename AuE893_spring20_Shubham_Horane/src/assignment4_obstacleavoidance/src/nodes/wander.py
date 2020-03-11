#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

global left_dist, right_dist, front, left_theta, right_theta, n_w, left_ar, right_ar
global right_cone, right_min, front_cone, ind
ind = 0
right_cone = []
front_cone = []
right_min = 0 
left_dist = 0
right_dist = 0 
left_theta = 0
right_theta = 0
front = 0
left_ar = 0
right_ar = 0
n_w = 0


def callback_scan(msg):
    global left_dist, right_dist, front, left_theta, right_theta, n_w, left_ar, right_ar, right_min, front_cone
    global ind
    # storing the scan values in the 20 degree frontal cone
    p = []
    p = msg.ranges

    front_cone = []
    for j in range(340,360):
        if p[j] ==0: front_cone.append(999)
        else: front_cone.append(p[j])
    for k in range(0,21):
        if p[k]==0: front_cone.append(999)
        else: front_cone.append(p[k])
    front = min(front_cone)
    ind = p.index(front)
    print(front, ind)


if __name__ == '__main__':
    global ind
    rospy.init_node('gazebo_scan_sub')
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    scan_sub = rospy.Subscriber('/scan', LaserScan, callback_scan)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.3
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        # checking obstacles in cone and turning accordingly
        
        while front < 0.7:
            # print(ind)
            if 0 < ind < 21: vel_msg.angular.z = -1.5
            # elif ind == 0 : vel_msg.angular.z = -1.5
            elif 339 < ind < 360 : vel_msg.angular.z = 1.5
            # vel_msg.angular.z = dir * 1.5
            vel_pub.publish(vel_msg)
            time.sleep(0.05)
        vel_msg.angular.z = 0
        vel_pub.publish(vel_msg)

        rate.sleep()
    rospy.spin()