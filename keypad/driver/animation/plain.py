import config

from neopixel import NeoPixel
from messaging import CommandBus, CommandType
from animation.program import AnimationProgram


class Plain(AnimationProgram):
    def __init__(self, pixels: NeoPixel, command_bus: CommandBus):
        pass

    def advance(self, time_delta):
        pass
