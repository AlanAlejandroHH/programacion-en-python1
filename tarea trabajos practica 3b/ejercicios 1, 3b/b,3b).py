#Alan Alejandro Herrera Huerta

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,5,80)
y=2*x**2-8*x-11
plt.plot(x,y,linewidth=5,color='k')
plt.legend()
plt.title('$G(x)=2x^2-8x-11$')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
