#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

#from opencv.cv import * # not needed here
from opencv.highgui import *
import detection


def testOpenCVedgeDetection():
    """ from chapter 2 of the book "Learning OpenCV: Computer Vision with the OpenCV Library", ISBN-10: 0596516134
        also found on http://www.beechtreetech.com/dev/opencv-exercises-in-python.aspx -> example 2.6 """
    
    cvNamedWindow("Canny", CV_WINDOW_AUTOSIZE)
    cvNamedWindow("original", CV_WINDOW_AUTOSIZE)
    g_capture = cvCreateFileCapture('sample.avi')
    frames = long(cvGetCaptureProperty(g_capture, CV_CAP_PROP_FRAME_COUNT))
    
    loop = True
    
    while(loop):
        frame = cvQueryFrame(g_capture)
        if (frame == None):
            break
        cvShowImage("original", frame)
        outCan = detection.DoCanny(frame, 70.0, 140.0, 3)
        cvShowImage("Canny", outCan)
        
        char = cvWaitKey(0)
        if (char != -1):
            if (ord(char) == 27):
                loop = False
    
    
    cvDestroyWindow("original")
    cvDestroyWindow("Canny")


if __name__ == '__main__':
    testOpenCVedgeDetection()

