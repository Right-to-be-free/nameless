import pandas as pd

from csv2pdf import convert
convert(r"C:\Users\rishi\output.csv", "destination.pdf")
print("PDF file created successfully.")