# Problem 2: Plotting Multiple Functions

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)
plt.plot(x, y1, label='y = x^2', color='blue')
plt.plot(x, y2, label='y = sqrt(x)', color='red', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
