from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

import datetime
import time
import os
import logging

class clockDisplay:
    """Display text on GFX Hat"""

    def __init__(self):
        self.font = ImageFont.truetype(fonts.FredokaOne, 38)
        #self.width, self.height = lcd.dimensions()
        self.width, self.height = self.font.getsize("88:88")
        logging.info("clockDisplay width, height = {} , {}".format( self.width, self.height) )
        
    def drawTime(self):
        self.image = Image.new('P', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

        now = datetime.datetime.now()
        text = now.strftime("%H:%M")

        w, h = self.font.getsize(text)

        #x = (self.width - w) // 2
        #y = (self.height - h) // 2
        x = 0
        y = 0
        
        self.draw.text((x, y), text, 1, self.font)

        for x in range(self.width):
            for y in range(self.height):
                pixel = self.image.getpixel((x, y))
                lcd.set_pixel(x, y, pixel)
        lcd.contrast(38)
        lcd.show()
