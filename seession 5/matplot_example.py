import numpy as np
import  matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
k=np.sinc(x)
j=np.tan(x)
fig=plt.figure()
fig.suptitle("Trigonometric Functions")
ax=fig.add_subplot(221)
ax1=fig.add_subplot(222)
ax2=fig.add_subplot(223)
ax3=fig.add_subplot(224)
ax.plot(x,y,color="blue",label="Sin")
ax1.plot(x,z,color="red",label="Cos")
ax2.plot(x,k,color="yellow",label="sinc")
ax3.plot(x,j,color="black",label="tan")
ax3.set_xlim(0,12)
fig.legend()
#plt.savefig("Trigonometric Functions.png")
#from matplotlib.backends.backend_pdf import PdfPages
#pp=PdfPages("Trigonometric Functions.pdf")
#pp.savefig()
#pp.close()
plt.show()
