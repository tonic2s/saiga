import config

from neopixel import NeoPixel
from lighting.program import LightingProgram
from messaging import CommandBus, InputType, CommandType


class ConfigurableHue(LightingProgram):
    def __init__(self, pixels: NeoPixel, command_bus: CommandBus):
        # Setup command handing
        self.command_reader = command_bus.subscribe()

        # Color state
        self.hue = config.RGB_LIGHTS["DEFAULT_HUE"]
        self.saturation = 1

        # Setup RGB LED's
        self.pixels = pixels
        self.update_color()

    def hsv_to_rgb(self, hue, saturation, value):
        # Source: https://stackoverflow.com/a/26856771/3593881

        rgb = None
        if saturation == 0.0: rgb = (value, value, value)
        i = int(hue*6.) # assume int() truncates!
        f = (hue*6.)-i; p,q,t = value*(1.-saturation), value*(1.-saturation*f), value*(1.-saturation*(1.-f)); i%=6
        if i == 0: rgb = (value, t, p)
        if i == 1: rgb = (q, value, p)
        if i == 2: rgb = (p, value, t)
        if i == 3: rgb = (p, q, value)
        if i == 4: rgb = (t, p, value)
        if i == 5: rgb = (value, p, q)

        return int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)

    def update_color(self):
        color = self.hsv_to_rgb(self.hue, self.saturation, 1)

        self.pixels.fill(color)
        self.pixels.show()

    def advance(self):
        for command in self.command_reader:
            if command.type == CommandType.BRIGHTNESS_CHANGE:
                self.pixels.brightness = max(0, min(1, self.pixels.brightness + command.metadata["delta"]))
                self.pixels.show()

            if command.type == CommandType.HUE_CHANGE:
                self.hue = (self.hue + command.metadata["delta"]) % 1

                self.update_color()
            if command.type == CommandType.SATURATION_CHANGE:
                self.saturation = max(0, min(1, self.saturation + command.metadata["delta"]))

                self.update_color()

    def deinit(self):
        self.command_reader.unsubscribe()
