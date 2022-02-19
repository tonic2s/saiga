import time
import config

from watchdog import Watchdog
from keyboard import SaigaKeyboard
from lighting.accent import Neopixel
from lighting.backlight import Backlight
from scheduler import Scheduler


scheduler = Scheduler(time.monotonic)


if config.WATCHDOG.ENABLED:
    # Reset system if broken
    scheduler.register_task(Watchdog(config.WATCHDOG.TIMEOUT), **config.WATCHDOG.SCHEDULE)

# Setup keyboard device
scheduler.register_task(SaigaKeyboard(), **config.KEYBOARD.SCHEDULE)

# RGB Neopixel
scheduler.register_task(Neopixel(), **config.RGB_LIGHTS.SCHEDULE)

# Single key LEDs
scheduler.register_task(Backlight(), **config.BACKLIGHT.SCHEDULE)


scheduler.start()
