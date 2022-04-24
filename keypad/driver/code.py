import config
import asyncio
import traceback

from messaging import CommandBus

from inputs.encoder import RotaryEncoderInput
from inputs.keyboard import KeyboardInput

from tasks.accent import AccentLight
from tasks.statuslight import StatusLight
from tasks.keyboard import USBKeyboardDevice
from tasks.logger import FileLogger, ConsoleLogger


# Setup tasks for execution
try:
    command_bus = CommandBus()

    tasks = [
        command_bus,

        # FileLogger(command_bus),
        ConsoleLogger(command_bus),

        KeyboardInput(command_bus),
        USBKeyboardDevice(command_bus),

        RotaryEncoderInput(command_bus),

        StatusLight(command_bus),

        AccentLight(command_bus),
    ]

    if config.CONSUMER_CONTROL["ENABLED"]:
        from tasks.consumer_control import ConsumerControlDevice
        tasks.append(ConsumerControlDevice(command_bus))

    if config.BACKLIGHT["ENABLED"]:
        from tasks.backlight import Backlight
        tasks.append(Backlight())

    # Reset system if broken
    if config.WATCHDOG["ENABLED"]:
        from tasks.watchdog_timer import Watchdog
        print("watchdog is enbled")
        tasks.append(Watchdog())

    # Set asyncio exception handler
    def loop_exception_handler(loop, context):
        print("Uncaught exception", loop, context)
    asyncio.get_event_loop().set_exception_handler(loop_exception_handler)

    # Create tasks and start core event loop
    asyncio_tasks = [task._advance() for task in tasks]
    asyncio.run(asyncio.gather(*asyncio_tasks, return_exceptions=False))

except Exception as e:
    print("INIT EXCEPTION", traceback.format_exception(BaseException, e, e.__traceback__))
