from collections import Counter

import pandas as pd
import numpy as np


def stats():
    df = pd.read_csv('train_info.csv')
    for style_type in ['artist', 'style', 'genre']:
        counts = list(Counter(df[style_type]).values())
        print((style_type, len(counts), np.mean(counts), np.std(counts), np.min(counts), np.max(counts)))


def new_info_with_min(style_type, k=10):
    df = pd.read_csv('train_info.csv')


if __name__ == '__main__':
    stats()