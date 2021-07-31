# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:12:11 2021

@author: limon
"""



import numpy as np
import matplotlib.image as mpimg
import cv2
from docopt import docopt
from IPython.display import HTML, Video
from moviepy.editor import VideoFileClip
from CameraCalibration import CameraCalibration
from Thresholding import *
from PerspectiveTransformation import *
from LaneLines import *



class FindLaneLines:
    
    def __init__(self):
        self.calibration = CameraCalibration('camera_cal', 9, 6)
        self.threshold = Thresholding()
        self.transform = PerspectiveTransformation()
        self.laneLines = LaneLines()
        
        
    def forward(self, img):
        out_img = np.copy(img)
        img = self.calibration.unidstort(img)
        img = self.transform.forward(img)
        img = self.thresholding.forward(img)
        img = self.lanelines.forward(img)
        img = self.transform.backward(img)
        
        out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
        out_img = self.laneLines.plot(out_img)
        return out_img
    
    
    def process_image(self, input_path, output_path):
        img = mpimg.imread(input_path)
        out_img = self.forward(img)
        mpimg.imsave(output_path, out_img)
        

    def process_video(self, input_path, output_path):
        clip = VideoFileClip(input_path)
        out_clip = clip.fl_image(self.forward)
        out_clip.write_videofile(output_path, audio=False)
        
        

def main():
    args = docopt(__doc__)
    inputs = args['INPUT_PATH']
    output = args["OUTPUT_PATH"]
    
    findLaneLines = FindLaneLines()
    if args["--video"]:
        findLaneLines.process_video(inputs, output)
    else:
        findLaneLines.preocess_image(inputs, output)


if __name__ == "__main__":
    main()