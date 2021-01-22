#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String
import threading

pub=None

def timeout():
    #if timeout, stop the vehicle by publishing the throttle,steer and brake values
    pub=rospy.Publisher('/cmds_for_brake',String,queue_size=5)
    rate=rospy.Rate(1)
    
    while not rospy.is_shutdown():#to avoid confusion in case if netwrok restores during emergency stopping
    
        msg=String()
        msg.data="Throttle:0 Steer:0 Brake:1"
        pub.publish(msg) #publishing the msg
        rate.sleep()

    
def callback_fun(msg):

    global timer

    timer.cancel() #cancel the timer is the message is recieved from the /signal topic 

    timer = threading.Timer(0.2,timeout)
    timer.start()


if __name__=='__main__':
    rospy.init_node('signal_checker')

    sub=rospy.Subscriber('/signal',String,callback_fun)#subscribe to the /signal topic on which the fake heartbeat signal is publishing
    print("heartbeat True")
    
    timer = threading.Timer(0.2,timeout) # If 0.2 seconds elapse, call timeout()
    
    timer.start()

    rospy.spin()
