"""
Gets pixels every X seconds and draws an image out of them.
A lazy Sunday afternoon hack!
"""

import time

import Image
import ImageGrab


X = 1 # seconds to pause before taking next pixel
size = 300 # the width=height of the image drawn, higher number = slower

if __name__ == '__main__':

    #start = time.time()
    
    pixels_img = Image.new('RGB', (size, size), 'black') # create a new Image instance
    pixels = pixels_img.load()
    
    for w in xrange(1, size):
        for h in xrange(1, size):
            img = ImageGrab.grab() # take a screenshot
            img = img.resize((size, size)) # create a thumbnail
            pixels[w, h] = img.getpixel((w, h)) # pixels(x, y) = (r, g, b)
            time.sleep(X)

    pixels_img.save('pixel.png', 'PNG')
    #print 'done'
    #print time.time() - start
