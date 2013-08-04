"""
Gets pixels every X seconds and draws an image out of them.
A lazy Sunday afternoon hack!
"""

import time

import Image
import ImageGrab


X = 0 # seconds to pause before taking next pixel
WIDTH = 300 # the width of the image drawn, higher number = slower
HEIGHT = 300 # the height of the image drawn, higher number = slower

if __name__ == '__main__':

    #start = time.time()
    
    pixels_img = Image.new('RGB', (WIDTH, HEIGHT), 'black') # create a new Image instance
    pixels = pixels_img.load()
    
    for w in xrange(WIDTH):
        for h in xrange(HEIGHT):
            img = ImageGrab.grab() # take a screenshot
            img = img.resize((WIDTH, HEIGHT)) # create a thumbnail
            pixels[w, h] = img.getpixel((w, h)) # pixels(x, y) = (r, g, b)
            time.sleep(X)

    pixels_img.save('pixel.png', 'PNG')
    pixels_img.show()
    #print time.time() - start
