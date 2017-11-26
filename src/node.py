#!/usr/bin/env python

# Import ros
import rospy

# Import opencv
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_srvs.srv import Empty

#
class ImageToTopic:

    def __init__(self):
        rospy.init_node('image_to_topic')
        self.image_path = rospy.get_param('/image_loader/image_path')
        self.bridge = CvBridge()
        self.s = rospy.Service(
            'get_image', Empty, self.image_to_topic_server
            )
        self.pub = rospy.Publisher("image_loader", Image, queue_size=1)

    def image_to_topic_server(self,req):
        image = cv2.imread(self.image_path, 1)

        msg = self.bridge.cv2_to_imgmsg(image, "bgr8")
        self.pub.publish(msg)


if __name__ == "__main__":
    image_to_topic = ImageToTopic()
    rospy.spin()
