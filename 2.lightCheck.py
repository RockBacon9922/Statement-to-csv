# import pandas as pd and re

import pandas as pd
import re
import os

# open each file in the ouput folder if the first line doesn't include words such as date time and balance then print the first line and ask teh user if he wants to delete the file


def check_file(file):
    with open(file, 'r') as f:
        first_line = f.readline()
        if not re.search(r'Date|Time|Balance', first_line):
            print(first_line)
            delete = input('Do you want to delete this file? (y/n) ')
            if delete == 'y':
                os.remove(file)
            else:
                pass

# loop through the files in the output folder and run the check_file function on each file


for file in os.listdir('output'):
    check_file('output/' + file)
