
import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,500)
a=4  
m=12
n=25
x=(1+a*np.cos(n*theta))*np.cos(m*theta)
y=(1+a*np.cos(n*theta))*np.sin(m*theta)
z=a*np.sin(n*theta)
plt.ion()
plt.plot(x,y,lw=2)
