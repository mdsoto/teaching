# One-curve plot program

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,101,1)

y = x**2 + 2*x + 2

plt.plot(x,y)
plt.ylabel('y')
plt.xlabel('x')
plt.show()
