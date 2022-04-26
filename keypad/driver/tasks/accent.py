import config

from task import TimedTask
from neopixel import NeoPixel
from messaging import CommandType, CommandBus

from lighting.plain import PlainProgram
from lighting.pulse import PulseProgram
from lighting.image import ImageProgram
from lighting.rainbow import RainbowProgram


class AccentLight(TimedTask):
    def __init__(self, command_bus: CommandBus):
        # Setup message handing
        self.command_bus = command_bus
        self.command_reader = self.command_bus.subscribe()

        # Setup RGB LED's
        self.pixels = NeoPixel(config.RGB_LIGHTS["DATA_PIN"], config.RGB_LIGHTS["COUNT"], brightness=config.RGB_LIGHTS["BRIGHTNESS"], auto_write=False)

        # Setup program list
        self.programs = [
            PlainProgram,
            PulseProgram,
            RainbowProgram,
            ImageProgram
        ]

        self.current_program_index = 0
        self.current_program = None

        self.load_program(self.current_program_index)

    def load_program(self, index):
        if self.current_program:
            self.current_program.deinit()

        self.current_program = self.programs[index](self.pixels, self.command_bus)

    async def advance(self, time_delta):
        for command in self.command_reader:
            if command.type == CommandType.LIGHTING_CHANGE_PROGRAM:
                if "delta" in command.metadata:
                    self.current_program_index = (self.current_program_index + command.metadata["delta"]) % len(self.programs)
                    self.load_program(self.current_program_index)

                elif "program" in command.metadata:
                    self.current_program_index = command.metadata["program"] % len(self.programs)
                    self.load_program(self.current_program_index)

            if command.type == CommandType.LIGHTING_CHANGE_BRIGHTNESS:
                if "delta" in command.metadata:
                    self.pixels.brightness = max(0, min(1, self.pixels.brightness + command.metadata["delta"]))
                    self.pixels.show()

                elif "brightness" in command.metadata:
                    self.pixels.brightness = max(0, min(1, command.metadata["brightness"]))
                    self.pixels.show()

        if self.current_program:
            self.current_program.advance(time_delta)
