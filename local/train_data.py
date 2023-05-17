import cv2
import os
import random
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf
import downloadimage

#check folder is exsist
def check_createfolder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

# max gpu memory set
"""
gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

print(gpus)
"""

# ez akkor kéne ha gpu-val tanítanám az adatot de valamiért nem ismeri fel a videókártyámat 
# ha ketörlöd a kommentet és megjelenik pl: (name='/phisical_device:GPU:0', device_type='GPU')
# akkor használhatod ha nem akkor hagy kikommentelve

check_createfolder("anchor")
check_createfolder("negative")
check_createfolder("positive")
downloadimage.run()