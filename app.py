import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from docx import Document
from fpdf import FPDF

app = Flask(__name__)

# Define paths correctly
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "pdfs")

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER
ALLOWED_EXTENSIONS = {"txt", "docx"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def clean_text(text):
    """Replace unsupported characters with safe alternatives"""
    replacements = {
        "\u2014": "-", "\u2013": "-", "\u2026": "...",
        "\u201C": '"', "\u201D": '"', "\u2018": "'", "\u2019": "'"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def convert_to_pdf(input_path, output_path):
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=10)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        if input_path.endswith(".txt"):
            with open(input_path, "r", encoding="utf-8") as file:
                for line in file:
                    pdf.cell(200, 10, txt=clean_text(line.strip()), ln=True)
        elif input_path.endswith(".docx"):
            doc = Document(input_path)
            for para in doc.paragraphs:
                pdf.cell(200, 10, txt=clean_text(para.text), ln=True)

        pdf.output(output_path, "F")

        # Debugging statement
        print(f"PDF generated successfully: {output_path}")

        if not os.path.exists(output_path):
            raise Exception("PDF file was not created successfully.")
    
    except Exception as e:
        print(f"Error during PDF conversion: {e}")

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"

        file = request.files["file"]
        if file.filename == "":
            return "No selected file"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(input_path)

            output_filename = f"{os.path.splitext(filename)[0]}.pdf"
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_filename)

            # Debugging statement
            print(f"Input File: {input_path}")
            print(f"Output PDF: {output_path}")

            convert_to_pdf(input_path, output_path)

            if os.path.exists(output_path):
                return send_file(output_path, as_attachment=True)
            else:
                return "Error: PDF file could not be created."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
