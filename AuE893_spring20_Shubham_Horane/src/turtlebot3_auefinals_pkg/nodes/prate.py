#!/usr/bin/env python

import rospy
import math
import time
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from people_msgs.msg import PositionMeasurementArray
from math import sqrt, atan2
# from follow_line_step_hsv import *
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
# from move_robot import MoveTurtlebot3

distanceo_1 = 1
distanceo_2 = 1
distanceo_3 = 1
tags = []
dist = 0
steer = 0
person_x = 0
person_y = 0
robot_x = 0
robot_y = 0
phi = 0

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           
    if len(num) != 0:
        avg = sum_num / len(num)
        return avg

def call_back_leg_detector(msg):
    global tags
    global person_x
    global person_y
    global phi
    tags = msg.people
    if len(tags) != 0:
        person_x = msg.people[0].pos.x
        person_y = msg.people[0].pos.y
    
def pose_data(msg_2):
    global robot_x
    global robot_y
    global phi 
    robot_x = msg_2.pose.pose.position.x
    robot_y = msg_2.pose.pose.position.y
    q_x = msg_2.pose.pose.orientation.x 
    q_y = msg_2.pose.pose.orientation.y 
    q_z = msg_2.pose.pose.orientation.z
    q_w = msg_2.pose.pose.orientation.w 
    K = 2*(q_w*q_z + q_x*q_y)
    L = 1 - 2*(q_y**2 + q_z**2)
    phi = np.arctan2(K, L)

def call_back_obs(obs_msg):
    global laserscan
    global distanceo_1
    global distanceo_2
    global distanceo_3
    distanceo_1 = []
    distanceo_2 = []
    distanceo_3 = []
    laserscan = obs_msg

    for i,value in enumerate(laserscan.ranges):
        if (i <= 20 or i >=340):
            distanceo_1.append(value)
        if (i>20 and i<=60)  and value != float('inf'):
            distanceo_2.append(value)
        if (i>300 and i<=330)  and value != float('inf'):
            distanceo_3.append(value)

    distanceo_1 = min(distanceo_1)
    if distanceo_1 == float('inf'):
        distanceo_1 = 10
    distanceo_2 = cal_average(distanceo_2)
    distanceo_3 = cal_average(distanceo_3)
    

def obstacle_avoidance():
    
    if distanceo_1 < 0.2:
        vel_msg.linear.x = 0.01
        p= 1
    else:
        vel_msg.linear.x = 0.10
        p = 1
    str_angle = p*(distanceo_2 - distanceo_3)
    vel_msg.angular.z = str_angle
    velocity_publisher.publish(vel_msg)

def leg_detect():
    sub_people = rospy.Subscriber('/people_tracker_measurements', PositionMeasurementArray, call_back_leg_detector)
    sub_robot_pose = rospy.Subscriber('/odom', Odometry, pose_data)
    
    theta =   atan2((person_y - robot_y), (person_x - robot_x)) - phi  
    x = (person_x - robot_x)
    y = (person_y - robot_y)
    distance = sqrt(x**2 + y**2)
    print(theta, 'theta')
    print("distance front- ", distance)
    if distance < 0.2:
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
    elif distance > 0.2 and distance < 0.8:
        p_steer = 0.5
        p_dist = 0.2
        vel_msg.linear.x = distance*p_dist
        vel_msg.angular.z = theta*p_steer
        # if vel_msg.angular.z > 0.2:
        #     vel_msg.angular.z = 0.1
    else:
        p_steer = 0.5
        vel_msg.linear.x = 0.1
        vel_msg.angular.z = theta*p_steer
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    rospy.init_node('move_combined_code')
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    follower_subscriber_obs = rospy.Subscriber('/scan' , LaserScan, call_back_obs)
    vel_msg = Twist()
    rate = rospy.Rate(5)

    # line follower part
    # line_follower_object = LineFollower()
    # ctrl_c = False
    # def shutdownhook():
    #     line_follower_object.clean_up()
    #     rospy.loginfo("shutdown time!")
    #     ctrl_c = True
    # rospy.on_shutdown(shutdownhook)
    
    while not rospy.is_shutdown():
        obstacle_avoidance()
        # leg_detect()
        rate.sleep()
