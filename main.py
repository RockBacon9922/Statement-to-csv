import re
import pandas as pd
import PyPDF2

# Define the column names for the CSV file
columns = ['date', 'type', 'description', 'paid in', 'paid out', 'balance']

# Open the PDF file and read its contents
with open('statements/Enclosures to Freeths.pdf', 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    num_pages = len(pdf.pages)
    page_texts = []

    # Extract the text from each page and remove the header
    for i in range(num_pages):
        page = pdf.pages[i]
        page_text = page.extract_text()
        header = re.findall(
            r'^\d{4}-\d{2}-\d{2}\s+\d{4}-\d{2}-\d{2}', page_text)[0]
        table_text = page_text.replace(header, '')
        page_texts.append(table_text)

    # Convert the text into a pandas DataFrame and save it as a CSV file
    df = pd.concat([pd.read_csv(pd.compat.StringIO(
        text), delimiter='\t', header=None, names=columns) for text in page_texts])
    df.to_csv('bank_statements.csv', index=False)
