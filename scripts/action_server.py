#! /usr/bin/env python
#Jacob Smith 9/13/2019 Cosi 119a Homework 4.2
#using simple_action_server as template
#An action to tell the robot to move given an integer turning amount
# used from keys to twist example

print "RUNNING ACTION SERVER"
import rospy
import actionlib
from rossummary.msg import MoveAction, MoveGoal, MoveResult
from geometry_msgs.msg import Twist
# Action Request Comes in
def do_move(goal):
    #Tell Robot to  move by turned amount
    t = Twist()
    t.angular.z =goal.turnGoal
    twist_pub.publish(t)
    #set turning results and say task suceeded
    result = MoveResult()
    result.turnResult=goal.turnGoal
    result.updatesSent=0
    print "I have been requested to do action"
    print goal.turnGoal
    print "and I did"
    print result.turnResult
    server.set_succeeded(result)


# Declare that we are a node
rospy.init_node('action_server')

# Declare that this node will handle actions
# When action requests come in, call do_timer method
server = actionlib.SimpleActionServer('move',MoveAction, do_move, False)

# Start it up
server.start()

# let me publish `cmd_vel` topic    
twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

# Wait until ^c
rospy.spin()

# Wait until ^c
rospy.spin()