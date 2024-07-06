import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Vehicle:
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        
        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        
        self.sample_time = 0.01

        
    def position_update (self, v, w):
        self.xc = self.xc + v * np.cos(self.beta + self.theta) * self.sample_time
        self.yc = self.yc + v * np.sin(self.beta + self.theta) * self.sample_time
        self.theta = self.theta + (v * np.cos(self.beta) * np.tan(self.delta)) / self.L * self.sample_time
        self.delta = self.delta + w * self.sample_time
        self.beta = np.arctan(self.lr * np.tan(self.delta) / self.L)
        
        if self.delta > self.w_max:
            self.delta = self.w_max
        elif self.delta < -self.w_max:
            self.delta = -self.w_max
        pass

    
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0


sample_time = 0.01
time_end = 30
model = Vehicle()
model.reset()

t_data = np.arange(0,time_end,sample_time)
x_data = np.zeros_like(t_data)
y_data = np.zeros_like(t_data)
v_data = np.zeros_like(t_data)
w_data = np.zeros_like(t_data)



radius = 8

delta = np.arctan(model.L/radius)

v_data[:]=  2*(2*np.pi*8/30)

w = v_data[0]* np.tan(delta)/model.L

print(w)



for i in range (t_data.shape[0]):
    x_data[i] = model.xc
    y_data[i] = model.yc
    
    if i <= (1/8)*t_data.shape[0]:
        
        if model.delta < delta:
            model.position_update(v_data[i], w)
            
        else:
            model.position_update(v_data[i], 0)
        
    elif i<= (5/8)* t_data.shape[0]:
        if model.delta > - delta:
            model.position_update(v_data[i], -w)
        else:
            model.position_update(v_data[i], 0)
    else:
        if model.delta < delta:
            model.position_update(v_data[i], w)
        else:
            model.position_update(v_data[i], 0)
        
            
        

plt.axis('equal')
plt.plot(x_data, y_data)
plt.show()
