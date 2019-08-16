"""
Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license
(https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
"""
import os.path

import pandas as pd
import torch.utils.data as data
from PIL import Image
from PIL import ImageFile
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

def default_loader(path):
    return Image.open(path).convert('RGB')


def default_filelist_reader(filelist):
    im_list = []
    with open(filelist, 'r') as rf:
        for line in rf.readlines():
            im_path = line.strip()
            im_list.append(im_path)
    return im_list


class ImageLabelFilelist(data.Dataset):
    def __init__(self,
                 root,
                 filelist,
                 transform=None,
                 loader=default_loader,
                 return_paths=False,
                 style_type='artist'):
        self.root = root
        self.transform = transform
        self.loader = loader
        df = pd.read_csv(filelist)
        self.classes = sorted(list(set(df[style_type])))
        self.class_to_idx = {self.classes[i]: i for i in range(len(self.classes))}
        self.imgs = [(im_name, self.class_to_idx[cls])
                     for _, (im_name, cls) in df[['filename', style_type]].iterrows()
                     if os.path.exists(os.path.join(self.root, im_name))]
        self.return_paths = return_paths
        print('Data loader')
        print("\tRoot: %s" % root)
        print("\tList: %s" % filelist)
        print("\tNumber of classes: %d" % (len(self.classes)))
        print("\tNumber of images: %d" % (len(self.imgs)))

    def __getitem__(self, index):
        im_path, label = self.imgs[index]
        path = os.path.join(self.root, im_path)
        img = self.loader(path)
        if self.transform is not None:
            img = self.transform(img)
        if self.return_paths:
            return img, label, path
        else:
            return img, label

    def __len__(self):
        return len(self.imgs)
