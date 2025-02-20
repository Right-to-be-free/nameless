#HeatMap
#To show correlations or relationships between multiple variables.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title("Heatmap Example")
plt.show()
