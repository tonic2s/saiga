import board
import config

from task import Task
from messaging import MessageBus, MessageType
from digitalio import DigitalInOut, Direction


class StatusLight(Task):
    SCHEDULE = { "update_time": 0.1, "priority": 1 }

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_reader = message_bus.subscribe()

        # Setup background LED's
        self.led = DigitalInOut(board.LED)
        self.led.direction = Direction.OUTPUT
        self.led.value = True

        self.remaining_blinks = 0
        self.time_since_transition = 0

    def advance(self, time_delta):
        self.time_since_transition += time_delta

        for message in self.message_reader:
            if message.type == MessageType.ERROR:
                self.remaining_blinks = 3

        if self.led.value and self.remaining_blinks > 0 and self.time_since_transition > config.STATUS_LIGHT["BLINK_PEROOD"]:
            self.led.value = False
            self.remaining_blinks -= 1
            self.time_since_transition = 0

        if not self.led.value and self.time_since_transition > config.STATUS_LIGHT["BLINK_PEROOD"]:
            self.led.value = True
            self.time_since_transition = 0
