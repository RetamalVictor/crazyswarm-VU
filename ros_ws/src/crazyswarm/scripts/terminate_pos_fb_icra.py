import rospy
from std_msgs.msg import UInt8

pub = rospy.Publisher('/term', UInt8, queue_size=1)
rospy.init_node('if_terminate_node', anonymous=True)
rate = rospy.Rate(10)

for i in range(10):
    pub.publish(1)
    rate.sleep()
