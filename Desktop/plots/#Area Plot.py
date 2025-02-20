#Area Plot
#Similar to a line plot but filled with color to show magnitude.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.plot(x, y, color='blue')
plt.title("Area Plot Example")
plt.show()
