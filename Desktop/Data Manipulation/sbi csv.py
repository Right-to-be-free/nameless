import pandas as pd

df = pd.read_csv(r"C:\Users\rishi\output.csv")

df.loc[0, "description"] = "This is a test"

df.to_csv(r"C:\Users\rishi\output.csv", index=False)

print(df)






