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
def DoCanny(img, lowThresh, highThresh, aperature):
    """ from chapter 2 of the book "Learning OpenCV: Computer Vision with the OpenCV Library", ISBN-10: 0596516134
        also found on http://www.beechtreetech.com/dev/opencv-exercises-in-python.aspx -> example 2.6 """
    gray = cvCreateImage(cvSize(cvGetSize(img).width, cvGetSize(img).height), IPL_DEPTH_8U, 1)
    cvCvtColor(img,gray,CV_BGR2GRAY)
    
    if (gray.nChannels != 1):
        return False
    
    out = cvCreateImage(cvSize(cvGetSize(gray).width, cvGetSize(gray).height), IPL_DEPTH_8U, 1)
    cvCanny(gray, out, lowThresh, highThresh, aperature)
    return out


# corner detection using opencv
from opencv.cv import *
def DoCorner(image):
    """ from http://opencv.willowgarage.com/documentation/python/image_processing.html#gradients-edges-and-corners """
    # yet to implement!
    # nice basic examples for python on http://opencv.willowgarage.com/wiki/PythonInterface
    
    return image


def getPictureCoordinates(image):
    
    # proposal for an algorithm: http://www.delphigroups.info/2/5/315424.html -> Mattias Andersson, 2005-04-30 03:32:39 AM
    
    
    pictureCoordinates = []
    for i in range(3):
        x_0=100
        y_0=(200*i)+50
        x_1=300
        y_1=(200*i)+150
        box = (x_0,y_0,x_1,y_1)
        pictureCoordinates.append(box)
    return pictureCoordinates



from opencv.cv import *
import math
import pdb

def findLines(image):

    # inspiration: Neural Units with Higher-Order Synaptic Operations for Robotic Image Processing Applications
    # downloaded here: http://www.springerlink.com.proxy.ub.uni-frankfurt.de/content/16573jn623915320/?p=75fd611d62cd4eb483977d1de039e3b4&pi=1
    # using edge detection and Hough transform to process the edge detection results
    
    gray = cvCreateImage(cvSize(cvGetSize(image).width, cvGetSize(image).height), IPL_DEPTH_8U, 1)
    cvCvtColor(image,gray,CV_BGR2GRAY)
    if (gray.nChannels != 1):
        return False
    
    dst = cvCreateImage( cvGetSize(image), 8, 1 )
    color_dst = cvCreateImage( cvGetSize(image), 8, 3 )
    storage = cvCreateMemStorage(0)
    lines = 0
    i=0
    cvCanny( gray, dst, 50, 200, 3 )
    cvCvtColor( dst, color_dst, CV_GRAY2BGR )
    #pdb.set_trace()
    # Hough transform using openCV: http://opencv.willowgarage.com/documentation/python/image_processing.html#HoughLines2
    # parameters of cvHoughLines2:
    #                    image; line_storage;     method;       rho; theta; threshold; param1; param2
    lines = cvHoughLines2( dst, storage, CV_HOUGH_PROBABILISTIC, 1, CV_PI/180, 80, 30, 10 )
    for line in lines:
        cvLine( color_dst, line[0], line[1], CV_RGB(255,0,0), 3, 8 )
    return [storage,color_dst]



