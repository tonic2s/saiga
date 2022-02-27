import time
import config
import asyncio

from messaging import MessageBus
from mediator import MessageCommandMediator

from providers.encoder import RotaryEncoderProvider
from providers.keyboard import AsyncKeyboardProvider

from consumers.accent import Neopixel
# from consumers.backlight import Backlight
from consumers.statuslight import StatusLight
from consumers.watchdog_timer import Watchdog
from consumers.keyboard import USBKeyboardDevice
from consumers.animation import NeopixelAnimation
from consumers.logger import FileLogger, ConsoleLogger


message_bus = MessageBus()

tasks = [
    message_bus,

    # FileLogger(message_bus),
    ConsoleLogger(message_bus),

    AsyncKeyboardProvider(message_bus),
    USBKeyboardDevice(message_bus),

    RotaryEncoderProvider(message_bus),


    StatusLight(message_bus),

    # Backlight(),

    Neopixel(message_bus)
    # NeopixelAnimation(message_bus)
]

# Reset system if broken
if config.WATCHDOG["ENABLED"]:
    print("watchdog is enbled")
    tasks.append(Watchdog())

# Set asyncio exception handler
def loop_exception_handler(loop, context):
    print("uncought exception", loop, context)
asyncio.get_event_loop().set_exception_handler(loop_exception_handler)

# Create tasks and start core event loop
asyncio_tasks = [asyncio.create_task(task._advance()) for task in tasks]
asyncio.run(asyncio.gather(*asyncio_tasks, return_exceptions=False))
