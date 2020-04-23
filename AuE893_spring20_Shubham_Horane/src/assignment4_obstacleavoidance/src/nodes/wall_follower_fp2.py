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
left_min =0
left = 0
right = 0
front = 0

def callback_scan(msg):
    global left_dist, right_dist, front, left_theta, right_theta, n_w, left_ar, right_ar, right_min, front_cone, left_min

    left_dist = msg.ranges[90]
    right_dist = msg.ranges[270]
    print("| left: " , left_dist, "front: ", msg.ranges[0],"| right:", right_dist)
    # print("width: ", (left_dist+right_dist))



    if left_ar == float('inf'): n_w =2
    if right_ar == float('inf'): n_w =3
    if front < 1.0: n_w = 1

    right_cone = []
    for i in range(200,341):
        right_cone.append(msg.ranges[i])
    right_min = sum(right_cone) / len(right_cone)

    left_cone = []
    for i in range(110,251):
        left_cone.append(msg.ranges[i])
    left_min = sum(left_cone) / len(left_cone)

    front_cone = []
    for j in range(355,359):
        front_cone.append(msg.ranges[j])
    for k in range(0,6):
        front_cone.append(msg.ranges[k])
    front = min(front_cone)

def callback(data):
    global left, right, front
    left = data.ranges[90]
    right = data.ranges[270]
    front = data.ranges[0]




if __name__ == '__main__':

    global right_min, left_min, left, right,front
    rospy.init_node('gazebo_scan_sub')
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    scan_sub = rospy.Subscriber('/scan', LaserScan, callback)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.08
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        # while front < 1:
        #     if left_dist == float('inf'): dir = 1
        #     elif right_dist == float('inf'): dir = -1
        #     elif left_dist>right_dist: dir = 1
        #     else: dir = -1

        #     vel_msg.angular.z = dir * 0.4
        #     vel_pub.publish(vel_msg)
        # vel_msg.angular.z = 0
        # vel_pub.publish(vel_msg)


        # if right_dist == float('inf'): continue
        # else: 
        #     error = right_min - 0.25
        #     if error > 0: j = -1
        #     if error < 0: j = 1
        #     vel_msg.angular.z = j * 1 * 0.4
        #     vel_pub.publish(vel_msg)
        #     time.sleep(0.02)
        #     vel_msg.angular.z = 0
        #     vel_pub.publish(vel_msg)
        
        error = 0.3 - right
        if right == float("inf"): vel_msg.angular.z = 0
        else: 
            while error>0.01:
                vel_msg.angular.z = error
        vel_pub.publish(vel_msg)
        print(vel_msg.angular.z)
        # print(left_min)
        # print(right_min)
        # if right_min != float("inf"):
        #     error = 0.3 - right_min
        #     # if error == float("inf"): error = 0
        #     vel_msg.angular.z = error 
        #     print(vel_msg.angular.z)
        # vel_pub.publish(vel_msg)


        rate.sleep()
    rospy.spin()