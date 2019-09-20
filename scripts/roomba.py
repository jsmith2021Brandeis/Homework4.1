#Jacob Smith Cosi 119A 9/20/2019
#Roomba Assignment, used wander.py as template
#!/usr/bin/env python

#Variables used in tuning robot
LINEAR_VEL=.5
TURN_VEL=1
DISTANCE_THRESH=.8

#import necesary libraries
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from random import randint
from time import sleep

# Function is called every time there's a scan
# Saves the smallest distance, which would be the closest obstacle
# This is without regard to the direction of the obstacle!
# global keyword is needed so g_range_ahead is available outside of the function
def scan_callback(msg):
    global g_range_ahead
    g_range_ahead = msg.ranges[0]

# Main program
g_range_ahead = 1 # anything to start

# Declare a subscriber to message 'scan' with message class LaserScan
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

# Same code can be a publisher and a subscriber, this is no problem
# be ready to publish the cmd_vel topic of class Twist
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

# Declare us to be a node
rospy.init_node('roomba')
state_change_time = rospy.Time.now()

# driving_forward: forward(true) vs. spin inplace (false)
#   TRUE: until x seconds pass or get close to an obstacle, go forward
#   FALSE: until y seconds pass, spin in place
driving_forward = True
rate = rospy.Rate(1)

while not rospy.is_shutdown():

    # Create an all zero Twist() message. Note a new one is created each loop
    twist = Twist()
    #if robot is too close to a wall, turn
    if g_range_ahead<DISTANCE_THRESH:
        twist.angular.z=TURN_VEL
    # if robot is not too close to a wall, move forward
    else:
        twist.linear.x = LINEAR_VEL
    print (g_range_ahead, twist.linear.x)
    #publish robot motion
    cmd_vel_pub.publish(twist)
    # Sleep for 1/rate seconds
    rate.sleep()
  