# Autonomous Vehicle Control Systems

## Description
This repository contains implementations of control systems for autonomous vehicles, focusing on two key aspects: Lane Changing Control and Adaptive Cruise Control (ACC). These systems utilize PID controllers to ensure smooth and safe vehicle operation.

## Repository Structure
- `Lateral_Controller/`: Contains the Lane Changing Control project.
- `ACC_PID/`: Contains the Adaptive Cruise Control project.

## Projects Overview

### Lane Changing Control
This project implements a lane-changing control system for autonomous vehicles using PID controllers to manage the lateral position and heading angle. The system ensures smooth and stable lane changes, even at higher speeds. It uses the bicycle model for vehicle dynamics.

#### Key Features
- PID control for lateral position and heading angle.
- Use of the bicycle model for vehicle dynamics.
- Simulation of lane changing.
- Visualization of vehicle trajectory, steering angle, and heading angle.

  ### Adaptive Cruise Control (ACC)
This project implements an Adaptive Cruise Control system for autonomous vehicles using PID controllers to manage the vehicle's speed and maintain a safe distance from the vehicle ahead. The system adapts to changing traffic conditions to ensure smooth and safe driving.

#### Key Features
- PID control for vehicle speed and distance management.
- Simulation of adaptive cruise control in various traffic scenarios.
- Visualization of vehicle speed, following distance, and acceleration.

#### Usage
Navigate to the `Lateral_Controller` or `ACC_PID` directory and run the simulation script
```bash
#### Usage
Navigate to the `ACC_PID` directory and run the simulation script:
```bash
cd ACC_PID
python acc_control.py
