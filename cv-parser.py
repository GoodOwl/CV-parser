import os
import docx2txt
import PyPDF2
import pandas as pd

def extract_data_from_word(doc_path):
    text = docx2txt.process(doc_path)
    # Extract relevant information like name and skills from 'text'
    # Example: name = extract_name(text)
    #         skills = extract_skills(text)
    return name, skills

def extract_data_from_pdf(pdf_path):
    # Use PyPDF2 or pdfplumber to extract text from PDF
    # Example: text = extract_text_from_pdf(pdf_path)
    # Extract relevant information like name and skills from 'text'
    # Example: name = extract_name(text)
    #         skills = extract_skills(text)
    return name, skills

# Iterate through CV files in a folder
cv_folder = "/path/to/cv/folder"
excel_path = "/path/to/output/excel/file.xlsx"

data = {'Name': [], 'Skills': []}

for filename in os.listdir(cv_folder):
    if filename.endswith(".docx"):
        doc_path = os.path.join(cv_folder, filename)
        name, skills = extract_data_from_word(doc_path)
        data['Name'].append(name)
        data['Skills'].append(skills)
    elif filename.endswith(".pdf"):
        pdf_path = os.path.join(cv_folder, filename)
        name, skills = extract_data_from_pdf(pdf_path)
        data['Name'].append(name)
        data['Skills'].append(skills)

# Create a DataFrame and save to Excel
df = pd.DataFrame(data)
df.to_excel(excel_path, index=False)