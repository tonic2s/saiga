import config
import neopixel

from task import Task
from messaging import MessageBus, MessageType, CommandType


class Neopixel(Task):
    UPDATE_TIME = 0.1

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_reader = message_bus.subscribe()

        # Setup RGB LED's
        self.brightness = config.RGB_LIGHTS["BRIGHTNESS"]

        self.pixels = neopixel.NeoPixel(config.RGB_LIGHTS["DATA_PIN"], config.RGB_LIGHTS["COUNT"], brightness=self.brightness, auto_write=False)

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

    async def advance(self):
        for message in self.message_reader:
            if message.type == MessageType.COMMAND and message.command == CommandType.HUE_SET:
                color = self.hsv_to_rgb(message.metadata["hue"], 1, 1)

                self.pixels.fill(color)
                self.pixels.show()

            elif message.type == MessageType.COMMAND and message.command == CommandType.BRIGHTNESS_SET:
                self.brightness = min(1.0, max(0.0, message.metadata["value"]))
                self.pixels.brightness = self.brightness
                self.pixels.show()

            elif message.type == MessageType.COMMAND and message.command == CommandType.BRIGHTNESS_UP:
                self.brightness = min(1.0, self.brightness + 0.1)
                self.pixels.brightness = self.brightness
                self.pixels.show()

            elif message.type == MessageType.COMMAND and message.command == CommandType.BRIGHTNESS_DOWN:
                self.brightness = max(0.0, self.brightness - 0.1)
                self.pixels.brightness = self.brightness
                self.pixels.show()
