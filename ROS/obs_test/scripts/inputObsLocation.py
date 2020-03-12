#!/usr/bin/env python

# Siemens AG, 2018
# Author: Berkay Alp Cakal (berkay_alp.cakal.ct@siemens.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# <http://www.apache.org/licenses/LICENSE-2.0>.
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy
import numpy

from geometry_msgs.msg import Point, Pose, Quaternion
from std_msgs.msg import String
from Xlib import display
from Xlib.ext import randr

def getViconData():
	return([0])

def calculateTransform(ref, vic):
	print(ref)
    
def inputObsLocation():
	# initialize node
	rospy.init_node('calibrate', anonymous = True)

	#### Setup obsLocation Publisher 
	rate = rospy.Rate(10) # 10hz

	#Transform Poses
	refTransforms = []
	viconTransforms = []


	nextRefPublisher = rospy.Publisher("/sendRef", String, queue_size = 5)
	endRefPublisher = rospy.Publisher("/endRef", String, queue_size = 5)

	while not rospy.is_shutdown():	
		print("waiting")
		rospy.wait_for_message("/startCal", String)
		print("started calibration")
		msg = String("next")
		print("on to next")	
		nextRefPublisher.publish(msg)

		while(len(refTransforms) < 10):
			print("waiting for next")
			refTransforms.append(rospy.wait_for_message("nextTransform", Pose))
			viconTransforms.append(getViconData())
			print("recieved")
		endRefPublisher.publish(msg)
		calculateTransform(refTransforms, viconTransforms)

		#### Initialize point msg every loop
		#msg.x = 0.0
		#msg.y = 0.0
		#msg.z = 0.0
		
		#### Prompt User for Obs Location
		#msg.x = float(input("Please Enter The X Position of the Obstacle: "))
		#msg.y = float(input("Please Enter The Y Position of the Obstacle: "))
		#msg.z = float(input("Please Enter The Z Position of the Obstacle: "))
		


		#### Publish msg
		#rospy.loginfo([pos_x, pos_y])
		#obsLocationPublisher.publish(msg)
		#rate.sleep()


if __name__ == '__main__':
	inputObsLocation()
