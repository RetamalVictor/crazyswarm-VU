![Crazyswarm ROS CI](https://github.com/USC-ACTLab/crazyswarm/workflows/Crazyswarm%20ROS%20CI/badge.svg)
![Sim-Only Conda CI](https://github.com/USC-ACTLab/crazyswarm/workflows/Sim-Only%20Conda%20CI/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/crazyswarm/badge/?version=latest)](https://crazyswarm.readthedocs.io/en/latest/?badge=latest)

# Crazyswarm
## *Onboard Controller Design for Nano UAV Swarm in Operator-Guided Collective Behaviours* 
[Flight videos of the experiments can be found on this link](https://www.youtube.com/watch?v=RA3ePt5Dhoo)

A Large Nano-Quadcopter Swarm.
Please, follow the oficial crazyswarm installation and connection to crazyflies. 
Modified files for the paper are included in ```crazyswarm-VU/ros_ws/src/crazyswarm/scripts``` and  ```crazyswarm-VU/ros_ws/src/crazyswarm/launch```.
The files included are:
- ```Tugay_hover.launch``` including the launch parameters and the initialization of logging functionality.
- ```icra_play_log.py``` file is used to replay experiments with the logged data. It will generate a dynamic animation to visualize current positions and trayectories during the experiment.
- ```pos_fb_icra_newplot.py``` extracts the real crazflie positions from the ros topics. It also visualizes the position in real time with a dynamic animation. 
- ```set_param.py``` is the main mission control script. It allows the operator to initiate, terminate and set different missions in real time during the flight.
- ```terminate_fb.py``` script to terminate the connection.

### Connection process
Before launching the experiments, please make sure the needed firmware is flashed in the crazyflies. More instructions [here](https://github.com/RetamalVictor/crazyflie-firmware-VU/tree/a17a530eadd8fc79359ada94f5e35742fdacfb49).

Modify the crazyflies ```id```, ```channel``` and ```type``` in the file ```crazyflies.yaml``` located at ```crazyswarm-VU/ros_ws/src/crazyswarm/launch``` to include the desired number of crazyflies for the swarm experiment. 

Make sure the terminals are sourced. ```$ source ./crazyswarm-VU/ros_ws/devel/setup.bash```

1. Open a terminal and launch the experiments with the command ```$ roslaunch crazyswarm tugay_hover.launch```. This will connect the crazyflies with the mission control.
2. Open a second terminal to initiate the experiment. To send mission commands, use the mission control scrip ```mission_control.py``` followed by the desired mission. E.g ```$ python3 mission_control.py 1 0``` to order the swarm to take off and start flocking autonomously. 
3. Modify or terminate the missions with the mission controller.
4. Data will be automatically logged in the ```/results``` folder.
5. To replay the visualization of an experiment run ```$ python3 replay_visualization.py <experiment_directory>```

### Mission control commands
| Command   | fmode                   | Mission                                                                                                 |
|-----------|-------------------------|---------------------------------------------------------------------------------------------------------|
| 1         | /takeoff                | The Swarm will take off and start flocking autonomously.                                                |
| 2         | /terminate              | The Swarm will land.                                                                                    |
| 3 0       | /flock_no_heading_align | The Swarm will flock without heading alignment.                                                         |
| 3 1       | /flock_heading_align    | The Swarm will flock with heading alingment.                                                            |
| 4         | /gradient_following     | The Swarm will find the max point of a gradient surface.                                                |
| 5 x y     | /go_to                  | The Swarm will go to the specified point (x,y).                                                         |
| 6         | /circle_formation       | The Swarm will maintain a circle formation around the point (2.5,2.5) in the global positioning system. |
| 7         | /reverse_circle         | The Agents of the swarm will exchange the positions in the circle formation by 180.                     |

The documentation is available here: http://crazyswarm.readthedocs.io/en/latest/.

## Troubleshooting
Please start a [Discussion](https://github.com/USC-ACTLab/crazyswarm/discussions) for...

- Getting Crazyswarm to work with your hardware setup.
- Advice on how to use the [Crazyswarm Python API](https://crazyswarm.readthedocs.io/en/latest/api.html) to achieve your goals.
- Rough ideas for a new feature.

Please open an [Issue](https://github.com/USC-ACTLab/crazyswarm/issues) if you believe that fixing your problem will involve a **change in the Crazyswarm source code**, rather than your own configuration files. For example...

- Bug reports.
- New feature proposals with details.

