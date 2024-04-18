# Problem 5: Plotting Piecewise Functions
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.where(x < 0, -1, 1)
plt.plot(x, y)
plt.grid(True)
plt.show()
