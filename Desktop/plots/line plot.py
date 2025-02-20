# Description: This script creates a simple line plot using matplotlib and numpy.
#To show trends over time or a continuous relationship between variables.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 20)
y = np.sin(x)

plt.plot(x, y)
plt.title("A Line Plot")
plt.show()