import config


from messaging import MessageBus, MessageType, CommandType
from animation.program import AnimationProgram


class Pulse(AnimationProgram):

    def __init__(self, pixels: NeoPixel, message_bus: MessageBus):
        super().__init__()

        self.cycletime = config.ANIMATION["CYCLE_TIME"]
        self.depth = config.ANIMATION["DEPTH"]

        self.currentstep = 0
        self.message_bus = message_bus

    
        self.timesincelastcall = 0
        self.animationprogress = 0

    def advance(self, time_delta):
        self.timesincelastcall += time_delta

        oldprogress = self.animationprogress
        self.animationprogress = ((self.timesincelastcall / self.cycletime) + oldprogress) % 1

        delta = (self.timesincelastcall / self.cycletime) / (1 / self.depth)
        if self.animationprogress < 0.5:
            self.message_bus.push(MessageType.COMMAND, command=CommandType.BRIGHTNESS_UP, value=delta)
            
        else:
            self.message_bus.push(MessageType.COMMAND, command=CommandType.BRIGHTNESS_DOWN, value=delta)

        self.timesincelastcall = 0