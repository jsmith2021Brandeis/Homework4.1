
#work area#!/bin/bash

#Jacob SMith 9/13/2019 COSI 119a jsmith2021@brandeis.edu
#Bash script to automatically log in to ROS robot
#kill all terminal windows so the terminal ids start at 0

#get the terminal window and store in a variable
#terminalNum=$(tty | cut -d'/' -f4)
#echo $terminalNum
#sleepTime=1
#sleep $sleepTime
#log in and launch ros core i new window (othewise execution stops)

#work area
###########################################33333333

#=letter_of_alphabet   # Variable "a" holds the name of another variable.
#letter_of_alphabet=z
echo "START TEST"
num=10
a="$num"
echo $a
num=20
#eval a=$a
eval a='$'$a
echo $num
echo "END TEST"
sleep 100
# Direct reference.
echo "a = $a"          # a = letter_of_alphabet

# Indirect reference.
eval a=\$$a
# ^^^        Forcing an eval(uation), and ...
#        ^   Escaping the first $ ...
# ------------------------------------------------------------------------
# The 'eval' forces an update of $a, sets it to the updated value of \$$a.
# So, we see why 'eval' so often shows up in indirect reference notation.
# ------------------------------------------------------------------------
echo "Now a = $a"    # Now a = z

echo

=letter_of_alphabet   # Variable "a" holds the name of another variable.
letter_of_alphabet=z

echo

# Direct reference.
echo "a = $a"          # a = letter_of_alphabet

# Indirect reference.
  eval a=\$$a
# ^^^        Forcing an eval(uation), and ...
#        ^   Escaping the first $ ...
# ------------------------------------------------------------------------
# The 'eval' forces an update of $a, sets it to the updated value of \$$a.
# So, we see why 'eval' so often shows up in indirect reference notation.
# ------------------------------------------------------------------------
  echo "Now a = $a"    # Now a = z

echo
######################################################################
sleep 100


#script to start a new window, login, and user 
WINDOWPOS=0
NEW_TERMINAL="gnome-terminal --geometry 73x31+$WINDOWPOS+0 --  /bin/sh -c"
LOGIN="sshpass -p "ROSlab134" ssh -t -oStrictHostKeyChecking=no "robb@robb.dyn.brandeis.edu""
$NEW_TERMINAL "$LOGIN 'whoami; roscore';sleep 10"
WINDOWPOS=$((WINDOWPOS+100))
echo $WINDOWPOS
echo $NEW_TERMINAL
$NEW_TERMINAL "$LOGIN 'whoami; roscore';sleep 10"



#$LOGIN 'roscore'
#echo $test
#gnome-terminal --geometry 73x31+0+0 --  /bin/sh -c "$LOGIN 'bu;sleep 10'"

#good



#$val='bu;sleep 10'
#echo "done"
#$NEW_TERMINAL "$LOGIN $val"

#"sshpass -p "ROSlab134" ssh -t -oStrictHostKeyChecking=no "robb@robb.dyn.brandeis.edu"" 
#sshpass -p "ROSlab134" ssh -t -oStrictHostKeyChecking=no "robb@robb.dyn.brandeis.edu" 'roscore'
#!/bin/bash
 
# Declare an array of string with type
#declare -a StringArray=("'bu;sleep 10'" "'bu;sleep 10'")
 
# Iterate the string array using for loop
#for val in ${StringArray[@]}; do
#   echo $val
#   $NEW_TERMINAL "$LOGIN $val"
#done

#LOGIN="sshpass -p "ROSlab134" ssho robb@rbb.dyn.brandeis.edu"
#gnome-terminal --geometry 73x31+0+0 --  /bin/sh -c "$LOGIN;roscore"#;$LOGIN
#sleep $sleepTime
#log in and launch bu in new window
#gnome-terminal --geometry 73x31+200+0 -- /bin/sh -c "$LOGIN;bu"#$LOGIN
#sleep $sleepTime
#log in and view list of topics in new window
#gnome-terminal --geometry 73x31+400+0 -- /bin/sh -c "$LOGIN;rostopic list"#$LOGIN
#sleep $sleepTime

#send command to terminal number
#ls > /dev/pts/0
#write y tty2
sleep 20
# rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  ;linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
#rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  \'{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}\';
#sleep 5;
#rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  \'{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}\';
#rosnode kill -a;
#logout;
pkill gnome-terminal-
#sleep 10

#links:shutdown ros https://answers.ros.org/question/242098/how-to-shutdown-all-nodes/
#publish cmd_vel https://answers.ros.org/question/218818/how-to-publish-a-ros-msg-on-linux-terminal/
#escape characters in bash https://linuxhint.com/bash_escape_quotes/
#expect commmand to automate ssh login, I didnt get to work https://www.linuxquestions.org/questions/linux-general-1/automatically-passing-an-answer-to-a-command%27s-prompt-918926/
#ssh pass aut log in https://www.cyberciti.biz/faq/noninteractive-shell-script-ssh-password-provider/
#agreeing to commnad line liscence https://askubuntu.com/questions/78235/how-do-i-accept-an-agreement-in-terminal
#sending remote command to terminal (Edward Torvalds Answer) https://unix.stackexchange.com/questions/261531/how-to-send-output-from-one-terminal-to-another-without-making-any-new-pipe-or-f
#get terminal number https://unix.stackexchange.com/questions/261531/how-to-send-output-from-one-terminal-to-another-without-making-any-new-pipe-or-f
#store command output in variable https://askubuntu.com/questions/323162/how-do-i-assign-the-output-of-a-command-to-a-variable
#parse a string https://unix.stackexchange.com/questions/312280/split-string-by-delimiter-and-get-n-th-element

#https://unix.stackexchange.com/questions/135108/sending-message-from-one-terminal-user-to-another-user/135111

#sshpass -p "$ROSlab134" ssh -t -oStrictHostKeyChecking=no "robb@rbb.dyn.brandeis.edu" 'roscore'
