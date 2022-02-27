import config
# import pulseio

from task import Task
from digitalio import DigitalInOut, Direction


class Backlight(Task):
    SCHEDULE = { "update_time": 1, "priority": 1 }

    def __init__(self):
        # https://circuitpython.readthedocs.io/en/latest/shared-bindings/pulseio/#pulseio.PWMOut

        # Setup background LED's
        self.led = DigitalInOut(config.BACKLIGHT["LED_PIN"])
        self.led.direction = Direction.OUTPUT

    async def advance(self):
        self.led.value = True
