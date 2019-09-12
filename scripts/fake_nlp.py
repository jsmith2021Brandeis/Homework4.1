#!/usr/bin/env python
#using service server as example
# rosrun rosbook service_server.py
# rosservice call word_count 'one two three'
print "running fake nlp"
import rospy
from rossummary.srv import fakeNLP,fakeNLPResponce

#when user asks for a process message, pattern match it to a word and space,
# and return number if pattern matches
def parse_command(request):
    print("Responding to a request for: "+command.message)
    return fakeNLPResponse(4)

# Declare a node
rospy.init_node('fake_nlp')

# Announce that we are a service
service = rospy.Service('fake_nlp',fakeNLP, parse_command)

# Wait until ^c or a service request
rospy.spin()