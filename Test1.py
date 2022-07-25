#!/usr/bin/env python



# A very basic TurtleBot script that moves TurtleBot forward indefinitely. Press CTRL + C to stop.  To run:
# On TurtleBot:
# roslaunch turtlebot_bringup minimal.launch
# On work station:
# python goforward.py

from controller import *
import rospy 
import time
from geometry_msgs.msg import Twist
from array import *

class Test1():
    def __init__(self):
        # initiliaze
        rospy.init_node('Test1', anonymous=False)

	# tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c
        rospy.on_shutdown(self.shutdown)

	# Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/odom',Odometry,self.callback)


	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(10)

        # Twist is a datatype for velocity
        move_cmd = Twist()
	# let's go forward at 0.2 m/s
        #move_cmd.linear.x = 0.20
	# let's turn at 0 radians/s
        #move_cmd.angular.z = 0



        controlist = [[0.2, 0], 
                      [0.3, 0],
                      [0.2, 0],
                      [0.4, 0],
                      [0.2, 0],
                      [0.2, 0],
                      [0.4, 0],
                      [0.2, 0],
                      [0.3, 0],
                      [0.2, 0],
                      [0.2, 0]]

        #counter = 0
        #interv = 10  #maximum time
        #wait = 15    #waiting time
        con_counter = 0
	# as long as you haven't ctrl + c keeping doing...
        start = time.time()
        while not rospy.is_shutdown():
            if con_counter<len(controlist)-1:
                #if counter < interv:   
	              #publish the velocity
                move_cmd.linear.x = controlist[con_counter][0]  #线速度
                move_cmd.angular.z = controlist[con_counter][1] #角速度   跑1s 2s
                self.cmd_vel.publish(move_cmd) #told the robot to move in this speed and direction

                   #rospy.loginfo("Forward")
                '''
                elif counter>= interv and counter<wait:
                  move_cmd.linear.x = 0.00
                  move_cmd.angular.z = 0
                  self.cmd_vel.publish(move_cmd)
                  #rospy.loginfo("Stop")
                
        else:
                  #reset time counter
                  counter = -1
                  #move to the next control input
                  con_counter += 1
                  '''

                #update the time counter
                #time.sleep()
                end = time.time()
                if end-start == 1:   
                        con_counter += 1
                        start = end

            #all comands from controllist have been executed
            '''
            else:
              move_cmd.linear.x = 0.00
              move_cmd.angular.z = 0
              self.cmd_vel.publish(move_cmd)   #to stop
              '''
              
            r.sleep()


    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
    def call_back(self):
        global x,y
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        #q1 = data.pose.pose.orientation.x
        #q2 = data.pose.pose.orientation.y
        #q3 = data.pose.pose.orientation.z
        #q4 = data.pose.pose.orientation.w
        #print(msg.pose.pose) ##忘记怎么写
        print("our x location is ",x, " our y location is ", y)

if __name__ == '__main__':
    try:
        Test1()
        if 5>= x>=4.9 and 5>= y >= 4.9 :
            print("robot arrivied")
        else:
            print("not arrivied")

    except:
        rospy.loginfo("GoForward node terminated.")