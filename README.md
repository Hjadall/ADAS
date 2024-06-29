# Autonomous Vehicle Control Systems

## Description
This repository contains implementations of control systems for autonomous vehicles, focusing on two key aspects: Lane Changing Control and Adaptive Cruise Control (ACC). These systems utilize PID controllers to ensure smooth and safe vehicle operation.

## Repository Structure
- `Lateral_Controller/`: Contains the Lane Changing Control project.
- `ACC_PID/`: Contains the Adaptive Cruise Control project.

## Projects Overview

### Lane Changing Control
This project implements a lane-changing control system for autonomous vehicles using PID controllers to manage the lateral position and heading angle. The system ensures smooth and stable lane changes, even at higher speeds.

#### Key Features
- PID control for lateral position and heading angle.
- Simulation of lane changing.
- Visualization of vehicle trajectory, steering angle, and heading angle.

#### Usage
Navigate to the `lane-changing-control` directory and run the simulation script:
```bash
cd lane-changing-control
python lane_changing_control.py
