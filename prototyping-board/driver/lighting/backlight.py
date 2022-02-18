import config

from digitalio import DigitalInOut, Direction, Pull


class Backlight(Task):
    def __init__(self):
        # Setup background LED's
        self.leds = []

        for led_pin in config.BACKLIGHT.LED_PINS:
            led = DigitalInOut(led_pin)
            led.direction = Direction.OUTPUT

            self.leds.append(led)

        self.current_led_index = 0

    def advance(self, time_delta):
        background_led = self.leds[self.current_led_index]
        background_led.value = not background_led.value

        self.current_led_index = (self.current_led_index + 1) % len(self.leds)
