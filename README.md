# mmtbot

**M**ulti-**M**odal **T**est **B**ot (mmtbot) is a conceptual robot designed to test advanced calibration methodologies. The system contains the following sensors:

- **3dlidar** - A 3D LiDAR mounted on a tripod
- **world_camera** - An RGB-D camera mounted on the same tripod
- **hand_camera** - A second RGB-D camera mounted on the manipulator's end effector link

![mmtbot_gazebo](docs/gazebo.png)

![mmtbot_gazebo](docs/rviz.png)

# Installation

https://github.com/iris-ua/iris_ur10e/tree/noetic-devel

https://github.com/iris-ua/iris_ur10e_calibration/tree/noetic-devel

# Running the simulation to collect a bag file:

To run the system with simulation use:

    roslaunch mmtbot_bringup sim.launch gui:=true

Setting gui:=false will not launch gazebo which will make it faster.

Then you can record a bag file

    roslaunch mmtbot_bringup record.launch bag:=/home/mike/Desktop/mmtbot.bag

After having a bagfile now you just calibrate as you did before with any atom robot calibration procedure.

# Using test Bagfiles and Datasets 

To test you can use the bag file at:

https://drive.google.com/file/d/1mnzHkKeuQmjPCMyq_iGF67GByIx4sQk-/view?usp=sharing

and the dataset at:

https://drive.google.com/file/d/1Vr_mSSZU24fMTfJdCmcwA9dumiedEbl2/view?usp=sharing

