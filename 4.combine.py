import os
import pandas as pd
import re


def combine_csv():
    csv_files = [file for file in os.listdir(
        "correct") if file.endswith('.csv')]
    # sort the list by the two digit number in the file name
    csv_files.sort(key=lambda f: int(re.sub('\D', '', f)))
    dataframes = [pd.read_csv(f'correct/{file}', header=0)
                  for file in csv_files]
    combined_df = pd.concat(dataframes)
    combined_df.to_csv('statements/combined.csv', index=False)


combine_csv()
