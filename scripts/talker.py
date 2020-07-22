#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import Float32

ser = serial.Serial("/dev/ttyACM0")    #Open named port 
ser.baudrate = 115200

def talker():
    pub = rospy.Publisher('YawChatter', Float32, queue_size=50)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(20) # 10hz
    while not rospy.is_shutdown():
        strdata = ser.readline().rstrip() # delete CRLF
        yaw = float(strdata)
        pub.publish(yaw)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
