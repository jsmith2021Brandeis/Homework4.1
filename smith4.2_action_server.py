#! /usr/bin/env python
#using simple_action_server as template
print "running action server"
import rospy
import actionlib
from prrexamples.msg import SpinAction, SpinGoal, SpinrResult

# Action Request Comes in
def do_spin(goal):
    result = SpinResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = 0
    server.set_succeeded(result)

# Declare that we are a node
rospy.init_node('smith_action_server')

# Declare that this node will handle actions
# When action requests come in, call do_timer method
server = actionlib.SimpleActionServer('spin',SpinResult, do_spin, False)

# Start it up
server.start()

# Wait until ^c
rospy.spin()