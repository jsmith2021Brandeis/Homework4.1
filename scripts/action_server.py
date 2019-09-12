#! /usr/bin/env python
#using simple_action_server as template
print "running action server"
import rospy
import actionlib

# Action Request Comes in
def do_move(goal):
    result = moveResult()
    print "I have been requested to do action"
    return 


# Declare that we are a node
rospy.init_node('action_server')

# Declare that this node will handle actions
# When action requests come in, call do_timer method
server = actionlib.SimpleActionServer('move',moveResult, do_move, False)

# Start it up
server.start()

# Wait until ^c
rospy.spin()