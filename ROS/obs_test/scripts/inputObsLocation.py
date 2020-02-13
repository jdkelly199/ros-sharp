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

from geometry_msgs.msg import Point
from Xlib import display
from Xlib.ext import randr
    
def inputObsLocation():
	# initialize node
	rospy.init_node('obsLocation', anonymous = True)

	#### Setup obsLocation Publisher 
   	obsLocationPublisher = rospy.Publisher("obs", Point, queue_size = 5)
	rate = rospy.Rate(10) # 10hz
	msg = Point()
	
	while not rospy.is_shutdown():
		#### Initialize point msg every loop
		msg.x = 0.0
		msg.y = 0.0
		msg.z = 0.0
		
		#### Prompt User for Obs Location
		msg.x = float(input("Please Enter The X Position of the Obstacle: "))
		msg.y = float(input("Please Enter The Y Position of the Obstacle: "))
		msg.z = float(input("Please Enter The Z Position of the Obstacle: "))
		


		#### Publish msg
		#rospy.loginfo([pos_x, pos_y])
		rospy.loginfo(msg)
		obsLocationPublisher.publish(msg)
		#rate.sleep()


if __name__ == '__main__':
	inputObsLocation()
