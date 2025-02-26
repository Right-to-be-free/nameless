import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the Excel file
file_path = r"C:\Users\rishi\.cursor-tutor\youtube_comments.xlsx"  # Ensure the correct file path
df = pd.read_excel(file_path)

# Data Cleaning Function
def clean_text(text):
    if isinstance(text, str):  # Ensure text is a string
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
        return text.strip()
    return ""

# Apply cleaning
df["Cleaned Comment"] = df["Comment Text"].fillna("").astype(str).apply(clean_text)

# Sentiment Analysis Function
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply Sentiment Analysis
df["Sentiment"] = df["Cleaned Comment"].apply(get_sentiment)

# Count Sentiment Categories
sentiment_counts = df["Sentiment"].value_counts()

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar", color=["green", "gray", "red"])
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")
plt.title("YouTube Comments Sentiment Analysis")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Save the processed data
df.to_excel("cleaned_youtube_comments.xlsx", index=False)

print("Sentiment analysis completed and saved as 'cleaned_youtube_comments.xlsx'.")
