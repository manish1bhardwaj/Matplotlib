import numpy as np
import matplotlib.pyplot as plt
# Problem 10: Plotting Piecewise Linear Functions
x = np.linspace(-2, 2, 100)
y = np.where(x <= 0, -x, x)
plt.figure()
plt.plot(x, y)
plt.title('Piecewise Linear Function: f(x) = -x if x <= 0, x if x > 0')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()