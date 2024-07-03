# Autonomous Vehicle Control Systems

## Description
This repository contains implementations of control systems for autonomous vehicles, focusing on two key aspects: Lane Changing Control and Adaptive Cruise Control (ACC). These systems utilize PID controllers to ensure smooth and safe vehicle operation.

## Repository Structure
- `Lateral_Controller/`: Contains the Lane Changing Control project.
- `ACC_PID/`: Contains the Adaptive Cruise Control project.

## Projects Overview

### Lane Changing Control
This project implements a lane-changing control system for autonomous vehicles using PID controllers to manage the lateral position and heading angle. The system ensures smooth and stable lane changes, even at higher speeds, using the bicycle model for vehicle dynamics.

#### Key Features
- PID control for lateral position and heading angle.
- Bicycle model for vehicle dynamics.
- Simulation and visualization of lane changing behavior.

### Adaptive Cruise Control (ACC)
This project implements an Adaptive Cruise Control system for autonomous vehicles using PID controllers to manage vehicle speed and maintain a safe distance from the vehicle ahead. The system adapts to changing traffic conditions to ensure smooth and safe driving.

#### Key Features
- PID control for vehicle speed and distance management.
- Simulation and visualization of ACC in various traffic scenarios.

### Future Work
For future iterations, consider implementing a Model Predictive Control (MPC) system. MPC offers advantages in handling nonlinear dynamics and constraints, potentially improving control accuracy and response times in complex driving scenarios.


### Usage
To run simulations:
```bash
cd ACC_PID
python acc_control.py
exit

### Future Work
For future iterations, consider implementing a Model Predictive Control (MPC) system. MPC offers advantages in handling nonlinear dynamics and constraints, potentially improving control accuracy and response times in complex driving scenarios.