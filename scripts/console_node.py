#! /usr/bin/3.2/env python
#Jacob Smith 9/9/2019 Cosi 119a Homework 3.2
# used topic_subscriber as template
#reads user input from console

import rospy
from std_msgs.msg import String
print "running console node"
# Make this into a ROS node.
rospy.init_node('console_node')

# Prepare to publish topic `direction`
pub = rospy.Publisher('demo/command', String, queue_size=10)

# sleep at 1 loop per second
rate = rospy.Rate(1)
count = 0

# loop until ^c
while not rospy.is_shutdown():
    #publish a random number every second to represent direction
    command = raw_input("Enter a commant like turn 84: ")
    pub.publish(command)
    rate.sleep()

