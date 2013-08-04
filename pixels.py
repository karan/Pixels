"""
Gets pixels every X minutes and draws an image out of them.
"""

import ImageGrab
from collections import defaultdict
from time import sleep

if __name__ == '__main__':

    img = ImageGrab.grab() # take a screenshot
    img = img.resize((100, 100)) # create a thumbnail
    (width, height) = img.size # get the image (screen) size

    data = defaultdict(tuple) # {(x, y): (r, g, b), ...}
    
    for w in xrange(100):
        for h in xrange(100):
            data[(w, h)] = img.getpixel((w, h))

    print data
