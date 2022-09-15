![Crazyswarm ROS CI](https://github.com/USC-ACTLab/crazyswarm/workflows/Crazyswarm%20ROS%20CI/badge.svg)
![Sim-Only Conda CI](https://github.com/USC-ACTLab/crazyswarm/workflows/Sim-Only%20Conda%20CI/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/crazyswarm/badge/?version=latest)](https://crazyswarm.readthedocs.io/en/latest/?badge=latest)

# Crazyswarm
## *Onboard Controller Design for Nano UAV Swarm in Operator-Guided Collective Behaviours *
A Large Nano-Quadcopter Swarm.

Please, follow the oficial crazyswarm installation and connection to crazyflies. 
Modified files for the paper are included in ```crazyswarm-VU/ros_ws/src/crazyswarm/scripts``` and  ```crazyswarm-VU/ros_ws/src/crazyswarm/launch```.
The files included are:
- ```Tugay_hover.launch``` including the launch parameters and the initialization of logging functionality.
- ```icra_play_log.py``` file is used to replay experiments with the logged data. It will generate a dynamic animation to visualize current positions and trayectories during the experiment.
- ```pos_fb_icra_newplot.py``` extracts the real crazflie positions from the ros topics. It also visualizes the position in real time with a dynamic animation. 
- ```set_param.py``` is the main mission control script. It allows the operator to initiate, terminate and set different missions in real time during the flight.
- ```terminate_fb.py``` script to terminate the connection.

The documentation is available here: http://crazyswarm.readthedocs.io/en/latest/.

## Troubleshooting
Please start a [Discussion](https://github.com/USC-ACTLab/crazyswarm/discussions) for...

- Getting Crazyswarm to work with your hardware setup.
- Advice on how to use the [Crazyswarm Python API](https://crazyswarm.readthedocs.io/en/latest/api.html) to achieve your goals.
- Rough ideas for a new feature.

Please open an [Issue](https://github.com/USC-ACTLab/crazyswarm/issues) if you believe that fixing your problem will involve a **change in the Crazyswarm source code**, rather than your own configuration files. For example...

- Bug reports.
- New feature proposals with details.

