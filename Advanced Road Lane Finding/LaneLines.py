# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:54:33 2021

@author: limon
"""


import cv2
import numpy as np
import matplotlib.image as mpimg


def hist(img):
    
    """After applying calibration, thresholding, and a perspective transform to a road image, you should have a binary image where the lane lines stand out clearly.
       However, you still need to decide explicitly which pixels are part of the lines and which belong to the left line and which belong to the right line.

       Plotting a histogram of where the binary activations occur across the image is one potential solution for this. In the quiz below, let's take a couple quick steps to create our histogram!"""
    
    bottom_half = img[img.shape[0]//2:,:]
    return np.sum(bottom_half, axis = 0)



class LaneLines:
    
    def __init__(self):
        
        self.left.fit = None
        self.right.fit = None
        self.binary = None
        self.nonzero = None
        self.nonzerox = None
        self.nonzeroy = None
        self.clear.visibility = True
        self.dir = []
        
        self.left_curve_img = mpimg.imread("left_turn.png")
        self.right_curve_img = mpimg.imread("right_turn.png")
        self.keep_straight_img = mpimg.imread("straight.png")
        
        self.left_curve_img = cv2.normalize(src = self.left_curve_img, dst = None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_8U)
        self.right_curve_img = cv2.normalize(src = self.right_curve_img, dst = None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_8U)
        self.keep_straight_img = cv2.normalize(src = self.keep_straight_img, dst = None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_8U)
        
        
        """set a few hyperparameters related to our sliding windows, and set them up to iterate across the binary activations in the image
        """
        
        self.nwindows = 9
        self.margin = 100
        self.minpix = 50
        
    
    def forward(self, img):
        
        self.extract_features(img)
        return self.fit_poly(img)
        
    
    def pixels_in_window(self, center, margin, height):
        
        topleft = (center[0] - margin, center[1] - height // 2)
        bottomright = (center[0] + margin, center[1] + height // 2)
        
        condx = (topleft[0] <= self.nonzerox) & (self.nozerox <= bottomright[0])
        condy = (topleft[1] <= self.nonzeroy) & (self.nonzeroy <= bottomright[1])
        
        return self.nonzerox[condx & condy], self.nonzeroy[condx & condy]
    
    
    def extract_features(self, img):
        
        self.img = img
        """ Height of of windows - based on nwindows and image shape """
        self.window_height = np.int(img.shape[0]//self.nwindows)

        """ Identify the x and y positions of all nonzero pixel in the image """
        self.nonzero = img.nonzero()
        self.nonzerox = np.array(self.nonzero[1])
        self.nonzeroy = np.array(self.nonzero[0])
        
    