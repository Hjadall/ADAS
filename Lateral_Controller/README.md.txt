# Lane Changing Control

## Description
This project implements a lane-changing control system for autonomous vehicles using PID controllers for lateral position and heading angle. The system ensures smooth and stable lane changes even at high speeds.

## Features
- **PID Control for Lateral Position**: Adjusts the vehicle's lateral position to reach the desired lane.
- **PID Control for Heading Angle**: Adjusts the vehicle's heading angle to maintain the correct orientation during lane changes.
- **Simulation**: Simulates the lane change process and visualizes the vehicle's trajectory, steering angle, and heading angle over time.

## Installation
Ensure you have Python installed. You will also need `numpy` and `matplotlib` for the simulations.

Install the required libraries using pip:
```bash
pip install numpy matplotlib


## Code Structure

lane_changing_control.py: The main script that runs the lane-changing simulation.
Vehicle: Class representing the vehicle's state and behavior.
LateralPositionController: Class implementing the PID controller for lateral position.
HeadingAngleController: Class implementing the PID controller for heading angle.
Example Output
The simulation will generate plots showing:

The vehicle's trajectory over time.
The steering angle over time.
The heading angle over time.
Future Work
Integration with real-time sensor data.
Implementation of more advanced control algorithms (e.g., Model Predictive Control).
