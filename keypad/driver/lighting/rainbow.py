from neopixel import NeoPixel
from messaging import CommandBus
from lighting.program import LightingProgram

from adafruit_led_animation.animation.rainbow import Rainbow


class RainbowProgram(LightingProgram):
    def __init__(self, pixels: NeoPixel, command_bus: CommandBus):
        self.pixel_animation = Rainbow(pixels, 0.05)

    def advance(self, time_delta):
        self.pixel_animation.draw()
        self.pixel_animation.show()
