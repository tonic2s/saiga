import time
import config

# from my_watchdog import Watchdog
from encoder import RotaryEncoder
from keyboard import SaigaKeyboard
from lighting.accent import Neopixel
# from lighting.backlight import Backlight
from scheduler import Scheduler


scheduler = Scheduler(time.monotonic)


# if config.WATCHDOG["ENABLED"]:
#     # Reset system if broken
#     scheduler.register_task(Watchdog(), **config.WATCHDOG["SCHEDULE"])

# Setup keyboard device
scheduler.register_task(SaigaKeyboard(), **config.KEYBOARD["SCHEDULE"])

# Setup rotary encoders
encoder_task = RotaryEncoder()
scheduler.register_task(encoder_task, **config.ENCODERS["SCHEDULE"])

if config.RGB_LIGHTS["ENABLED"]:
    # RGB Neopixel
    scheduler.register_task(Neopixel(encoder_task), **config.RGB_LIGHTS["SCHEDULE"])

# if config.BACKLIGHT["ENABLED"]:
#     # Single key LEDs
#     scheduler.register_task(Backlight(), **config.BACKLIGHT["SCHEDULE"])


scheduler.start()
