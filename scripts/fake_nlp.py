#!/usr/bin/env python
#Jacob Smith 9/13/2019 Cosi 119a Homework 4.2
#using service server as example
#A service to parse a user entered command into amount to turn
print "RUNNING FAKE NLP"
import rospy
from std_msgs.msg import Int32,String
from rossummary.srv import fakeNLP, fakeNLPResponse #error on import

#when user asks for a process message, pattern match it to a word and space,
# and return number if pattern matches
def parse_command(request):
    print("Responding to a request for: "+request.message)
    #split the message by spaces
    sentence=request.message.split(" ")
    #store the last element
    number=sentence[len(sentence)-1]
    #if last element is a number, return it
    if representsInt(number):
        return  int(number)
    #otherwise, delcare error and return 0
    else:
        print "error, you didn't type a number"
        return 0

#Hlper method to check if string represents an integer, see readme for link
def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# Declare a node
rospy.init_node('service_server')

# Announce that we are a service
service = rospy.Service('fake_nlp',fakeNLP, parse_command)

# Wait until ^c or a service request
rospy.spin()
