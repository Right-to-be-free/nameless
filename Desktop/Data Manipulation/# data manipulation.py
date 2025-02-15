# data manipulation

import pandas as pd



df = pd.DataFrame( {"Name" : ["rishi"],
                  "Age" : [29],
                   "City" : ["Boston"],
                    "State" : ["MA"], 
                    "Country" : ["USA"],
                    "Phone" : ["1234567890"] })
new_rows = pd.DataFrame([
    {"Name": "rishi", "Age": 29, "City": "Boston", "State": "MA", "Country": "USA", "Phone": 12365464686},
    {"Name": "Jaga", "Age": 25, "City": "Boston", "State": "CA", "Country": "USA", "Phone": 123654286},
    {"Name": "Pavan", "Age": 29, "City": "Boston", "State": "MI", "Country": "USA", "Phone": 1236564664886},
    {"Name": "Naveen", "Age": 22, "City": "Boston", "State": "OA", "Country": "USA", "Phone": 12342286686},
    {"Name": "Anirudh", "Age": 27, "City": "Boston", "State": "FL", "Country": "USA", "Phone": 124144411486},
    {"Name": "Nani", "Age": 32, "City": "Boston", "State": "MA", "Country": "USA", "Phone": 12365441144686},
])
df = pd.concat([df, new_rows], ignore_index=True)
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.describe(include='all'))
