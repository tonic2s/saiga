import config

from task import TimedTask
from neopixel import NeoPixel
from messaging import CommandType, CommandBus

from lighting.hue import ConfigurableHue
from lighting.flag import SelectableFlag
from lighting.rainbow import RainbowAnimation

from animation.pulse import Pulse


class AccentLight(TimedTask):
    def __init__(self, command_bus: CommandBus):
        super().__init__()

        # Setup message handing
        self.command_bus = command_bus
        self.command_reader = self.command_bus.subscribe()

        # Setup RGB LED's
        self.pixels = NeoPixel(config.RGB_LIGHTS["DATA_PIN"], config.RGB_LIGHTS["COUNT"], brightness=config.RGB_LIGHTS["BRIGHTNESS"], auto_write=False)

        # Setup brightness
        self.brightness = config.RGB_LIGHTS["BRIGHTNESS"]

        # Setup program list
        self.programs = [
            SelectableFlag,
            ConfigurableHue,
            RainbowAnimation
        ]

        self.current_program_index = 0
        self.current_program = None

        self.load_program(self.current_program_index)

        # Setup animation list
        self.animations = [
            Pulse
        ]

        self.current_animation_index = 0
        self.current_animation = None

        self.load_animation(self.current_animation_index)

    def load_program(self, index):
        if self.current_program:
            self.current_program.deinit()

        self.current_program = self.programs[index](self.pixels, self.command_bus)

    def load_animation(self, index):
        if self.current_animation:
            self.current_animation.deinit()

        self.current_animation = self.animations[index](self.pixels, self.command_bus)

    async def advance(self, time_delta):
        for command in self.command_reader:
            if command.type == CommandType.LIGHTING_PROGRAM_NEXT:
                self.current_program_index = (self.current_program_index + 1) % len(self.programs)
                self.load_program(self.current_program_index)

            elif command.type == CommandType.LIGHTING_PROGRAM_LAST:
                self.current_program_index = (self.current_program_index - 1) % len(self.programs)
                self.load_program(self.current_program_index)

            elif command.type == CommandType.BRIGHTNESS_SET:
                self.brightness = min(1.0, max(0.0, command.metadata["value"]))
                self.pixels.brightness = self.brightness
                self.pixels.show()

            elif command.type == CommandType.BRIGHTNESS_UP:
                if "delta" in command.metadata:
                    delta = command.metadata["delta"]
                else:
                    delta = 0.025

                self.brightness = min(1.0, self.brightness + delta)
                self.pixels.brightness = self.brightness
                self.pixels.show()

            elif command.type == CommandType.BRIGHTNESS_DOWN:
                if "delta" in command.metadata:
                    delta = command.metadata["delta"]
                else:
                    delta = 0.025

                self.brightness = max(0.0, self.brightness - delta)
                self.pixels.brightness = self.brightness
                self.pixels.show()

        if self.current_program:
            self.current_program.advance()

        if self.current_animation:
            self.current_animation.advance(time_delta)
