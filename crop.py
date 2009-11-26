#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image # needs PIL: sudo aptitude install python-imaging
import detection

def cropMultipleScannedImages(image):
    
    # two notes here:
    #    - presumably we need corner detection here, not edge detection!!!
    #      http://cs223b.stanford.edu/notes/CS223B-L3-Features.ppt found here:
    #      http://stackoverflow.com/questions/1391212/best-articles-to-start-learning-about-edge-detection-image-recognition/1394450#1394450
    #    - when we have the corners, we still have to find out, which corners belong together and to rotate the images accordingly!
    
    coordinates = detection.getPictureCoordinates(image)
    pictures = []
    for i in coordinates:
        pictures.append(image.crop(i))    # http://www.pythonware.com/library/pil/handbook/image.htm -> crop
    return pictures
