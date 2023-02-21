# check the first line of each file in output if they match "","Date","Type","Description","Paid in","Paid out","Balance"
# if not, print the file name and the first line
# if yes, move the file to the folder "correct"

import os
import shutil


def check_file(file):
    with open(file, 'r', encoding="UTF-8") as f:
        first_line = f.readline()
        if first_line == '"","Date","Type","Description","Paid in","Paid out","Balance"\n' or first_line == '"Date","Type","Description","Paid in","Paid out","Balance"\n':
            return True
        return False


def check_folder(folder):
    for file in os.listdir(folder):
        if check_file(folder + '/' + file):
            shutil.move(folder + '/' + file, 'correct/' + file)
        else:
            print(file, 'is not correct')


check_folder('output')
