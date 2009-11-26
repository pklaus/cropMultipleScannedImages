#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.klaus AT gmail.com

import Image # for Image.open()
import detection

def main():
    im = Image.open("photos_scanned_to_be_separated_small_brighter.png")
    #im.show()
    im_edges = detection.sobel(im)
    im_edges.show()

if __name__ == '__main__':
    main()
