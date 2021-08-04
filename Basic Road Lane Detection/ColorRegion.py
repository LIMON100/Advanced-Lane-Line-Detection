# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:31:25 2021

@author: limon
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


image = mpimg.imread('test.jpg')


ysize = image.shape[0]
xsize = image.shape[1]

color_select= np.copy(image)
line_image = np.copy(image)

# Define our color criteria
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]


# Vertices of a triangular region
left_bottom = [0, 539]
right_bottom = [900, 539]
apex = [475, 320]


# Perform a linear fit to each of the three sides of the triangle
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)


## Find those pixels which are below threshold
color_thresholds  = (image[:,:,0] < rgb_threshold[0])\
            | (image[:,:,1] < rgb_threshold[1])\
            | (image[:,:,2] < rgb_threshold[2])
            


XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))

region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))


# Mask color selection
color_select[color_thresholds] = [0,0,0]

# Find where image is both colored right and in the region
line_image[~color_thresholds & region_thresholds] = [255,0,0]

# Draw the dash line on the boundary
x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw=4)

# Display our two output images
plt.imshow(color_select)
plt.show()
plt.imshow(line_image)
plt.show()
mpimg.imsave("test-line-image.jpg", line_image)