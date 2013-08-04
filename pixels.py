"""
Gets pixels every X minutes and draws an image out of them.
"""

import ImageGrab

if __name__ == '__main__':

    while True:
        img = ImageGrab.grab() # take a screenshot
        
