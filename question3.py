# Problem 3: Plotting Trigonometric Functions
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
plt.figure()
plt.plot(x, y_sin, label='y = sin(x)', color='blue')
plt.plot(x, y_cos, label='y = cos(x)', color='red')
plt.plot(x, y_tan, label='y = tan(x)', color='green')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

