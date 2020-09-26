# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:50:55 2020

@author: user
"""
import os
from imutils import paths

images="Nepali"
model = "NSL.hdf5"
imagePaths = list(paths.list_images(images))
def get_labels():
    labels = []
    for x in imagePaths:
        label = x.split(os.path.sep)[-1].split(".")[0].split("-")[0]
        if label not in labels:
            labels.append(label)
    CLASSES = labels
    CLASSES.sort()
    return CLASSES
        
    


