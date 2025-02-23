from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'C:/path/to/DejaVuSans.ttf')  # Replace with the actual path
pdf.set_font('DejaVu', '', 14)
pdf.cell(200, 10, txt="Hello World!", ln=True, align='C')
pdf.output("hello_world.pdf")
# Sample DataFrame
data = {
    'Page': ['/about/state-profile/', '/legislature/members-of-legislature/', '/judiciary/chief-justice/'],
    'Title': ['State Profile – Telangana State Portal', 'Members of Legislative Assembly – Telangana State Portal', 'Chief Justice – Telangana State Portal'],
    'Content': ['Formed as the 29th State of India, Telangana ...', 'Site Map | Screen Reader | Contact | Terms Of...', 'Hon’ble Chief Justice Alok Aradhe was born on...']
}
df = pd.DataFrame(data)

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add Unicode font (DejaVu)
pdf.add_font('DejaVu', '', 'path_to_your_DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)

# Add Title
pdf.cell(200, 10, text="Cleaned Data", new_x='LMARGIN', new_y='NEXT', align='C')

# Process each row
for _, row in df.iterrows():
    row_text = f"Page: {row['Page']} | Title: {row['Title']} | Content: {row['Content']}"
    
    # Write text to PDF
    pdf.cell(200, 10, text=row_text, new_x='LMARGIN', new_y='NEXT')

# Save the PDF
pdf.output("output.pdf")
