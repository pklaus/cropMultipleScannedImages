#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image # needs PIL: sudo aptitude install python-imaging
import crop


def testCrop():
    counter = 0
    for i in crop.cropMultipleScannedImages(Image.open("photos_scanned_to_be_separated_small_brighter.png")):
        i.save("cropped%s.jpg" % counter)
        counter += 1

if __name__ == '__main__':
    testCrop()

