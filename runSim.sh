#Jacob smith COSI 119A 9/9/2019 Homework 3.2
#launches a simulation node
#roscd prrexamples
#!/bin/bash
cd ~/catkin_ws/src/prrexamples/scripts
chmod +x smith4.2_sim.py
#This sequence launches my smith file
python smith4.2_sim.py
rostopic list
rostopic echo counter -n 5 