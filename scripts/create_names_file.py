import os
import pandas as pd
import math

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
combined = pd.read_csv(os.path.join(data_path, 'processed/combined.csv.bz2'))
emojis = combined['label'].unique()

names_file = open(os.path.join(data_path, 'class_names.txt'), 'w')
for emoji in emojis:
    if pd.notnull(emoji):
        names_file.write(str(emoji) + '\n')
names_file.close()