import math
import config
import neopixel

from task import Task

# from adafruit_led_animation.animation.pulse import Pulse
# from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
# from adafruit_led_animation.animation.rainbowcomet import RainbowComet
# from adafruit_led_animation.animation.rainbowchase import RainbowChase
# from adafruit_led_animation.animation.rainbow import Rainbow
# from adafruit_led_animation.animation.colorcycle import ColorCycle


class Neopixel(Task):
    def __init__(self, encoders):
        self.encoders = encoders

        # Setup RGB LED's
        self.pixels = neopixel.NeoPixel(config.RGB_LIGHTS["DATA_PIN"], config.RGB_LIGHTS["COUNT"], brightness=config.RGB_LIGHTS["BRIGHTNESS"], auto_write=False)

        # self.pixel_animation = Pulse(self.pixels, 0.1, (255, 0, 0))
        # self.pixel_animation = RainbowSparkle(self.pixels, 0.1)
        # self.pixel_animation = RainbowComet(self.pixels, 0.1, 2)
        # self.pixel_animation = RainbowChase(self.pixels, 0.1)
        # self.pixel_animation = ColorCycle(self.pixels, 1.0, ((255, 0, 0), (255, 40, 0), (255, 150, 0), (0, 255, 0), (0, 0, 255), (180, 0, 255)))
        # self.pixel_animation = Rainbow(self.pixels, 0.05)

    def hsv_to_rgb(self, h, s, v):
        # https://stackoverflow.com/a/26856771/3593881

        rgb = None
        if s == 0.0: rgb = (v, v, v)
        i = int(h*6.) # XXX assume int() truncates!
        f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
        if i == 0: rgb = (v, t, p)
        if i == 1: rgb = (q, v, p)
        if i == 2: rgb = (p, v, t)
        if i == 3: rgb = (p, q, v)
        if i == 4: rgb = (t, p, v)
        if i == 5: rgb = (v, p, q)

        return int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)

    def advance(self, time_delta):
        # self.pixel_animation.draw()
        # self.pixel_animation.show()

        self.pixels.brightness = ((self.encoders.state[1] + 12) % 24) / 24

        hue = (self.encoders.state[0] % 64) / 64
        saturation = 1
        value = 1

        rgb = self.hsv_to_rgb(hue, saturation, value)

        self.pixels.fill(rgb)
        self.pixels.show()
