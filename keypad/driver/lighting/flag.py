import config

from neopixel import NeoPixel
from lighting.program import LightingProgram
from messaging import MessageBus, MessageType, CommandType


class SelectableFlag(LightingProgram):
    def __init__(self, pixels: NeoPixel, message_bus: MessageBus):
        self.pixels = pixels

        # Setup message handing
        self.message_reader = message_bus.subscribe()
        self.flag = list(config.RGB_LIGHTS["FLAGS"].values())
        self.step = 0

        for i in range(len(self.pixels)):
             self.pixels[i] = self.flag[self.step][16-i]
        self.pixels.show()
        
        print(type(self.flag))

    def advance(self):
        for message in self.message_reader:
            if message.type == MessageType.COMMAND and message.command == CommandType.FLAG_SET:
                for i in range(len(self.pixels)):
                    self.pixels[i] = self.flag[self.step][16-i]
                self.pixels.show()

                self.step = (self.step + 1) % len(self.flag)

    def deinit(self):
        self.message_reader.unsubscribe()

