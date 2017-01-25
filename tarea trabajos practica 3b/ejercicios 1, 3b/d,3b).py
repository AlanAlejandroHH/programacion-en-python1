#Alan Alejandro Herrera Huerta

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,24,100)
h=math.e**(-1*t)
plt.plot(t,h,linewidth=5,color='r')
plt.legend()
plt.title('$H(t)=e^(-2t)sen(2t)$')
plt.xlabel('Horas')
plt.ylabel('Kilometros')
plt.grid(True)
plt.show()
