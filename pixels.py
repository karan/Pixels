"""
Gets pixels every X seconds and draws an image out of them.
"""

import time
from collections import defaultdict

import Image
import ImageGrab
import ImageDraw


X = 0 # seconds to pause before taking next pixel

if __name__ == '__main__':

    start = time.time()
    
    data = defaultdict(tuple) # {(x, y): (r, g, b), ...}

    pixels_img = Image.new('RGB', (200, 200), 'black') # create a new Image instance
    pixels = pixels_img.load()
    
    for w in xrange(1, 200):
        for h in xrange(1, 200):
            img = ImageGrab.grab() # take a screenshot
            img = img.resize((200, 200)) # create a thumbnail
            #data[(w, h)] = img.getpixel((w, h))
            pixels[w, h] = img.getpixel((w, h))

    pixels_img.save('pixel.png', 'PNG')
    print 'done'
    print time.time() - start
