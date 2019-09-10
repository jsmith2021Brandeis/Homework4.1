

# COSI 119A Repository Jacob Smith Fall 2019

### Contains my homework for the course and serves as a backup

### Homework 3.2

#### 	**Overview**

​					Demonstrates ROS nodes publishing and subscribing direction information. This could 					be used to interface a sensor which only knows numbers, an interpreter which can 					convert the numbers to human language, and a logger which can display the cleaned 					information:

​					![Demonstration of bash file and ROS nodes](/home/robotics/bin/Demo.gif)

#### 			Bash Script

​				<u>3.2Script</u> calls the client scripts in a new terminal window, closes the window after x

​					seconds, and copies all python files that start with smith to this repository

​				<u>RunMid.sh</u>,<u>RinPub.sh</u>, and <u>runSub.sh</u> all go to the correct directory and run their

​					respective node file

#### 			Python Nodes

​			<u>smith_topic _publisher</u> publishes a random integer representing the direction every second

​			<u>smith __topic __middle</u> converts that integer direction into a word, like Forward for 0 and 		

​				publishes that

​			<u>smith_topic _subscriber</u> prints the word integer

**-Jacob Smith** jsmith2021@brandeis.edu