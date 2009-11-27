#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

#from opencv.cv import * # not needed here
from opencv.highgui import *
import detection
import Image # needs PIL: sudo aptitude install python-imaging
import pdb

def testFindLines():
    """ from chapter 2 of the book "Learning OpenCV: Computer Vision with the OpenCV Library", ISBN-10: 0596516134
        also found on http://www.beechtreetech.com/dev/opencv-exercises-in-python.aspx -> example 2.6 """
    
    
    cvNamedWindow("processed", CV_WINDOW_AUTOSIZE)
    cvNamedWindow("original", CV_WINDOW_AUTOSIZE)
    
    orig = cvLoadImage("photos_scanned_to_be_separated_small_brighter.png")
    cvShowImage("original", orig)
    lineScanResult = detection.findLines(orig)
    cvShowImage("processed", lineScanResult[1])
    #pdb.set_trace()
    detection.guessPictureCoordinates(lineScanResult[0],(1000,1000))
    
    loop = True
    while(loop):
        char = cvWaitKey(0)
        if (char != -1):
            if (ord(char) == 27):
                loop = False
    
    g_capture = cvCreateFileCapture('sample.avi')
    frames = long(cvGetCaptureProperty(g_capture, CV_CAP_PROP_FRAME_COUNT))
    
    loop = True
    while(loop):
        frame = cvQueryFrame(g_capture)
        if (frame == None):
            break
        cvShowImage("original", frame)
        outCan = detection.findLines(frame)[1]
        cvShowImage("processed", outCan)
        
        char = cvWaitKey(0)
        if (char != -1):
            if (ord(char) == 27):
                loop = False
    
    
    cvDestroyWindow("original")
    cvDestroyWindow("processed")


if __name__ == '__main__':
    testFindLines()

