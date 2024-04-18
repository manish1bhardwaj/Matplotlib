import numpy as np
import matplotlib.pyplot as plt

# Problem 1: Plotting a Linear Function
x = np.linspace(-10, 10, 100)
y = 2*x + 3
plt.figure()
plt.plot(x, y)
plt.title('Linear Function: y = 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
