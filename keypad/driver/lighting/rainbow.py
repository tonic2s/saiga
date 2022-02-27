from neopixel import NeoPixel
from messaging import MessageBus
from lighting.program import LightingProgram

from adafruit_led_animation.animation.rainbow import Rainbow


class RainbowAnimation(LightingProgram):
    def __init__(self, pixels: NeoPixel, message_bus: MessageBus):
        self.pixel_animation = Rainbow(pixels, 0.05)

    def advance(self):
        self.pixel_animation.draw()
        self.pixel_animation.show()
