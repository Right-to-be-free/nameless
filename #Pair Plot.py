#Pair Plot
#To visualize relationships between multiple numerical variables.

import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("iris")
sns.pairplot(data, hue="species")
plt.show()
