import config

from neopixel import NeoPixel
from lighting.plain import PlainProgram
from messaging import CommandBus, CommandType


class PulseProgram(PlainProgram):
    def __init__(self, pixels: NeoPixel, command_bus: CommandBus):
        super().__init__(pixels, command_bus)

        # Setup command handing
        self.pulse_command_reader = command_bus.subscribe()

        # Setup RGB LED's
        self.pixels = pixels

        # Setup animation state
        self.cycletime = config.ANIMATION["CYCLE_TIME"]
        self.depth = config.ANIMATION["DEPTH"]

        self.currentstep = 0
        self.command_bus = command_bus


        self.time_since_last_call = 0
        self.animation_progress = 0

    def update_brightness(self, time_delta):
        self.time_since_last_call += time_delta

        self.animation_progress = ((self.time_since_last_call / self.cycletime) + self.animation_progress) % 1
        brightness_delta = (self.time_since_last_call / self.cycletime) / (1 / self.depth)

        if self.animation_progress < 0.5:
            self.pixels.brightness += brightness_delta
        else:
            self.pixels.brightness -= brightness_delta

        self.time_since_last_call = 0
        self.pixels.show()

    def advance(self, time_delta):
        for command in self.pulse_command_reader:
            if command.type == CommandType.LIGHTING_CHANGE_SECONDARY:
                self.cycletime = max(0.1, self.cycletime + command.metadata["delta"])

        super().advance(time_delta)
        self.update_brightness(time_delta)

    def deinit(self):
        super().deinit()
        self.pulse_command_reader.unsubscribe()
