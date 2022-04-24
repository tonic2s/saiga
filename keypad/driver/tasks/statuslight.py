import board
import config

from task import TimedTask
from messaging import CommandBus, CommandType
from digitalio import DigitalInOut, Direction


class StatusLight(TimedTask):
    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_reader = command_bus.subscribe()

        # Setup background LED's
        self.led = DigitalInOut(board.LED)
        self.led.direction = Direction.OUTPUT
        self.led.value = config.STATUS_LIGHT["ON_BY_DEFAULT"]

        self.remaining_blinks = 0
        self.time_since_transition = 0

    async def advance(self, time_delta):
        self.time_since_transition += time_delta

        for command in self.command_reader:
            if command.type == CommandType.STATUS_BLINK:
                self.remaining_blinks += command.metadata["count"]

        if self.is_in_default_state() and self.remaining_blinks > 0 and self.should_transition():
            self.led.value = not config.STATUS_LIGHT["ON_BY_DEFAULT"]
            self.remaining_blinks -= 1
            self.time_since_transition = 0

        if not self.is_in_default_state() and self.should_transition():
            self.led.value = config.STATUS_LIGHT["ON_BY_DEFAULT"]
            self.time_since_transition = 0


    def is_in_default_state(self):
        return self.led.value == config.STATUS_LIGHT["ON_BY_DEFAULT"]

    def should_transition(self):
        return self.time_since_transition > config.STATUS_LIGHT["BLINK_PEROOD"]
