from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

import datetime
import time
import os

class buttonActions:
    """Set up handler to respond to button presses"""

    def __init__(self):
        self.playing = False

        for x in range(6):
            backlight.set_pixel(x, 0, 128, 0)

        backlight.show()

        def handlerVolumeUp(ch, event):
            if event == 'press':
                print ("Volume Up")
                os.system("mpc volume +5")

        def handlerVolumeDown(ch, event):
            if event == 'press':
                print ("Volume Up")
                os.system("mpc volume -5")        

        def handler2(ch, event):
            if event == 'press':
                print ("Press on button 2")

        def handler3(ch, event):
            if event == 'press':
                print ("Press on button 3")

        def handlerOnOff(ch, event):
            if event == 'press':
                if not self.playing: # if 
                    print ("On")
                    os.system("mpc play")
                    self.playing = True
                else:
                    print ("Off")
                    os.system("mpc stop")
                    self.playing = False

        def handlerOff(ch, event):
            if event == 'press':
                print ("Off")
                os.system("mpc stop")



        print("Registering button handlers....")
        touch.on(0,handlerVolumeUp)
        touch.on(1,handlerVolumeDown)
        touch.on(2,handler2)
        touch.on(3,handler3)
        touch.on(4,handlerOnOff)
        touch.on(5,handlerOff)

        os.system("mpc play")
        
