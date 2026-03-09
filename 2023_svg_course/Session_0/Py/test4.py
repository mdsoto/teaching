# Two-curve plot with grid and title program

# libraries
import matplotlib.pyplot as plt
import numpy as np

# data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
r = 1 + np.cos(2 * np.pi * t)

# plot
plt.plot(t, s)
plt.plot(t, r)
plt.xlabel('x')
plt.ylabel('s and r')
plt.title('Two waves')
plt.grid()
plt.show()
