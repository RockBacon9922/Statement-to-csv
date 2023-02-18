import camelot

# read the pdf file
tables = camelot.read_pdf('statements/Enclosures to Freeths.pdf', pages='all')

# print the number of tables found
print(f'Number of tables extracted: {len(tables)}')
