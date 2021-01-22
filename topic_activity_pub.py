#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String


if __name__=='__main__':
    rospy.init_node("fake_beat_publisher")
    pub=rospy.Publisher('/signal',String,queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        msg=String()
        msg.data='heartbeat recieved'
        pub.publish(msg)
        rate.sleep()
    rospy.loginfo("killed")