import os
from skimage import io, color, transform
import matplotlib.pyplot as plt
import numpy as np

namelist = os.listdir('/Users/alexanderyoung/Desktop/SampleImages/pics')
dir = os.getcwd();
total = []

for i in namelist:
    if i!=".DS_Store":
        # filepath=dir+"/pics/"+i
        img = io.imread("/Users/alexanderyoung/Desktop/SampleImages/pics/WT101.tif",'tiff')
        # plt.figure()
        # plt.imshow(img, cmap='gray')

        #Image already in grayscale

        #Resize gray image
        # plt.figure()
        img_resized = transform.resize(img, (60,80))
        # plt.imshow(img_resized, cmap='gray')
    
        #Convert image to 1D array
        img_1d = np.concatenate(img_resized, 0)
        print img_1d.shape
        total.append(img_1d)

# print total
    


