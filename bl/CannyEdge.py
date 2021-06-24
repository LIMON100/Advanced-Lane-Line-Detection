# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 00:23:16 2021

@author: limon
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import cv2

image = mpimg.imread('test.jpg')


gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and run it
low_threshold = 1
high_threshold = 200
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)


plt.imshow(edges, cmap='Greys_r')
mpimg.imsave("edges.jpg", edges)
plt.show()