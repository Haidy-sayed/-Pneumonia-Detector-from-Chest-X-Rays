#this is a simple program to detect pneumoia from chest x-ray , submitted by Haidy Sayed , started this project on June 14th of 2026


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


#conting content of each directory

path_train_normal = 'chest_xray\\train\\NORMAL'
path_train_pneumonia = 'chest_xray\\train\\PNEUMONIA'

train_normal = os.listdir(path_train_normal)
train_pneumonia = os.listdir(path_train_pneumonia)

print("len train N = " + str(len(train_normal)))
print("len train P = " + str(len(train_pneumonia)))

# Visualize sample images
fig, axes = plt.subplots(2, 4, figsize=(12, 6))
for i, label in enumerate(['NORMAL', 'PNEUMONIA']):
    folder = f'chest_xray\\train\\{label}'
    images = [f for f in os.listdir(folder) if f.endswith(('.jpg', '.jpeg', '.png'))][:4]
    for j, img_name in enumerate(images):
        img = Image.open(f'{folder}/{img_name}').convert('L')
        axes[i][j].imshow(img, cmap='gray')
        axes[i][j].set_title(label)
        axes[i][j].axis('off')
plt.tight_layout()
plt.savefig('sample_images.png')
plt.show()