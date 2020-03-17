import pandas as pd
import os


def run_csvreader(directory):
    for CSV in os.listdir(directory):
        if '.csv' in CSV:
            dataframe = pd.read_csv(directory+'/'+CSV)

    print(dataframe)


print('-------Train------')
run_csvreader('ObjectDetec/train')
print('\n-------Test------')
run_csvreader('ObjectDetec/test')