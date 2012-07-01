#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

#from opencv.cv import * # not needed here
import cv2
import cv
import detection
import Image # needs PIL: sudo aptitude install python-imaging
import os
import sys

import pdb

def key_continue():
    char = cv2.waitKey(0)
    if char != -1:
        if char == 27:
            return False
    return True

def do_n_display_line_detection(frame):
    cv2.imshow("original", frame)
    lines, processed_img = detection.findLines(frame)
    cv2.imshow("processed", processed_img)
    detection.guessPictureCoordinates(lines,(1000,1000))

if __name__ == '__main__':
    """ from chapter 2 of the book "Learning OpenCV: Computer Vision with the OpenCV Library", ISBN-10: 0596516134
        also found on http://www.beechtreetech.com/dev/opencv-exercises-in-python.aspx -> example 2.6 """

    cv2.namedWindow("processed")
    cv2.namedWindow("original")
    try:
        fn = os.path.abspath(sys.argv[1])
    except:
        print ("Usage: %s <image or video file>" % sys.argv[0]); sys.exit(1)

    fnl = fn.lower()

    if '.png' in fnl or '.jpg' in fnl:
        orig = cv2.imread(fn,-1)
        do_n_display_line_detection(orig)
        while key_continue(): pass
    elif '.avi' in fnl:
        vc = cv2.VideoCapture(fn)
        frames = long( vc.get(cv.CV_CAP_PROP_FRAME_COUNT) )
        loop = True
        while key_continue():
            successFlag, frame = vc.read()
            if frame == None: break
            do_n_display_line_detection(frame)
    else:
        raise NotImplementedError("Image or video format not added yet.")
