import cv2
import os
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
        print(f"{folder_path} mappa létrehozva.")
    else:
        print(f"{folder_path} mappa már létezik.")

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

#check_createfolder("anchor")
#check_createfolder("negative")
#check_createfolder("positive")
#downloadimage.run()

# a mérete miatt nem tudtam feltölteni ide de innen le kell tölteni All images as gzipped tar file
# én winrar-al csomagoltam ki. Másold be a local mappába futtatás elött és a program átmásolja magától. 
contents = os.listdir("negative")

if len(contents) == 0:
    for directory in os.listdir('lfw'):
        for file in os.listdir(os.path.join('lfw', directory)):
            EX_PATH = os.path.join('lfw', directory, file)
            NEW_PATH = os.path.join("negative", file)
            os.replace(EX_PATH, NEW_PATH)

else:
    print("A képke már a negative mappában vannak.")

anchor = tf.data.Dataset.list_files("anchor/andris/*.jpg").take(25)
positive =  tf.data.Dataset.list_files("positive/andris/*.jpg").take(25)
negative =  tf.data.Dataset.list_files("negative/*.jpg").take(25)