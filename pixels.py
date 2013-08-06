"""
Gets pixels every X seconds and draws an image out of them.
A lazy Sunday afternoon hack!
"""

import time

import Image
import pyscreenshot as ImageGrab


if __name__ == '__main__':

    start = time.time()

    X = input('How many seconds to wait between each screenshot (seconds)?: ')
    width = input('Width of the image to make (0 for max): ')
    height = input('Height of the image to make (0 for max): ')

    img = ImageGrab.grab() # take a screenshot
    
    if width == 0:
        width = img.size[0]
    if height == 0:
        height = img.size[1]
    
    pixels_img = Image.new('RGB', (width, height), 'black') # create a new Image instance
    pixels = pixels_img.load()
    
    for w in xrange(width):
        img = ImageGrab.grab() # take a screenshot
        img = img.resize((width, height)) # create a thumbnail
        for h in xrange(height):
            pixels[w, h] = img.getpixel((w, h)) # pixels(x, y) = (r, g, b)
        time.sleep(X)

    pixels_img.save('pixel.png', 'PNG')
    pixels_img.show()

    print 'Completed in %fs' % (time.time() - start)
