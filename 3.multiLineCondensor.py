import pandas as pd
import os
import re

# get every file in correct
csv_files = [file for file in os.listdir(
    "correct") if file.endswith('.csv')]

csv_files.sort(key=lambda f: int(re.sub('\D', '', f)))
dataframes = [pd.read_csv(f'correct/{file}', header=0) for file in csv_files]


for frame in csv_files:
    df = pd.read_csv(f'correct/{frame}', header=0)

    # get rid of any line with the words "BROUGHT FORWARD" in it any column
    df = df[df['Date'] != 'BROUGHT FORWARD']
    # Drop the first column with nothing in it
    try:
        df = df.drop(columns=['Unnamed: 0'])
    except:
        pass
    # get rid of all the lines which are completely empty
    df = df.dropna(how='all')

    blanks = df[df['Balance'].isna()]

    # create a new DataFrame to hold the modified data
    new_df = pd.DataFrame(columns=df.columns)

    # iterate over the rows in blanks
    for _, row in blanks.iterrows():
        # iterate over the columns in df
        for col in df.columns:
            # if the cell is not empty
            if not pd.isna(row[col]):
                # get the index value for the previous row
                prev_row_idx = row.name - 1
                # check if the previous row exists in df
                if prev_row_idx in df.index:
                    # append the cell contents to the previous row
                    df.loc[prev_row_idx, col] = str(
                        df.loc[prev_row_idx, col]) + ' ' + str(row[col])

                else:
                    # append a new row to the new DataFrame with the cell contents
                    new_row = pd.DataFrame(
                        {col: [row[col]]}, index=[prev_row_idx+1])
                    new_df = pd.concat([new_df, new_row])

    # append the non-empty rows from df to the new DataFrame
    new_df = pd.concat([new_df, df.drop(blanks.index)])

    # assign the new DataFrame to df
    df = new_df

    # write the modified DataFrame to a the same file
    df.to_csv(f'correct/{frame}', index=False)
