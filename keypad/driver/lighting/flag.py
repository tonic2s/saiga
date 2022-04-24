import config

from neopixel import NeoPixel
from lighting.program import LightingProgram
from messaging import CommandBus, CommandType


class SelectableFlag(LightingProgram):
    def __init__(self, pixels: NeoPixel, message_bus: CommandBus):
        self.pixels = pixels

        # Setup message handing
        self.command_reader = message_bus.subscribe()
        self.flag = list(config.RGB_LIGHTS["FLAGS"].values())
        self.step = 0

        for i in range(len(self.pixels)):
             self.pixels[i] = self.flag[self.step][16-i]
        self.pixels.show()

    def advance(self):
        for command in self.command_reader:
            if command.type == CommandType.FLAG_SET:
                for i in range(len(self.pixels)):
                    self.pixels[i] = self.flag[self.step][16-i]
                self.pixels.show()

                self.step = (self.step + 1) % len(self.flag)

    def deinit(self):
        self.command_reader.unsubscribe()
