import rospy
from crazyswarm.msg import GenericLogData
from std_msgs.msg import UInt8
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import time

num_cf = 6


def cf_2_cb(pos_log_msg):
    global positions
    positions[0][0] = pos_log_msg.values[0]
    positions[1][0] = pos_log_msg.values[1]
    positions[2][0] = pos_log_msg.values[2]


cf2_cb = rospy.Subscriber("/cf2/log1", GenericLogData, cf_2_cb, queue_size=1)


if num_cf > 1:
    def cf_3_cb(pos_log_msg):
        global positions
        positions[0][1] = pos_log_msg.values[0]
        positions[1][1] = pos_log_msg.values[1]
        positions[2][1] = pos_log_msg.values[2]

    cf3_cb = rospy.Subscriber("/cf3/log1", GenericLogData, cf_3_cb, queue_size=1)


if num_cf > 2:
    def cf_4_cb(pos_log_msg):
        global positions
        positions[0][2] = pos_log_msg.values[0]
        positions[1][2] = pos_log_msg.values[1]
        positions[2][2] = pos_log_msg.values[2]

    cf4_cb = rospy.Subscriber("/cf4/log1", GenericLogData, cf_4_cb, queue_size=1)

if num_cf > 3:
    def cf_5_cb(pos_log_msg):
        global positions
        positions[0][3] = pos_log_msg.values[0]
        positions[1][3] = pos_log_msg.values[1]
        positions[2][3] = pos_log_msg.values[2]

    cf5_cb = rospy.Subscriber("/cf5/log1", GenericLogData, cf_5_cb, queue_size=1)

if num_cf > 4:
    def cf_6_cb(pos_log_msg):
        global positions
        positions[0][4] = pos_log_msg.values[0]
        positions[1][4] = pos_log_msg.values[1]
        positions[2][4] = pos_log_msg.values[2]

    cf6_cb = rospy.Subscriber("/cf6/log1", GenericLogData, cf_6_cb, queue_size=1)

if num_cf > 5:
    def cf_7_cb(pos_log_msg):
        global positions
        positions[0][5] = pos_log_msg.values[0]
        positions[1][5] = pos_log_msg.values[1]
        positions[2][5] = pos_log_msg.values[2]

    cf7_cb = rospy.Subscriber("/cf7/log1", GenericLogData, cf_7_cb, queue_size=1)


def terminate_cb_func(msg):
    global if_terminate
    if_terminate = True


global positions
global if_terminate
if_terminate = False
size_x = 6.5
size_y = 4.0

harita = sio.loadmat('/home/tugay/Environments/circle_4x65.mat')
harita = harita['I']

plt.ion()
plt.show()

positions = np.full([3, num_cf], 0.01)
rospy.init_node('icra_pos_fb_listener', anonymous=True)
terminate_cb = rospy.Subscriber("/term", UInt8, terminate_cb_func, queue_size=1)
r = rospy.Rate(1)

log_x = np.full([1,num_cf],0.00)
log_y = np.full([1,num_cf],0.00)
log_h = np.full([1,num_cf],0.00)

boundaryx = np.array([0., size_x, size_x, 0, 0])
boundaryy = np.array([0, 0., size_y, size_y, 0.])
boundaryx_1 = np.array([0.20, size_x-0.20, size_x-0.20, 0.20, 0.20])
boundaryy_1= np.array([0.20, 0.20, size_y-0.20, size_y-0.20, 0.20])
colors = ["red", "green", "blue", "orange", "purple", "black"]
colors_1=[ "red", "green", "blue", "orange", "purple", "black",
        "red", "green", "blue", "orange", "purple", "black",
        "red", "green", "blue", "orange", "purple", "black",
        "red", "green", "blue", "orange", "purple", "black",
        "red", "green", "blue", "orange", "purple", "black",
        "red", "green", "blue", "orange", "purple", "black"]
time.sleep(2)

while (not rospy.is_shutdown()) and (not if_terminate):
    cf_positions = positions
    plt.imshow(harita, extent=[0, size_x, 0, size_y])

    plt.axis([0, size_x, 0, size_y])
    plt.plot(boundaryx_1, boundaryy_1, c="black")
    plt.plot(boundaryx, boundaryy, c="red", linewidth=20, alpha=0.25,ls="--")
    plt.axis('off')
    plt.set_cmap("Greys_r")
    plt.scatter(cf_positions[0, :], cf_positions[1, :], c=colors, marker="X",s=135)
    plt.quiver(cf_positions[0], cf_positions[1], np.cos(cf_positions[2]), np.sin(cf_positions[2]))
    i = len(log_x)
    if i-10 > 0: plt.scatter(log_x[i-6:i,:], log_y[i-6:i, :], c=colors_1,s=14,marker="_")

    log_x = np.vstack([log_x, positions[0]])
    log_y = np.vstack([log_y, positions[1]])
    log_h = np.vstack([log_h, positions[2]])

    plt.draw()
    plt.pause(0.000001)
    plt.clf()
    # print(if_terminate)

    r.sleep()

sio.savemat('/home/tugay/icra_results/log_x.mat', {'x':log_x})
sio.savemat('/home/tugay/icra_results/log_y.mat', {'y':log_y})
sio.savemat('/home/tugay/icra_results/log_h.mat', {'h':log_h})
