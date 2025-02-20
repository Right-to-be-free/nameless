#Pie Chart
#To show the proportion of categories in a dataset.

import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [10, 20, 30, 40]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()
