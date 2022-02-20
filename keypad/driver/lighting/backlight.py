import config

from digitalio import DigitalInOut, Direction


class Backlight(Task):
    def __init__(self):
        # Setup background LED's
        self.led = DigitalInOut(config.BACKLIGHT["LED_PIN"])
        self.led.direction = Direction.OUTPUT

    def advance(self, time_delta):
        self.led.value = True
