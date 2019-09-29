from skimage import io, color, transform
import os
import matplotlib.pyplot as plt
import numpy as np


filename = os.path.join('/Users/dexterwei/Documents/ML/alex/toy_images', 'img_1.png')
img = io.imread(filename)
plt.figure()
plt.imshow(img, cmap='gray')

# Convert color image to grayscale
plt.figure()
img_grayscale = color.rgb2gray(img)
plt.imshow(img_grayscale, cmap='gray')

# Resize gray image
plt.figure()
img_resized = transform.resize(img_grayscale, (100, 100))
plt.imshow(img_resized, cmap='gray')

# concatenate image to 1-D array
img_1d = np.concatenate(img_resized, 0)

plt.show()

print 'orig image: ', img.shape, type(img)

print 'grayscale image: ', img_grayscale.shape, type(img_grayscale)

print 'resized image: ', img_resized.shape, type(img_resized)

print 'concatenated image', img_1d.shape, type(img_1d)