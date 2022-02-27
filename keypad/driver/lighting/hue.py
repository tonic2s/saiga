import config

from neopixel import NeoPixel
from lighting.program import LightingProgram
from messaging import MessageBus, MessageType, CommandType


class ConfigurableHue(LightingProgram):
    def __init__(self, pixels: NeoPixel, message_bus: MessageBus):
        self.pixels = pixels

        # Setup message handing
        self.message_reader = message_bus.subscribe()

        # Setup RGB LED's
        self.pixels.fill(self.hsv_to_rgb(config.RGB_LIGHTS["DEFAULT_HUE"], 1, 1))
        self.pixels.show()

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

    def advance(self):
        for message in self.message_reader:
            if message.type == MessageType.COMMAND and message.command == CommandType.HUE_SET:
                color = self.hsv_to_rgb(message.metadata["hue"], 1, 1)

                self.pixels.fill(color)
                self.pixels.show()

    def deinit(self):
        self.message_reader.unsubscribe()
