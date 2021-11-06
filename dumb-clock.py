#!/usr/bin/env python3

import datetime
import time
import signal
import os

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler

import clockDisplay

import buttonActions

import config

import logging

logFileName = "/var/log/rPiClockRadio/rPiClockRadio.log"

logging.basicConfig(filename=logFileName, level=logging.INFO)

logging.info("""hello-world.py

This basic example prints the text "Hello World" in the middle of the LCD

Press any button to see its corresponding LED toggle on/off.

Press Ctrl+C to exit.

""")

config = config.config()

#scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()

display = clockDisplay.clockDisplay()

buttons = buttonActions.buttonActions(config,display)

# start by displaying the minutes...
display.drawTime()

# Now schedule a job to update every minute
logging.info("Setting scheduler")
job = scheduler.add_job(display.drawTime, trigger='cron', minute='*')
scheduler.print_jobs()

logging.info("Pausing main thread by starting blocking scheduler")
scheduler.start()
logging.info("Whoops.... schduler.start didn't block")
