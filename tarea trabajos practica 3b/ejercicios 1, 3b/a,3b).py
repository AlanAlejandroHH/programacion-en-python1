Alan Alejandro Herrera Huerta
#tarea 3b


import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6,2,100)
y=5-4*x-x**2
plt.plot(x,y,linewidth=3,color='g')
plt.legend()
plt.title('$F(x)=5-4x-x^2$')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
