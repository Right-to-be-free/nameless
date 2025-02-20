#YouTube Data Analysis

import pandas as pd
import os

# Define the CSV file path
csv_file_path = r"C:\Users\rishi\Downloads\archive (1).zip"

# Load the dataset
df = pd.read_csv(csv_file_path)

# Display basic information about the dataset
print(df.info())
print(df.head())

# Convert 'Video views' and 'Likes' to numeric (remove commas)
df["Video views"] = df["Video views"].str.replace(",", "").astype(float)
df["Likes"] = df["Likes"].str.replace(",", "").astype(float)

# Drop rows with missing values in essential numeric columns
df_cleaned = df.dropna(subset=["Video views", "Likes"])

# Display the cleaned dataset summary
df_cleaned.info(), df_cleaned.head()

#1. Line Plot
#Use Case:
#Shows trends over time (e.g., number of views per year).


import matplotlib.pyplot as plt

# Average views per year
views_per_year = df_cleaned.groupby("published")["Video views"].mean()

plt.plot(views_per_year.index, views_per_year.values, marker="o", linestyle="-", color="blue")
plt.title("Average Video Views Over Time")
plt.xlabel("Year Published")
plt.ylabel("Average Views")
plt.grid()
plt.show()


#2. Bar Plot
#Use Case:
#Compares average views across different video categories.

import seaborn as sns

category_views = df_cleaned.groupby("Category")["Video views"].mean().reset_index()
sns.barplot(x="Video views", y="Category", data=category_views, palette="Blues")

plt.title("Average Views per Category")
plt.xlabel("Average Views")
plt.ylabel("Category")
plt.show()

#3. Histogram
#Use Case:
#Shows the distribution of video views.

plt.hist(df_cleaned["Video views"], bins=30, edgecolor="black", color="purple", alpha=0.7)
plt.title("Distribution of Video Views")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.xscale("log")  # Log scale to handle large numbers
plt.show()

#4. Scatter Plot
#Use Case:
#Shows the relationship between likes and views.

plt.scatter(df_cleaned["Video views"], df_cleaned["Likes"], alpha=0.5, color="red")
plt.title("Scatter Plot: Views vs Likes")
plt.xlabel("Video Views")
plt.ylabel("Likes")
plt.xscale("log")
plt.yscale("log")
plt.show()

#5. Box Plot
#Use Case:
#Identifies outliers in video views.

sns.boxplot(y=df_cleaned["Video views"])
plt.title("Box Plot of Video Views")
plt.yscale("log")  # Log scale for better visibility
plt.show()

#6. Pie Chart
#Use Case:
#Shows the proportion of video categories.

import matplotlib.pyplot as plt

# Count categories
category_counts = df_cleaned["Category"].value_counts()

# Define explode values (slightly separate slices)
explode_values = [0.05] * len(category_counts)  # Slightly separate all slices

# Create pie chart with adjustments
plt.figure(figsize=(12, 8))  # Increase figure size
wedges, texts, autotexts = plt.pie(
    category_counts, 
    labels=category_counts.index,  # Use category names as labels
    autopct='%1.1f%%', 
    startangle=140, 
    explode=explode_values,  # Slightly separate slices
    pctdistance=0.75,  # Position percentage labels closer
    labeldistance=1.05,  # Move text labels outward
    wedgeprops={"edgecolor": "black", "linewidth": 1}  # Add border
)

# Make percentage labels bold
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_weight("bold")

# Move legend outside the pie chart
plt.legend(
    loc="upper left", 
    bbox_to_anchor=(1, 1), 
    title="Video Categories", 
    fontsize=10
)

# Set title
plt.title("Distribution of Video Categories", fontsize=14)

# Show plot
plt.show()


#7. Heatmap
#Use Case:
#Shows correlations between views, likes, and published year.

import numpy as np

corr_matrix = df_cleaned[["Video views", "Likes", "published"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#8. Violin Plot
#Use Case:
#Shows the density of video views by category.

sns.violinplot(x="Category", y="Video views", data=df_cleaned)
plt.title("Violin Plot of Views per Category")
plt.xticks(rotation=90)
plt.yscale("log")
plt.show()


#9. Area Plot
#Use Case:
#Shows the total views per year.

plt.fill_between(views_per_year.index, views_per_year.values, color='skyblue', alpha=0.4)
plt.plot(views_per_year.index, views_per_year.values, color='blue', marker="o")
plt.title("Total Video Views Over Time")
plt.xlabel("Year Published")
plt.ylabel("Total Views")
plt.grid()
plt.show()

#10. Pair Plot
#Use Case:
#Shows relationships between multiple numerical variables.

sns.pairplot(df_cleaned[["Video views", "Likes", "published"]])
plt.show()



