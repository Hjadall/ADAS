# Kinematic Bicycle Model for ADAS

## Overview
This repository contains a Python implementation of the kinematic bicycle model designed for ADAS (Advanced Driver Assistance Systems) applications. The project demonstrates trajectory following using the kinematic bicycle model.

## Features
- Implementation of the kinematic bicycle model
- Trajectory following for a figure-8 path
- Visualization of vehicle path, steering angle, and heading angle

## Getting Started

### Prerequisites
- Python 3.x
- numpy
- matplotlib

### Installation
Clone this repository:
git clone https://github.com/your-username/adas-kinematic-bicycle-model.git


### Project Structure
- `main.py`: Main script for running the simulation
- `vehicle.py`: Contains the `Vehicle` class implementing the kinematic model
- `plots.py`: Utility for plotting the results

## Detailed Explanation

### Kinematic Bicycle Model
The kinematic bicycle model is used to simulate the motion of a vehicle. The model equations are:

\[
\begin{align*}
\dot{x}_c &= v \cos{(\theta + \beta)} \\
\dot{y}_c &= v \sin{(\theta + \beta)} \\
\dot{\theta} &= \frac{v \cos{\beta} \tan{\delta}}{L} \\
\dot{\delta} &= \omega \\
\beta &= \tan^{-1}\left(\frac{l_r \tan{\delta}}{L}\right)
\end{align*}
\]

where:
- \( v \) is the vehicle speed
- \( \omega \) is the steering angle rate
- \( L \) is the wheelbase
- \( l_r \) is the distance from the rear axle to the center of mass
- \( \delta \) is the steering angle
- \( \beta \) is the slip angle

### Trajectory Following
The vehicle is driven in a figure-8 trajectory using speed \( v \) and steering angle rate \( \omega \) inputs. The speed is maintained constant, and the steering angle is adjusted to follow the desired path.

## Results
The following plots show the vehicle path, steering angle, and heading angle during the simulation:

![Vehicle Path](figures/vehicle_path.png)
![Steering Angle](figures/steering_angle.png)
![Heading Angle](figures/heading_angle.png)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
This is an Assignment that have been given in the Self-Driving car specialization on Coursera
