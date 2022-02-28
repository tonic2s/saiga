import config
import neopixel
import time
import random

from task import Task
from messaging import MessageBus, MessageType


class NeopixelFlag(Task):
    SCHEDULE = { "update_time": 0.01, "priority": 1 }

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_reader = message_bus.subscribe()

        # Setup RGB LED's
        self.brightness = config.RGB_LIGHTS["BRIGHTNESS"]

        # Flags
        self.ukraine_flag = [0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0xffd500,0xffd500,0xffd500,0xffd500,0xffd500,0xffd500]


        self.white_flag = [0xffffff for i in range(17)]

        self.japan_flag = [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xbc002d,0xbc002d,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff]

        self.taiwan_flag = [0xfe0000,0x000097,0x000097,0x000097,0x000097,0xffffff,0x000097,0xfe0000,0x000097,0x000097,0x000097,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000]

        self.flags = [self.ukraine_flag, self.white_flag, self.japan_flag, self.taiwan_flag]

        self.pixels = neopixel.NeoPixel(config.RGB_LIGHTS["DATA_PIN"], config.RGB_LIGHTS["COUNT"], brightness=self.brightness, auto_write=False)

        for i in range(len(self.pixels)):
            self.pixels[i] = self.flags[0][16-i]

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

    def advance(self, time_delta):

        for message in self.message_reader:
            if message.type == MessageType.ENCODER_CHANGED:
                if message.metadata["id"] == 0:
                    step = message.metadata["position"] % len(self.flags)

                    for i in range(len(self.pixels)):
                        self.pixels[i] = self.flags[step][16-i]

                    self.pixels.show()

                elif message.metadata["id"] == 1:
                    if message.metadata["delta"] > 0:
                        self.brightness = min(1.0, self.brightness + 0.05)
                    else:
                        self.brightness = max(0.0, self.brightness - 0.05)

                    self.pixels.brightness = self.brightness
                    self.pixels.show()

