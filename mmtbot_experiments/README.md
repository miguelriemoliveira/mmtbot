# MMTBOT Experiments

This is to store several experiments of the [mmtbot robotic system](https://github.com/miguelriemoliveira/mmtbot).

## Experiments 

1. Initial estimate vs error

## Input Data

### Bagfiles

| Bagfile | Link |
| -------------- | :----------: |
11_03_2021.bag | [download](https://drive.google.com/file/d/1jkTlIhdSJ_TTkvIu6U-6j6kLHGSzQUo6/view?usp=sharing)

### Datasets

| Dataset | Link |
| -------------- | :----------: |
train_dataset | [download](https://drive.google.com/drive/folders/13PcP5iHk8gDlB-ghH2vwQ4iIt2crny0L?usp=sharing)

### How to use

Open mmtbot analysis.ipynb on Jupyter.
If you want to generate commands for the batch execution run the cell "Create commands for batch execution" with the lines 

```
total=50
distances=np.linspace(0,0.75,total)
angles=np.linspace(0,0.75,total)
```

costumized to the experiments you want to performe. This will generate a txt file with the commands you should copy to the batch execution file.

If you just want to evaluate your results, start running the cells from "Create vectors with sensors errors and execution time". This will create vectors with the time and calibration errors for the LiDAR, world camera and hand camera, and then will create 3D plots with the calibration errors. 

# Contributors

* Daniela Rato - University of Aveiro
* Miguel Riem Oliveira - University of Aveiro

