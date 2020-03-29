#!/usr/bin/env python
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from apriltag_ros.msg import AprilTagDetectionArray

x_diff = 0
z_diff = 0

def callback(data):
    global x_diff
    global z_diff
    # extracting the relative positions of the tag in X and Z axis
    x_diff = data.detections[0].pose.pose.pose.position.x
    z_diff = data.detections[0].pose.pose.pose.position.z


if __name__ == '__main__':

    # Defining publisher and subscriber
    rospy.init_node('Follow_apriltag', anonymous=True)
    vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    tag_sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, callback)

    # P-control over steering and linear forward velocity for apriltag following
    rate = rospy.Rate(10)
    vel = Twist()

    while not rospy.is_shutdown():

        # Linear velocity control
        Kp_linear = 0.25
        Kp_angular = 5
        f = 0
        if z_diff < 0.3:
            vel.linear.x = 0
        else:
            vel.linear.x = z_diff*Kp_linear

        # Steering Control
        if x_diff < 0: f = 1
        if x_diff > 0: f = -1
        vel.angular.z = f * Kp_angular * x_diff
        # publish velocity
        vel_pub.publish(vel)

        rate.sleep()
    rospy.spin()
