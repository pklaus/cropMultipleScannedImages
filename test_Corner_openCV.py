#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

#from opencv.cv import * # not needed here
from opencv.highgui import *
import detection


def testOpenCVcornerDetection():
    cvNamedWindow("corner detection", CV_WINDOW_AUTOSIZE)
    cvNamedWindow("original", CV_WINDOW_AUTOSIZE)
    g_capture = cvCreateFileCapture('sample.avi')
    frames = long(cvGetCaptureProperty(g_capture, CV_CAP_PROP_FRAME_COUNT))
    
    loop = True
    
    while(loop):
        frame = cvQueryFrame(g_capture)
        if (frame == None):
            break
        cvShowImage("original", frame)
        outCorner = detection.DoCorner(frame)
        cvShowImage("corner detection", outCorner)
        
        char = cvWaitKey(0)
        if (char != -1):
            if (ord(char) == 27):
                loop = False
    
    
    cvDestroyWindow("original")
    cvDestroyWindow("corner detection")


if __name__ == '__main__':
    testOpenCVcornerDetection()

