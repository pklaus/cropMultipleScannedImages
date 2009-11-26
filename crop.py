#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image # needs PIL: sudo aptitude install python-imaging
import detection

def cropMultipleScannedImages(image):
    coordinates = detection.getPictureCoordinates(image)
    pictures = []
    for i in coordinates:
        pictures.append(image.crop(i))    # http://www.pythonware.com/library/pil/handbook/image.htm -> crop
    return pictures
