
#!/bin/bash
#Jacob Smith 9/13/2019 COSI 119a jsmith2021@brandeis.edu
#Bash script to automatically log in to ROS robot

#Define how to start a new terminal and log in
NEW_TERMINAL="gnome-terminal --geometry 73x31+$WINDOWPOS+0 --  /bin/sh -c"
LOGIN="sshpass -p "ROSlab134" ssh -t -oStrictHostKeyChecking=no "roba@roba.dyn.brandeis.edu""
#create new terminal, log in, and run commands to start up robot
$NEW_TERMINAL "$LOGIN 'whoami; roscore;sleep 10'"
$NEW_TERMINAL "$LOGIN 'whoami; bu;sleep 10'"
#$NEW_TERMINAL "$LOGIN 'whoami; sleep 10;rostopic list;sleep 5;rosnode kill -a'"
$NEW_TERMINAL "$LOGIN 'whoami; rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  ;linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}';sleep 10;rosnode kill -a;logout"

#Close down all windows
sleep 20
pkill gnome-terminal-