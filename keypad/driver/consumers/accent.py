import config

from task import Task
from neopixel import NeoPixel
from messaging import CommandType, MessageBus, MessageType

from lighting.hue import ConfigurableHue
from lighting.rainbow import RainbowAnimation


class AccentLight(Task):
    UPDATE_TIME = 0.1

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_bus = message_bus
        self.message_reader = self.message_bus.subscribe()

        # Setup RGB LED's
        self.pixels = NeoPixel(config.RGB_LIGHTS["DATA_PIN"], config.RGB_LIGHTS["COUNT"], brightness=config.RGB_LIGHTS["BRIGHTNESS"], auto_write=False)

        # Setup brightness
        self.brightness = config.RGB_LIGHTS["BRIGHTNESS"]

        # Setup program list
        self.programs = [
            ConfigurableHue,
            RainbowAnimation
        ]

        self.current_program_index = 0
        self.current_program = None

        self.load_program(self.current_program_index)

    def load_program(self, index):
        if self.current_program:
            self.current_program.deinit()

        self.current_program = self.programs[index](self.pixels, self.message_bus)

    async def advance(self):
        for message in self.message_reader:
            if message.type == MessageType.COMMAND and message.command == CommandType.LIGHTING_PROGRAM_NEXT:
                self.current_program_index = (self.current_program_index + 1) % len(self.programs)
                self.load_program(self.current_program_index)

            elif message.type == MessageType.COMMAND and message.command == CommandType.LIGHTING_PROGRAM_LAST:
                self.current_program_index = (self.current_program_index - 1) % len(self.programs)
                self.load_program(self.current_program_index)

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

        if self.current_program:
            self.current_program.advance()
