import rospy
import numpy

from geometry_msgs.msg import Point, Pose, Quaternion
from std_msgd.msg import String
from Xlib import display
from Xlib.ext import randr


#Transform Poses
refTransforms = []
viconTransforms = []

def getViconData():
	return([0])

def calculateTransform():
	print(refTransforms)
	refTransforms = []
	viconTransforms = []

def calibrateRefListener():
	# initialize node
	rospy.init_node('calibrateRef', anonymous = True)

	while not rospy.is_shutdown():

		nextRefPublisher = rospy.Publisher("sendRef", String, queue_size = 5)

		rospy.wait_for_message("startCal", String)
		print("started calibration")
		msg.data = "next"		

		while(len(refTransforms) < 10):
			nextRefPublisher.publish(msg)
			#refTransforms.append(rospy.wait_for_message("nextTrans", Pose))
			#viconTransforms.append(getViconData())
		calculateTransform()

		rospy.spin()

if __name__ == '__main__':
	calibrateRefListener()
