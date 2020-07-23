#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import Float32

ser = serial.Serial("/dev/ttyUSB1") # determine manually
ser.baudrate = 115200

def EBimuAsciiParser():
    str_list = ser.readline().rstrip().split(',')
    yaw = float(str_list[-1])
    return yaw

def talker():
    pub = rospy.Publisher('YawChatter', Float32, queue_size=50)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        yaw = EBimuAsciiParser()
        pub.publish(yaw)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
