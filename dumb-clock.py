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

print("""hello-world.py

This basic example prints the text "Hello World" in the middle of the LCD

Press any button to see its corresponding LED toggle on/off.

Press Ctrl+C to exit.

""")

#scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()

display = clockDisplay.clockDisplay()

buttons = buttonActions.buttonActions()

# start by displaying the minutes...
display.drawTime()

# Now schedule a job to update every minute
print("Setting scheduler")
job = scheduler.add_job(display.drawTime, trigger='cron', minute='*')
scheduler.print_jobs()

print("Pausing main thread by starting blocking scheduler")
scheduler.start()
print("Whoops.... schduler.start didn't block")
