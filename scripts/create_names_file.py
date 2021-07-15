import os
import pandas as pd
import math

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
full = pd.read_csv(os.path.join(data_path, 'raw/full.csv.bz2'))
emojis = full['label'].unique()

names_file = open(os.path.join(data_path, 'class_names.txt'), 'w')
for emoji in emojis:
    names_file.write(str(emoji) + '\n')
names_file.close()