#! /usr/bin/env python

import rospy
import tf
from std_msgs.msg import String
import time

"""Reference: http://answers.ros.org/question/33443/publish-marker/"""

class Find:

	def __init__(self):
		pub = rospy.Publisher('position', String, queue_size=10)
		orientationPub = rospy.Publisher('orientation', String, queue_size=10)	
		#orientationPub = rospy.Publisher('orientation', Marker)	
		rospy.init_node('find_copter')
		listener = tf.TransformListener()
		
		while not rospy.is_shutdown():
			try:
				start = time.time()
				#orientationTopic = Marker() 
				now = rospy.Time.now()
				listener.waitForTransform('usb_cam', 'ar_marker_0', now, rospy.Duration(2))
				position, orientation = listener.lookupTransform('usb_cam', 'ar_marker_0', now)

				# Publish Position as a ROS Topic
				positionTopic = str(position)				
				rospy.loginfo(positionTopic)
				pub.publish(positionTopic)

				# Publish Orientation as a ROS Topic
				orientationTopic = str(orientation)
				rospy.loginfo(orientationTopic)
				orientationPub.publish(orientationTopic)

				#print "position", position, "orientation", orientation
				print "x: ", position[0], "y: ", position[1], "z: ", position[2]
				print "orientation: ", orientation

				#check loop time
				end = time.time()
				elapsed = end-start
				print "time elapsed: ", elapsed #0.256s loop time

			except tf.Exception as e:
				rospy.logerr(e)
if __name__ == '__main__':
	Find()
