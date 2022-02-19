import time
import config
import neopixel

from task import Task

from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.colorcycle import ColorCycle


class Neopixel(Task):
    def __init__(self):
        # Setup RGB LED's
        self.pixels = neopixel.NeoPixel(config.RGB_LIGHTS.DATA_PIN, config.RGB_LIGHTS.COUNT, brightness=config.RGB_LIGHTS.BRIGHTNESS, auto_write=False)

        # self.pixel_animation = Pulse(self.pixels, 0.1, (255, 0, 0))
        # self.pixel_animation = RainbowSparkle(self.pixels, 0.1)
        # self.pixel_animation = RainbowComet(self.pixels, 0.1, 2)
        # self.pixel_animation = RainbowChase(self.pixels, 0.1)
        # self.pixel_animation = ColorCycle(self.pixels, 0.5, ((255, 0, 0), (255, 40, 0), (255, 150, 0), (0, 255, 0), (0, 0, 255), (180, 0, 255)))
        self.pixel_animation = Rainbow(self.pixels, 0.05)

    def advance(self, delta):
        self.pixel_animation.draw()
        self.pixel_animation.show()
