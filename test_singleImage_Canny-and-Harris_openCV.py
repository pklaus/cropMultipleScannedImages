#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image
import os
import sys
from opencv.cv import *
from opencv.highgui import *

def analyzeImage(f,name):
    """ http://pythonimage.blogspot.com/2009/04/opencv-example.html """
    im=Image.open(f)
    try:
        if(im.size[0]==1 or im.size[1]==1):
            return
        print (name+' : '+str(im.size[0])+','+ str(im.size[1]))
        le=1
        if(type(im.getpixel((0,0)))==type((1,2))):
            le=len(im.getpixel((0,0))) 
        gray = cvCreateImage (cvSize (im.size[0], im.size[1]), 8, 1)
        edge1 = cvCreateImage (cvSize (im.size[0], im.size[1]), 32, 1)
        edge2 = cvCreateImage (cvSize (im.size[0], im.size[1]), 8, 1)
        edge3 = cvCreateImage (cvSize (im.size[0], im.size[1]), 32, 3)

        for h in range(im.size[1]):
            for w in range(im.size[0]):
                p=im.getpixel((w,h))
                if(type(p)==type(1)):
                    gray[h][w] = im.getpixel((w,h))
                else:
                    gray[h][w] = im.getpixel((w,h))[0]

        cvCornerHarris(gray,edge1,5,5,0.1)
        cvCanny(gray,edge2,20,100)

        cvNamedWindow("original gray")
        cvShowImage("original gray", gray);
        cvNamedWindow("CornerHarris")
        cvShowImage("CornerHarris", edge1);
        cvNamedWindow("CannyEdge")
        cvShowImage("CannyEdge", edge2);

        cvWaitKey()

        f.close()
    except Exception,e:
        print e
        print 'ERROR: problem handling '+ name


f = open(sys.argv[1],'r')
analyzeImage(f,sys.argv[1])

