#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

right_min = 0.3
left_min = 0.3
front_min = 10

def callback_scan(msg):
    

    left_dist = msg.ranges[90]
    right_dist = msg.ranges[270]
    print("| left: " , left_dist, "front: ", msg.ranges[0],"| right:", right_dist)

def callback_wall(data):
    global right_min, left_min, front_min
    left = data.ranges[90]
    right = data.ranges[270]
    front = data.ranges[0]
    right_cone = []
    left_cone = []
    front_cone = []
    if right == float("inf"): right_min = 0.3
    else: 
        for i in range(300,341):
            right_cone.append(data.ranges[i])

    if left == float("inf"): left_min = 0.3
    else: 
        for o in range(20,61):
            left_cone.append(data.ranges[o])

    for p in range(len(data.ranges)):
        if p<20 or p>340:
            front_cone.append(data.ranges[p])
        right_min = min(right_cone)
        left_min = min(left_cone)
        front_min = min (front_cone)

if __name__ == '__main__':
    global right_min, left_min, front_min
    rospy.init_node('gazebo_scan_sub')
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    scan_sub = rospy.Subscriber('/scan', LaserScan, callback_wall)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        error = (left_min - right_min)/2
        
        print("error: ", error)
        
        if front_min <= 0.4: 
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0.05
        if front_min > 0.2: vel_msg.linear.x = 0.12 

        if error!= float("inf") and error != float("-inf"):
            vel_msg.angular.z = error * 3
        vel_pub.publish(vel_msg)


        rate.sleep()
    rospy.spin()