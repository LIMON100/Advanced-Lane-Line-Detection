# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:37:48 2021

@author: limon
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('I:/1.232 Pora/ALL Projects/Road Lane recognition/Try/test_images/test.jpg')



ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)


# Define color selection criteria
red_threshold = 200
green_threshold = 200
blue_threshold = 200


rgb_threshold = [red_threshold, green_threshold, blue_threshold]


## Find those pixels which are below threshold
thresholds = (image[:,:,0] < rgb_threshold[0])\
            | (image[:,:,1] < rgb_threshold[1])\
            | (image[:,:,2] < rgb_threshold[2])
             
             
color_select[thresholds] = [0, 0, 0]

plt.imshow(color_select)

mpimg.imsave('test_after.jpg', color_select)