import random
from collections import Counter

import pandas as pd
import numpy as np


def stats(csv_file='train_info.csv'):
    df = pd.read_csv(csv_file)
    for style_type in ['artist', 'style', 'genre']:
        counts = list(Counter(df[style_type]).values())
        print((style_type, len(counts), np.mean(counts), np.std(counts), np.min(counts), np.max(counts)))


def split_train_test(train_per=0.9):
    df = pd.read_csv('train_info.csv')
    artists = list(set(df['artist']))
    random.shuffle(artists)
    split_index = int(len(artists) * train_per)
    artists_train = artists[:split_index]
    artists_test = artists[split_index:]
    df_train = df[df['artist'].isin(artists_train)]
    df_test = df[df['artist'].isin(artists_test)]
    df_train.to_csv('train.csv')
    df_test.to_csv('test.csv')


if __name__ == '__main__':
    stats()
    # split_train_test()
    # stats('train.csv')
    # stats('test.csv')
