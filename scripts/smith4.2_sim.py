#! /usr/bin/3.2/env python
#Jacob Smith 9/9/2019 Cosi 119a Homework 3.2
# used topic_subscriber as template
#simulates robot moving a certain distance
import rospy
from std_msgs.msg import Int32
print "starting simulator"
# define function is called each time the message is published (by some other node)
def callback(msg):
    #publish simulated odemeter data
    pub.publish(msg.data+1)
    sleep(1)

# Make this into a ROS node.
rospy.init_node('smith_sim')

sub = rospy.Subscriber('/cmd_vel', Int32, callback)

#create publisher of direction
pub = rospy.Publisher('/odom', Int32, queue_size=10)

# Wait for published topics, exit on ^c
rospy.spin()