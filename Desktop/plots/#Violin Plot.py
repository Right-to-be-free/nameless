#Violin Plot
#Similar to a box plot but shows the probability density.

import seaborn as sns      
import matplotlib.pyplot as plt
import pandas as pd


data = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=data)
plt.show()

