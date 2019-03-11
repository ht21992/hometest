import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,color="blue",label="Sin")
plt.plot(x,z,color="red",label="Cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot of sin and cos from 0 to 4π")
plt.legend()
plt.show()
