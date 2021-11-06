from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

import datetime
import time
import os
import logging
import config

class buttonActions:
    """Set up handler to respond to button presses"""

    def __init__(self,config,display):
        # self.playing = False
        self.myConfig = config
        self.myDisplay = display
        
        for x in range(6):
            backlight.set_pixel(x, 0, 128, 0)

        backlight.show()

        def handlerVolumeUp(ch, event):
            if event == 'press':
                logging.info("Volume Up")
                volume = self.myConfig.getVolume()
                volume = volume + 5
                os.system("mpc volume %d"%(volume))
                self.myDisplay.drawVolume(volume)
                self.myConfig.setVolume(volume)
                
        def handlerVolumeDown(ch, event):
            if event == 'press':
                logging.info("Volume Down")
                volume = self.myConfig.getVolume()
                volume = volume - 5
                os.system("mpc volume %d"%(volume))
                self.myDisplay.drawVolume(volume)
                self.myConfig.setVolume(volume)                

        def handler2(ch, event):
            if event == 'press':
                logging.info("Press on button 2")

        def handler3(ch, event):
            if event == 'press':
                logging.info("Press on button 3")

        def handlerOnOff(ch, event):
            if event == 'press':
                if not self.myConfig.getPlayState(): # if 
                    logging.info("On")
                    #os.system("mpc play")
                    self.myConfig.setPlayState(True)
                    self.setPlaying(self.myConfig.getPlayState() )
                else:
                    logging.info("Off")
                    #os.system("mpc stop")
                    self.myConfig.setPlayState(False)
                    self.setPlaying(self.myConfig.getPlayState() )
                    
        def handlerOff(ch, event):
            if event == 'press':
                logging.info("Off")
                os.system("mpc stop")



        logging.info("Registering button handlers....")
        touch.on(0,handlerVolumeUp)
        touch.on(1,handlerVolumeDown)
        touch.on(2,handler2)
        touch.on(3,handler3)
        touch.on(4,handlerOnOff)
        touch.on(5,handlerOff)

        self.setPlaying(True)
        
    def setPlaying(self,playState):
        logging.info("setting playing state to {}".format(playState) )
        if playState:
            os.system("mpc play")
        else:
            os.system("mpc stop")
