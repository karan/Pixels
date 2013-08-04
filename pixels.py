"""
Gets pixels every X seconds and draws an image out of them.
"""

import ImageGrab
from collections import defaultdict
from time import sleep


X = 5 # seconds to pause before taking next pixel

if __name__ == '__main__':

    data = defaultdict(tuple) # {(x, y): (r, g, b), ...}
    
    for w in xrange(100):
        for h in xrange(100):
            img = ImageGrab.grab() # take a screenshot
            img = img.resize((100, 100)) # create a thumbnail
            data[(w, h)] = img.getpixel((w, h))
            sleep(X)

    print data
