 import numpy as np
 import matplotlib.pyplot as plt
 
 x1=-10
 x2=100
 y1=-10
 y2=100
 plt.axis([x1,x2,y1,y2])
 
 plt.axis('on')
 plt.grid(True,color='fuchsia')
 plt.title('Doughnut')
 plt.xlabel('this is the x axis')
 plt.ylabel('this is the y axis')
 plt.plot([x,x],[0,10],linewidth=25,color=(.5,1,.2))
 plt.scatter(20,20,s=1000,color='b',alpha=1)
 plt.arrow(20,20,10,0,linewidth=5,head_length=4,head_width=2,color='r')
 plt.plot([-5,5],[-5,-5],linewidth=2,color='k')
 plt.plot([5,5],[-5,5],linewidth=2,color='k')
 plt.plot([5,-5],[5,5],linewidth=2,color='k')
 plt.plot([-5,-5],[5,-5],linewidth=2,color='k')
 plt.plot([40,100],[30,30],linewidth=10,color='g',linestyle=':')
 r=10
 alpha1=radians(10)
 alpha2=radians(360)
 dalpha=radians(20)
 xc=50
 yc=50
 plt.scatter(xc,yc,s=100,color='fuchsia')
 for alpha in np.arange(alpha1,alpha2,dalpha):
     x=xc+r*cos(alpha)
     y=yc+r*sin(alpha)
     plt.scatter(x,y,s=5,color='k')
 plt.show()
