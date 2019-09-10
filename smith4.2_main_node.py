#! /usr/bin/3.2/env python
#Jacob Smith 9/9/2019 Cosi 119a Homework 3.2
# used topic_subscriber as template
#subscribes to command from console
import rospy
from std_msgs.msg import String
import sys
print "running main node"
# define function is called each time the message is published (by some other node)
def callback(msg):
    
    print (msg.data)
    rospy.wait_for_service('fake_nlp')

    # Get the method (service proxy)
    turn = rospy.ServiceProxy('fake_nlp', WordCount)
    print turn

    #publish the direction as a string
    #pub.publish(dirName)

# Make this into a ROS node.
rospy.init_node('smith_main_node')
sub = rospy.Subscriber('demo/command', String, callback)
rospy.spin()

#action client code

#! /usr/bin/env python
#print "running main node"
#import rospy
#import actionlib
#from prrexamples.msg import TimerAction, TimerGoal, TimerResult

# Declare the node
#rospy.init_node('timer_action_client')

# Get the method to talk to the action
#client = actionlib.SimpleActionClient('timer', TimerAction)

# Now just wait for it  to come up.
#client.wait_for_server()
#rospy.loginfo("Action server detected")

# Create the TimerGoal objet
#goal = TimerGoal()

# Set it up
#goal.time_to_wait = rospy.Duration.from_sec(5.0)

# And now tell the action to begin working on the goal
#client.send_goal(goal)

# Block until the action says the job is done
#client.wait_for_result()

# Print the result.
#rospy.loginfo('Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))