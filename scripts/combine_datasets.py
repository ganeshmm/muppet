import os
import pandas as pd
import re

rt_regex = re.compile(r'^[rR][tT]')
url_regex = re.compile(r'https?:\/\/')

raw_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/raw'))
processed_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/processed'))

train = pd.read_csv(os.path.join(raw_path, 'train.csv.tar.bz2'))
train = train[pd.notna(train['text'])]
dev = pd.read_csv(os.path.join(raw_path, 'dev.csv'))
test = pd.read_csv(os.path.join(raw_path, 'test.csv'))

sets = [train, dev, test]
combined = pd.concat(sets, ignore_index=True)
combined = combined[['text', 'lable']]
combined = combined.rename(columns={'lable': 'label'})
combined = combined[pd.notna(combined['text'])]

combined = combined[combined['text'].apply(lambda text: rt_regex.search(text) is None)]
combined = combined[combined['text'].apply(lambda text: url_regex.search(text) is None)]

print('Size: ', combined.shape[0]) # Size: 358067
combined.to_csv(os.path.join(processed_path, 'combined.csv.bz2'), index=False, compression='bz2')