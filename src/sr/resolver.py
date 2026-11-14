# Basic code for computationally increasing resolution of captured images

import cv2 # OpenCV
from scipy.ndimage import gaussian_filter
import numpy as np

class Resolver:
    def __init__(camera):
        self.camera = camera
    
    def basic_sharpen(frame, harshness):
        # Create a blurred version of the frame and subtract it from the frame
        # drawback: focuses on sharpening already properly resolved features, not increasing resolution
        blurred_frame = scipy.ndimage.gaussian_filter(frame.astype(np.float32), sigma = (1, 1, 0))
        sharpened_frame = frame.astype(np.float32) + harshness * (frame.astype(np.float32) - blurred_frame)
        return sharpened_frame

    def frame_average(frame):
        return

    def non_blind_convolution(frame, type):
        return
    
    def fourier_ptychography(frame): # personally, this looks the most promising (will require an LED array purchase)
        return