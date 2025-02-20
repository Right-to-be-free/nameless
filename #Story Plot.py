#Story Plot

#Line Plot
#Use Case:
#Typically used to show trends over time.
#Since your dataset doesn’t have time-series data, we can use it to plot Age trends.

import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Name": ["Rishi", "Jaga", "Pavan", "Naveen", "Anirudh", "Nani"],
    "Age": [29, 32, 27, 23, 27, 25]
})

plt.plot(df["Name"], df["Age"], marker="o", linestyle="-", color="blue")
plt.title("Age Line Plot")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.grid()
plt.show()

#2. Bar Plot
#Use Case:
#Comparing categorical values (e.g., Age of different people).

import seaborn as sns

sns.barplot(x=df["Name"], y=df["Age"], palette="Blues")
plt.title("Bar Plot of Ages")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.show()

#3. Histogram
#Use Case:
#Shows the distribution of a numerical variable (e.g., Age).

import matplotlib.pyplot as plt
plt.hist(df["Age"], bins=5, edgecolor="black", color="purple", alpha=0.7)
plt.title("Histogram of Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#4. Scatter Plot
#Use Case:
#Shows relationships between two numerical variables (e.g., Name vs. Age).

plt.scatter(df["Age"], range(len(df["Age"])), color="red", marker="o", alpha=0.5)
plt.title("Scatter Plot of Ages")
plt.xlabel("Age")
plt.ylabel("Index")
plt.show()

#5. Box Plot
#Use Case:
#Helps identify outliers and the spread of a dataset.

sns.boxplot(y=df["Age"])
plt.title("Box Plot of Age")
plt.show()

#6. Pie Chart
#Use Case:
#Shows proportions of categorical data (e.g., people in different states).

df["State"] = ["MA", "NC", "SC", "AL", "FL", "GA"]

df["State"].value_counts().plot.pie(autopct='%1.1f%%', cmap="coolwarm")
plt.title("State Distribution")
plt.ylabel("")
plt.show()

#7. Heatmap
#Use Case:
#Shows correlation between numerical data (not much in this dataset, but we can visualize it).


import numpy as np

corr_matrix = df[["Age"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap of Age")
plt.show()

#8. Violin Plot
#Use Case:
#Similar to a box plot but also shows data density.

sns.violinplot(y=df["Age"])
plt.title("Violin Plot of Age")
plt.show()


#9. Area Plot
#Use Case:
#Similar to a line plot but with the area under the curve filled.
#Shows the magnitude of a variable over a sequence (e.g., Age distribution).

import numpy as np

plt.fill_between(df["Name"], df["Age"], color='skyblue', alpha=0.4)
plt.plot(df["Name"], df["Age"], color='blue', marker="o")
plt.title("Area Plot of Age")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.show()


#10. Bubble Plot
#Use Case:      
#Shows relationships between three numerical variables.
#In this case, we can use it to show Name, Age, and State.

plt.scatter(df["Name"], df["Age"], s=df["Age"]*10, alpha=0.5)
plt.title("Bubble Plot of Age")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.show()

#10. Pair Plot
#Use Case:
#Shows relationships between multiple numerical variables in a dataset.
#Works best when there are at least 2-3 numerical columns.
#Since your dataset has only Age as a numerical column, we can modify it by adding random Salary values for demonstration.

import seaborn as sns
import numpy as np

# Adding a new numerical column (Salary) for better visualization
df["Salary"] = np.random.randint(40000, 100000, size=len(df))

sns.pairplot(df, hue="State")  # Color by 'State' (categorical variable)
plt.show()



