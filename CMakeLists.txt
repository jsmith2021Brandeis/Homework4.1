cmake_minimum_required(VERSION 2.8.3)
project(rossummary)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  actionlib_msgs
)


## Generate messages in the 'msg' folder
add_message_files(
   FILES
  )

## Generate services in the 'srv' folder
add_service_files(
   FILES
   fakeNLP.srv
 )

## Generate actions in the 'action' folder
 add_action_files(
#   DIRECTORY action
   FILES Move.action
 )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   actionlib_msgs
   std_msgs
 )

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################


catkin_package(
  CATKIN_DEPENDS actionlib_msgs 
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


