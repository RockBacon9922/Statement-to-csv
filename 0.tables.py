import camelot

# read the pdf file
tables = camelot.read_pdf(
    'statements/example.pdf', pages='all', flavor='stream')

# print the number of tables found
print(f'Number of tables extracted: {len(tables)}')

# export the event number table to a csv file
fileCounter = 1
for i, table in enumerate(tables):
    table.to_csv(f'output/page_{fileCounter}.csv')
    fileCounter += 1

