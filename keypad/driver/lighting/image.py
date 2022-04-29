import config

from neopixel import NeoPixel
from lighting.program import LightingProgram
from messaging import CommandBus, CommandType


class ImageProgram(LightingProgram):
    def __init__(self, pixels: NeoPixel, message_bus: CommandBus):
        self.pixels = pixels

        # Setup message handing
        self.command_reader = message_bus.subscribe()
        self.images = list(config.RGB_LIGHTS["IMAGES"].values())
        self.current_image_index = 0

        self.update_image()

    def update_image(self):
        for i in range(len(self.pixels)):
            self.pixels[i] = self.images[self.current_image_index][16 - i]

        self.pixels.show()

    def advance(self, time_delta):
        for command in self.command_reader:
            if command.type == CommandType.LIGHTING_CHANGE_SECONDARY:
                if "delta" in command.metadata:
                    if command.metadata["delta"] > 0:
                        self.current_image_index = (self.current_image_index + 1) % len(self.images)
                    else:
                        self.current_image_index = (self.current_image_index - 1) % len(self.images)


                    self.update_image()

    def deinit(self):
        self.command_reader.unsubscribe()
