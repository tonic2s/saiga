import config

from neopixel import NeoPixel
from messaging import CommandBus, CommandType
from animation.program import AnimationProgram


class Pulse(AnimationProgram):
    def __init__(self, pixels: NeoPixel, command_bus: CommandBus):
        super().__init__()

        self.cycletime = config.ANIMATION["CYCLE_TIME"]
        self.depth = config.ANIMATION["DEPTH"]

        self.currentstep = 0
        self.command_bus = command_bus


        self.time_since_last_call = 0
        self.animation_progress = 0

    def advance(self, time_delta):
        self.time_since_last_call += time_delta

        self.animation_progress = ((self.time_since_last_call / self.cycletime) + self.animation_progress) % 1

        delta = (self.time_since_last_call / self.cycletime) / (1 / self.depth)
        if self.animation_progress < 0.5:
            self.command_bus.push(CommandType.BRIGHTNESS_UP, delta=delta)

        else:
            self.command_bus.push(CommandType.BRIGHTNESS_DOWN, delta=delta)

        self.time_since_last_call = 0
