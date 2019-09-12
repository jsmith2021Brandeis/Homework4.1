#!/usr/bin/env python
#using service server as example
# rosrun rosbook service_server.py
# rosservice call word_count 'one two three'
print "running fake nlp"
import rospy
from prrexamples.srv import Command,CommandResponce

#when user asks for a process message, pattern match it to a word and space,
# and return number if pattern matches
def verify_command(command):
    print("Responding to a request for: "+command.data)
    return CommandResponse(4)

# Declare a node
rospy.init_node('fake_nlp')

# Announce that we are a service
service = rospy.Service('fake_nlp',Command, verify_command)

# Wait until ^c or a service request
rospy.spin()