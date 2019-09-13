
# COSI 119A Repository Jacob Smith Fall 2019

### Contains my homework for the course and serves as a backup

### Homework 4.2 ROSSUMMARY

#### 	**Overview**

###### 		4.1Script: A bash file that automatically launches ROSCORE, gazebo, and all of my python classes

###### 		action_server.py: This ROS Action receives a request to turn the robot by a certain amount and 	 				publishes a Twist message to move the robot.

###### 		console_node.py: This ROS node prompts the user to enter console input and publishes the 			input to a topic

###### 		fake_nlp.py: This ROS service parses user entered commands into an amount to turn the robot. 				If the command does not translate to an amount to turn, it prints an error message and 					turns 0

###### 		main_node.py: This ROS node handles communication with the other ROS objects and with 					gazebo. It subscribes to the console node, passes the command to the fake_nlp service, 					and requests the action server to move the robot

![Demonstration of ROS objects](demo.gif)

### Other Code

​	The only code I used not included here are these convenience lines which let me create a shortcut to run 	the 4.1Script file

	Type: code ~/.bashrc#	
	add Path so I don't have to type Bash and start at that directory Jacob Smith 		9/11/2019`
	`curDir='/home/robotics/Documents/Homework4.2/catkin_ws/src/rossummary/scripts'export PATH="$PATH:"$curDircd $curDir``
### Note

​		I used the class prrexamples as a template for the package and node/service/action layout of this 			assignment. I also searched the internet for solutions to errors and problems I was having, see links 			below.

#### Useful Links

Looping in bash script :

​	https://www.cyberciti.biz/faq/bash-loop-over-file/ 
Allow git merging: 

​	https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase 
Get current directory: 

​	https://www.rapidtables.com/code/linux/linux-current-directory.html
Open new terminal window:

​	https://unix.stackexchange.com/questions/373186/ 
Kill terminal windows by name:

​	 https://stackoverflow.com/questions/160924/how-can-i-kill-a-process-by-na	 
Copy files from one location to another:

​	https://stackoverflow.com/questions/14371039/copy-all-files-in-a-directory-with-a-particular-string-in-the-filename-to-differ

 Avoid typing bash to run a script
 	https://stackabuse.com/how-to-permanently-set-path-in-linux/

Start bash to run in correct directory

​	https://askubuntu.com/questions/332062/setting-default-path-when-opening-a-terminal-session

Store path in bash variable

​	https://stackoverflow.com/questions/8950695/shell-scripting-using-a-variable-to-define-a-path

Adding variable to string

​	http://www.compciv.org/topics/bash/variables-and-substitution/

Doing arithmetic with variable

​	https://unix.stackexchange.com/questions/55069/how-to-add-arithmetic-variables-in-a-script

Set window of new terminal

​	https://unix.stackexchange.com/questions/48984/how-can-i-set-the-position-that-terminal-opens-at

`Set default path`

	https://askubuntu.com/questions/332062/setting-default-path-when-opening-a-terminal-session
	 	https://stackabuse.com/how-to-permanently-set-path-in-linux

Check if String represents an integer

​	https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except

Convert String to int

​	https://guide.freecodecamp.org/python/how-to-convert-strings-into-integers-in-python/

Set Robot Type in Gazebo NathanelGandi, set MODEL to burger instead of whatthey where doing

​	https://github.com/turtlebot/turtlebot/issues/236

Launch Gazbo 20:21 in video:

​	https://www.youtube.com/watch?v=9U6GDonGFHw

**-Jacob Smith** jsmith2021@brandeis.edu