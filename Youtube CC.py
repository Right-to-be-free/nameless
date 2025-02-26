import pandas as pd

# Load the uploaded Excel file
file_path = "/mnt/data/youtube_comments.xlsx"
df = pd.read_excel(file_path)

# Display basic info about the data
df.head()
