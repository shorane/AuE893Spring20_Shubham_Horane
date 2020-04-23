#!/usr/bin/env python
import rospy
import time
import cv2
import numpy as np
from darknet_ros_msgs.msg import BoundingBoxes

def callback(data):
    # print(len(data.bounding_boxes))
    # rospy.loginfo(data.bounding_boxes[0].Class)
    for i in range(len(data.bounding_boxes)):
        rospy.loginfo(data.bounding_boxes[i].probability)
        if data.bounding_boxes[i].Class == "stop sign":
            # seconds_stop = time.time()
            # rospy.loginfo("Time for Stop sign detection before= %f" % (seconds_stop))
            
            rospy.sleep(3)
            # seconds_stop = time.time()
            # rospy.loginfo("Time for Stop sign detection after= %f" % (seconds_stop))

        elif data.bounding_boxes[i].Class == "person":
            seconds_person = time.time()
            print('Time for Person detection before=',seconds_person)
            rospy.sleep(3)
            print('Time for Person detection after=',seconds_person)

if __name__ == '__main__':
    rospy.init_node('stopit',anonymous= True)
    rospy.Subscriber("/darknet_ros/bounding_boxes",BoundingBoxes,callback)
    rospy.spin()
