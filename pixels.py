"""
Gets pixels every X minutes and draws an image out of them.
"""

import ImageGrab
from collections import defaultdict

if __name__ == '__main__':

    img = ImageGrab.grab() # take a screenshot
    (width, height) = img.size # get the image (screen) size

    data = defaultdict(tuple) # {(x, y): (r, g, b), ...}
    
    for w in xrange(width):
        for h in xrange(height):
            data[(w, h)] = img.getpixel((w, h))

    print data
