import PyPDF2
import re


# Open the PDF file in read-binary mode
with open('statements/Enclosures to Freeths.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Loop over each page in the PDF
    for page_num in range(pdf_reader.numPages):
        # Extract the text from the page
        page_text = pdf_reader.getPage(page_num).extractText()

        # find the line that contains account number using regex
        account_number = re.findall(r'Account number: \d+', page_text)[0]
        # find the line that conatins sort code using regex there is a hyphen in the sort code
        sort_code = re.findall(r'Sort code: \d+-\d+-\d+', page_text)[0]

        # Print the account number
        print(account_number)
        print(sort_code)

        # output the page text to a text file
        with open(f'page_{page_num + 1}.txt', 'w') as text_file:
            text_file.write(page_text)
