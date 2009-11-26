#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

#from opencv.cv import * # not needed here
from opencv.highgui import *
import detection

if __name__ == '__main__':

    cvNamedWindow("Example5-Canny", CV_WINDOW_AUTOSIZE)

    cvNamedWindow("Example5", CV_WINDOW_AUTOSIZE)
    g_capture = cvCreateFileCapture('sample.avi')
    frames = long(cvGetCaptureProperty(g_capture, CV_CAP_PROP_FRAME_COUNT))
      
    loop = True
    
    while(loop):

        frame = cvQueryFrame(g_capture)
        if (frame == None):
            break
        cvShowImage("Example5", frame)
        outCan = detection.DoCanny(frame, 70.0, 140.0, 3)
        cvShowImage("Example5-Canny", outCan)
        
        char = cvWaitKey(0)
        if (char != -1):
            if (ord(char) == 27):
                loop = False

    cvDestroyWindow("Example5")
    cvDestroyWindow("Example5-Canny")

