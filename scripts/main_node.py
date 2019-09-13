#! /usr/bin/3.2/env python
#Jacob Smith 9/9/2019 Cosi 119a Homework 3.2
# used topic_subscriber as template
#Subscribes to console, sends command to fakeNLP for parsing, and asks Move action
#to move the robot by that amount
import rospy
#import actionLib
from std_msgs.msg import String
import actionlib
from rossummary.srv import fakeNLP
from rossummary.msg import MoveAction, MoveGoal, MoveResult
import sys
print "RUNNING MAIN NODE"
# define function is called each time the message is published (by some other node)
def callback(msg):
    print"User entered into console"
    print (msg.data)
    #wait for service to start up
    rospy.wait_for_service('fake_nlp')
    print "Asking fake nlp service to parse"
    # Get the method (service proxy)
    parse_command= rospy.ServiceProxy('fake_nlp', fakeNLP)
    
    #call parse command of fakeNLP without storing it
    parsed=parse_command(msg.data)
    print "natural language processing found turn to be"
    print parsed.toTurn

    #et the method to talk to the action
    client = actionlib.SimpleActionClient('move', MoveAction)

    # Now just wait for it  to come up.
    client.wait_for_server()

    # Create the TimerGoal objet
    goal = MoveGoal()

    # Set it up
    #goal.time_to_wait = rospy.Duration.from_sec(5.0)
    goal.turnGoal=parsed.toTurn
    # And now tell the action to begin working on the goal
    client.send_goal(goal)
    client.wait_for_result()
    print "Move action returned result of"
    print client.get_result()

# Make this into a ROS node.
rospy.init_node('main_node')
sub = rospy.Subscriber('demo/command', String, callback)
rospy.spin()