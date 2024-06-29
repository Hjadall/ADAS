# ACC_PID_Simulation
## Import Libararies

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
## Vehicle Class
class vehicle:
    def __init__ (self, initial_position, initial_speed):
        self.position = initial_position
        self.speed = initial_speed
    
    def update_position (self, acceleration, dt):
        self.speed = self.speed + acceleration *dt 
        self.position = self.position + self.speed *dt

        
## ACC Class
class ACC_Trip:

    def __init__ (self, kp, ki, kd, saftey_distance, velocity_target):

        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.saftey_distance = saftey_distance
        self.velocity_target = velocity_target
        self.previous_error = 0
        self.integral = 0
    
    def accleration_computing (self, distance, velocity, dt ): 

        # calculation of PID controller
        error = self.saftey_distance - distance

       
        if error <= 0:
         error = self.velocity_target - velocity

         self.kp = 0.5
         self.ki = 0.1
         self.kd = 0.05

         if error <= 0 :    

            return 0         
            

      
        
        self.integral = self.integral + (error + self.previous_error)/2 *dt
        derivative =  (error - self.previous_error)/dt
        self.previous_error = error 
        
        return self.kp* error + self.ki * self.integral + self.kd* derivative
     

## simulation parameters

simulation_time = 60
dt = 0.1
steps = int(simulation_time/dt)
## vehicles definition
# we have 2 vehicles a lead and a following

lead_vehicle = vehicle(20, 60) #speed in m/s
following_vehicle = vehicle(15,60) #speed in m/s

## ACC definition
# acc = ACC_Trip (-0.5, 0.1, 0.05, 10)
acc = ACC_Trip (-1, 0.1, 0.1, 10, 60)
#acc = ACC_Trip (-0.5, 0.1, 0.01, 10)

## arrays initiallization

lead_positions = []
following_positions = []
distances = []
following_velocity = []
following_acceleration = []
errortoprint = []


np.set_printoptions(precision=2)

for i in range(steps):
    distance = lead_vehicle.position - following_vehicle.position
    acceleration = acc.accleration_computing(distance ,following_vehicle.speed, dt)
    lead_vehicle.update_position(0, dt)
    following_vehicle.update_position(acceleration, dt)

    #append Data
    errortoprint.append (acc.previous_error)
    lead_positions.append(lead_vehicle.position)
    following_positions.append(following_vehicle.position)
    distances.append(distance)
    following_velocity.append(following_vehicle.speed)
    following_acceleration.append(acceleration)
    
print(distances)
print(following_acceleration)
print(following_velocity)
## Plot Results

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,1)

fig_1 = fig.add_subplot(gs[0,0])
plt.plot(np.arange(steps) * dt, lead_positions, label='Lead Vehicle Position')
plt.plot(np.arange(steps) * dt, following_positions, label='Following Vehicle Position')
plt.plot(np.arange(steps) * dt, distances, label='Distance Between Vehicles')
plt.xlabel('Time (s)')
plt.ylabel('Position (m) / Distance (m)')
plt.legend()
plt.title('Adaptive Cruise Control Simulation (Trapezoidal Integral)')
plt.grid(True)

fig_2 = fig.add_subplot(gs[1, 0])
plt.plot(np.arange(steps) * dt, following_velocity, label='Following Vehicle Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.grid(True)

fig_3 = fig.add_subplot(gs[2, 0])
plt.plot(np.arange(steps) * dt, following_acceleration, label='Following Vehicle Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.legend()
plt.grid(True)

plt.show()

