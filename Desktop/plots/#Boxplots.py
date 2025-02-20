#Boxplots
#To show the distribution of data and detect outliers.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
sns.boxplot(y=data)
plt.title("Box Plot Example")
plt.show()
