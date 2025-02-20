#Hisogram
#To show the distribution of a continuous variable.

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.title("Histogram Example")
plt.show()
