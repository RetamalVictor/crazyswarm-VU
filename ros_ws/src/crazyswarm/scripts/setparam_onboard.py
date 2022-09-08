#!/usr/bin/env python
from pycrazyswarm import Crazyswarm
import sys

command = int(sys.argv[1])  # 1-->takeoff, 2-->terminate, 3-->flock, 4-->grad_follow, 5-->GoTo, 6-->Circle Formation
heading = int(sys.argv[2])  # 1-->Heading Control ON, 1-->Heading Control OFF
point = int(sys.argv[3])
num_cf = 6

if point == 1:
    g_x = 3.5
    g_y = 1.0
elif point == 2:
    g_x = 5.5
    g_y = 2.0
elif point == 3:
    g_x = 3.5
    g_y = 3.5
elif point == 4:
    g_x = 1.0
    g_y = 3.0
elif point == 5:
    g_x = 3.50
    g_y = 2.0

formation = 1  # 1-->Circle

cfs = dict()
Cswarm = Crazyswarm()
timeHelper = Cswarm.timeHelper
for i in range(0, num_cf):
    cfs[i] = Cswarm.allcfs.crazyflies[i]

if command == 1:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/if_takeoff", 1)
        timeHelper.sleep(0.1)

elif command == 2:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/if_terminate", 1)
        timeHelper.sleep(0.1)

elif command == 3:
    for cf in range(num_cf):
        print("here")
        cfs[cf].setParam("fmodes/fmode", 1)
        timeHelper.sleep(0.1)

elif command == 4:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/fmode", 2)
        timeHelper.sleep(0.1)

elif command == 5:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/fmode", 3)
        cfs[cf].setParam("fmodes/goal_x", g_x)
        cfs[cf].setParam("fmodes/goal_y", g_y)
        timeHelper.sleep(0.1)

elif command == 6:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/fmode", 4)
        cfs[cf].setParam("fmodes/goal_x", g_x)
        cfs[cf].setParam("fmodes/goal_y", g_y)
        timeHelper.sleep(0.1)

elif command == 7:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/fmode", 5)
        cfs[cf].setParam("fmodes/goal_x", g_x)
        cfs[cf].setParam("fmodes/goal_y", g_y)
        timeHelper.sleep(0.1)

elif command == 8:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/fmode", 6)
        cfs[cf].setParam("fmodes/goal_x", g_x)
        cfs[cf].setParam("fmodes/goal_y", g_y)
        timeHelper.sleep(0.1)

if heading == 1:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/if_heading", 1)
        timeHelper.sleep(0.1)
elif heading == 0:
    for cf in range(num_cf):
        cfs[cf].setParam("fmodes/if_heading", 0)
        timeHelper.sleep(0.1)