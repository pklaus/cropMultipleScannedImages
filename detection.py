#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image # needs PIL: sudo aptitude install python-imaging
import math


def sobel(img):
    """ function from http://bitecode.co.uk/2008/07/edge-detection-in-python/ """
    if img.mode != "RGB":
        img = img.convert("RGB")
    out_image = Image.new(img.mode, img.size, None)
    imgdata = img.load()
    outdata = out_image.load()
 
    gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
 
    for row in xrange(1, img.size[0]-1):
        for col in xrange(1, img.size[1]-1):
            pixel_gx = pixel_gy = 0
            pxval = sum(imgdata[row,col])/3
            for i in range(-1, 2):
                for j in range(-1, 2):
                    val = sum(imgdata[row+i,col+j])/3
                    pixel_gx += gx[i+1][j+1] * val
                    pixel_gy += gy[i+1][j+1] * val
            newpixel = math.sqrt(pixel_gx * pixel_gx + pixel_gy * pixel_gy)
            newpixel = 255 - int(newpixel)
            outdata[row, col] = (newpixel, newpixel, newpixel)
    return out_image


# Canny edge detection using opencv
# http://en.wikipedia.org/wiki/Edge_detection#Canny_edge_detection
from opencv.cv import *
from opencv.highgui import *
def DoCanny(img, lowThresh, highThresh, aperature):
    """ from http://www.beechtreetech.com/dev/opencv-exercises-in-python.aspx -> example 2.6 """
    gray = cvCreateImage(cvSize(cvGetSize(img).width, cvGetSize(img).height), IPL_DEPTH_8U, 1)
    cvCvtColor(img,gray,CV_BGR2GRAY)
    
    if (gray.nChannels != 1):
        return False
    
    out = cvCreateImage(cvSize(cvGetSize(gray).width, cvGetSize(gray).height), IPL_DEPTH_8U, 1)
    cvCanny(gray, out, lowThresh, highThresh, aperature)
    return out
