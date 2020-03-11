#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

global left_dist, right_dist, front, left_theta, right_theta
global right_cone, right_min, front_cone
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

    left_dist = msg.ranges[90]
    right_dist = msg.ranges[270]


    if left_ar == float('inf'): n_w =2
    if right_ar == float('inf'): n_w =3
    if front < 1.0: n_w = 1

    right_cone = []
    for i in range(200,341):
        right_cone.append(msg.ranges[i])
    right_min = min(right_cone)

    front_cone = []
    for j in range(355,359):
        front_cone.append(msg.ranges[j])
    for k in range(0,6):
        front_cone.append(msg.ranges[k])
    front = min(front_cone)




if __name__ == '__main__':
    rospy.init_node('gazebo_scan_sub')
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    scan_sub = rospy.Subscriber('/scan', LaserScan, callback_scan)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.65
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        while front < 1.25:
            if left_dist == float('inf'): dir = 1
            elif right_dist == float('inf'): dir = -1
            elif left_dist>right_dist: dir = 1
            else: dir = -1

            vel_msg.angular.z = dir * 1.5
            vel_pub.publish(vel_msg)
        vel_msg.angular.z = 0
        vel_pub.publish(vel_msg)


        if right_dist == float('inf'): continue
        else: 
            error = right_min - 0.25
            if error > 0: j = -1
            if error < 0: j = 1
            vel_msg.angular.z = j * 1 * 0.5
            vel_pub.publish(vel_msg)
            time.sleep(0.02)
            vel_msg.angular.z = 0
            vel_pub.publish(vel_msg)

        rate.sleep()
    rospy.spin()