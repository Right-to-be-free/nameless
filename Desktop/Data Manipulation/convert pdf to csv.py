import pdfplumber
import pandas as pd
    
def convert_pdf_to_csv(pdf_path, csv_path):
        all_data = []
        with pdfplumber.open(r"C:\Users\rishi\Desktop\sbi\1739469570761HKIsf9DLaW8dHKUC.pdf") as pdf:

            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    all_data.append(df)
        
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df.to_csv(csv_path, index=False)
    
pdf_file = 'input.pdf'
csv_file = 'output.csv'
convert_pdf_to_csv(pdf_file, csv_file)
print(f"Successfully converted '{pdf_file}' to '{csv_file}'")