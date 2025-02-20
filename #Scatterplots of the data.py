#Scatterplots of the data
#To visualize the relationship between two numerical variables.

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.show()
