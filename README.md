# mmtbot

Multi-modal test bot

# Installation

https://github.com/iris-ua/iris_ur10e

https://github.com/iris-ua/iris_ur10e_calibration

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

