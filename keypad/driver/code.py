import time
import config

from consumers.accent import Neopixel
# from consumers.backlight import Backlight
from consumers.statuslight import StatusLight
from consumers.watchdog_timer import Watchdog
from consumers.keyboard import USBKeyboardDevice
from consumers.animation import NeopixelAnimation
from consumers.logger import FileLogger, ConsoleLogger

from providers.encoder import RotaryEncoderProvider
from providers.keyboard import AsyncKeyboardProvider

from scheduler import Scheduler
from messaging import MessageBus


scheduler = Scheduler(time.monotonic)

message_bus = scheduler.register_task(MessageBus())

# Reset system if broken
if config.WATCHDOG["ENABLED"]:
    print("watchdog is enbled")
    scheduler.register_task(Watchdog())

# Setup keyboard device
scheduler.register_task(AsyncKeyboardProvider(message_bus))
scheduler.register_task(USBKeyboardDevice(message_bus))

# Setup rotary encoders
scheduler.register_task(RotaryEncoderProvider(message_bus))

# RGB Neopixel
scheduler.register_task(Neopixel(message_bus))
# scheduler.register_task(NeopixelAnimation(message_bus))

scheduler.register_task(StatusLight(message_bus))

scheduler.register_task(FileLogger(message_bus))
scheduler.register_task(ConsoleLogger(message_bus))

# Single key LEDs
# if config.BACKLIGHT["ENABLED"]:
#     scheduler.register_task(Backlight(), **config.BACKLIGHT["SCHEDULE"])

try:
    scheduler.start()
except Exception as e:
    print("critical error", str(e))
