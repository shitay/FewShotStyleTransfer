import os
import random
import shutil
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


def minimum_images():
    df = pd.read_csv('train.csv')
    artists = list(set(df['artist']))
    counts = {artist: len(df[df.artist == artist]) for artist in artists if len(df[df.artist == artist]) >= 100}
    print(len(counts))
    df_train = df[df['artist'].isin(list(counts.keys()))]
    df_train.to_csv('new_train.csv')
    print(len(df_train))


def copy_files(ref_csv, old_path, new_path):
    df = pd.read_csv(ref_csv)
    for i, row in df.iterrows():
        _, _, filename, artist, title, style, genere, date = row
        src_path = os.path.join(old_path, filename)
        dst_path = os.path.join(new_path, filename)
        if os.path.exists(src_path):
            if not os.path.exists(dst_path):
                shutil.copy(src_path, dst_path)


def min_dataset(style_type, n_sub_types, n_min_for_type, n_max_for_type):
    df = pd.read_csv('train.csv')
    sub_types = list(set(df[style_type]))
    counts = {sub_type: len(df[df[style_type] == sub_type]) for sub_type in sub_types
              if n_min_for_type <= len(df[df[style_type] == sub_type]) <= n_max_for_type}
    counts = Counter(counts)
    counts_top = dict(counts.most_common(n_sub_types))

    df_train = df[df[style_type].isin(list(counts_top.keys()))]
    print(len(df_train))
    df_train.to_csv(f'{style_type}_train.csv')

    print(list(counts_top.keys()), len(counts_top))


if __name__ == '__main__':
    # stats()
    # split_train_test()
    # stats('train.csv')
    # stats('test.csv')
    # minimum_images()
    # min_dataset('genre', 20, n_min_for_type=1000, n_max_for_type=2000)  # 'artist', 'style', 'genre'
    # min_dataset('style', 20, n_min_for_type=1000, n_max_for_type=2000)
    # min_dataset('artist', 20, n_min_for_type=150, n_max_for_type=300)
    copy_files('genre_train.csv', 'train', 'train_genre')
