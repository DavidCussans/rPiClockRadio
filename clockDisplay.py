from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

import datetime
import time
import os
import logging

class clockDisplay:
    """Display text on GFX Hat"""

    def __init__(self):
        self.timeFont = ImageFont.truetype(fonts.FredokaOne, 38)
        self.infoFont = ImageFont.truetype(fonts.FredokaOne, 20)
        #self.width, self.timeHeight = lcd.dimensions()
        self.totalWidth, self.totalHeight = [128,64]
        self.timeWidth, self.timeHeight = self.timeFont.getsize("88:88")
        self.infoWidth, self.infoHeight = self.infoFont.getsize("88:88:88")
        self.volWidth, self.volHeight = [10,64]
        self.volXoffset , self.volYoffset = [self.totalWidth-self.volWidth,0]
        logging.info("clockDisplay width, height = {} , {}".format( self.timeWidth, self.timeHeight) )
        
    def drawTime(self):
        """Draw text showing current time on screen"""
        self.image = Image.new('1', (self.timeWidth, self.timeHeight))
        self.draw = ImageDraw.Draw(self.image)

        now = datetime.datetime.now()
        text = now.strftime("%H:%M")

        w, h = self.timeFont.getsize(text)

        #x = (self.timeWidth - w) // 2
        #y = (self.timeHeight - h) // 2
        x = 0
        y = 0
        
        self.draw.text((x, y), text, 1, self.timeFont)

        for x in range(self.timeWidth):
            for y in range(self.timeHeight):
                pixel = self.image.getpixel((x, y))
                lcd.set_pixel(x, y, pixel)
        lcd.contrast(38)
        lcd.show()

    def drawVolume(self,volume):
        """Draw box at right hand of screen to represent current volume"""
        self.volImage = Image.new('1', (self.volWidth, self.volHeight))
        self.volDraw  = ImageDraw.Draw(self.volImage)
        print ("volume = %d"%(volume))
        self.volDraw.polygon([ (0,0) ,  (0 , self.volHeight*volume/100), (self.volWidth , self.volHeight*volume/100),  (self.volWidth , 0) ] , fill="#ffffff")

        for x in range(self.volWidth):
            for y in range(self.volHeight):
                pixel = self.volImage.getpixel((x, y))
                print(x,y,pixel)
                lcd.set_pixel(self.volXoffset + x, self.volYoffset + y, pixel)
        lcd.contrast(38)
        lcd.show()

    def drawInfo(self,info):
        """Draw text with current channel at bottom of screen"""
        
