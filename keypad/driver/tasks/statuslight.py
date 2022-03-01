import board
import config

from task import TimedTask
from messaging import CommandBus, InputType, CommandType
from digitalio import DigitalInOut, Direction


class StatusLight(TimedTask):
    def __init__(self, command_bus: CommandBus):
        super().__init__()

        # Setup command handing
        self.command_reader = command_bus.subscribe()

        # Setup background LED's
        self.led = DigitalInOut(board.LED)
        self.led.direction = Direction.OUTPUT
        self.led.value = True

        self.remaining_blinks = 0
        self.time_since_transition = 0

    async def advance(self, time_delta):
        self.time_since_transition += time_delta

        for command in self.command_reader:
            if command.type == CommandType.STATUS_BLINK:
                self.remaining_blinks += command.metadata["count"]

        if self.led.value and self.remaining_blinks > 0 and self.time_since_transition > config.STATUS_LIGHT["BLINK_PEROOD"]:
            self.led.value = False
            self.remaining_blinks -= 1
            self.time_since_transition = 0

        if not self.led.value and self.time_since_transition > config.STATUS_LIGHT["BLINK_PEROOD"]:
            self.led.value = True
            self.time_since_transition = 0
