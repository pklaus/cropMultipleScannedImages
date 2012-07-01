#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image # needs PIL: sudo aptitude install python-imaging
import math
import numpy as np
import cv2
import pdb

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
def DoCanny(img, lowThresh, highThresh, aperature):
    """ from chapter 2 of the book "Learning OpenCV: Computer Vision with the OpenCV Library", ISBN-10: 0596516134
        also found on http://www.beechtreetech.com/dev/opencv-exercises-in-python.aspx -> example 2.6 """
    gray = cv2.createImage(cvSize(cvGetSize(img).width, cvGetSize(img).height), IPL_DEPTH_8U, 1)
    cv2.cvtColor(img,gray,cv2.CV_BGR2GRAY)
    if (gray.nChannels != 1):
        return False
    out = cv2.Canny(gray, lowThresh, highThresh, aperature)
    return out

# corner detection using opencv
def DoCorner(image):
    """ from http://opencv.willowgarage.com/documentation/python/image_processing.html#gradients-edges-and-corners """
    # yet to implement!
    # nice basic examples for python on http://opencv.willowgarage.com/wiki/PythonInterface
    raise NotImplementedError()

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

class Vector(object):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return repr(self.data)
    def __add__(self, other):
        data = []
        for j in range(len(self.data)):
          data.append(self.data[j] + other.data[j])
        return Vector(data)
    def __sub__(self, other):
        data = []
        for j in range(len(self.data)):
          data.append(self.data[j] - other.data[j])
        return Vector(data)
    def __mul__(self, other):
        scalarProduct = 0
        for j in range(len(self.data)):
          scalarProduct += self.data[j] * other.data[j]
        return scalarProduct
    def length(self):
        squaredSum=0
        for j in range(len(self.data)):
            squaredSum += self.data[j]**2
        return math.sqrt(squaredSum)

def guessPictureCoordinates(lines, imageDimensions, maxCheck=10):
    """ may replace getPictureCoordinates """
    lines.sort()
    lines.reverse()

    counter = 0
    limit = maxCheck if maxCheck<len(lines) else len(lines)
    importantLines=[]
    pictureCoordinates = []
    alreadyMatched=[]
    for line in lines:
        #pdb.set_trace()
        # check scalar product with other lines:
        for j in range(limit):
            if [counter,j] in alreadyMatched or [j,counter] in alreadyMatched:
                continue
            v1=lines[j][1]-lines[j][2]
            v2=line[1]-line[2]
            cosphi=float(v1*v2)/(float(v1.length())*float(v2.length()))-.000000000000001
            #print cosphi,
            angle = math.acos(cosphi)
            #print angle
            if abs(angle-math.acos(0))<0.05:
                alreadyMatched.append([counter,j])
                importantLines.append([line,lines[j]])
                #if line not in importantLines: importantLines.append(line)
                #if lines[j] not in importantLines: importantLines.append(lines[j])
        box = (50,50,100,100)
        pictureCoordinates.append(box)
        if counter==limit-1: break
        counter+=1
    print importantLines
    return pictureCoordinates

def findLines(image):
    # inspiration: Neural Units with Higher-Order Synaptic Operations for Robotic Image Processing Applications
    # downloaded here: http://www.springerlink.com.proxy.ub.uni-frankfurt.de/content/16573jn623915320/?p=75fd611d62cd4eb483977d1de039e3b4&pi=1
    # using edge detection and Hough transform to process the edge detection results http://danthorpe.me.uk/blog/2005/02/24/Implementing_the_Hough_Transform
    gray = np.empty((image.shape[0],image.shape[1],1), np.uint8)
    import cv
    gray = cv2.cvtColor(image,cv.CV_BGR2GRAY)
    dst = np.empty((image.shape[0],image.shape[1],1), np.uint8)
    #color_dst = np.empty((image.shape[0],image.shape[1],3), np.uint8)
    color_dst = np.empty(image.shape, np.uint8)
    lines = 0
    i=0
    dst = cv2.Canny( gray, 50, 200 )
    color_dst = cv2.cvtColor( dst, cv.CV_GRAY2BGR )
    # Hough transform using openCV
    # http://docs.opencv.org/modules/imgproc/doc/feature_detection.html?highlight=cv2.houghlinesp#cv2.HoughLinesP
    lines = cv2.HoughLinesP(dst, 1, 3.14/180, 80)
    ## calculate length and sort by length:
    l = []
    try:
        for line in lines[0]:
            length = math.sqrt((line[0]-line[2])**2+(line[1]-line[3])**2)
            l.append([length, Vector([line[0], line[2]]), Vector([line[1], line[3]])])
            cv2.line( color_dst, (line[0], line[1]), (line[2], line[3]), (255,0,0), 3, 8 )
        l.sort()
        l.reverse()
    except:
        pass
    return (l,color_dst)
