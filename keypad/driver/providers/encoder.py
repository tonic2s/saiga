import config
import rotaryio

from task import Task
from messaging import MessageBus, MessageType


class RotaryEncoderProvider(Task):
    SCHEDULE = { "update_time": 0.01, "priority": 50 }

    def __init__(self, message_bus: MessageBus):
        # Setup message bus
        self.message_bus = message_bus

        # Setup encoders
        self.encoders = []

        for a_pin, b_pin in config.ENCODERS["AB_PINS"]:
            self.encoders.append(
                rotaryio.IncrementalEncoder(a_pin, b_pin, divisor=config.ENCODERS["DIVISOR"])
            )

        # Setup State
        self.state = [0 for i in range(len(self.encoders))]

    def advance(self, time_delta):
        for i, encoder in enumerate(self.encoders):
            new_position = encoder.position

            if new_position != self.state[i]:
                self.message_bus.push(MessageType.ENCODER_CHANGED, id=i, position=new_position, delta=(new_position - self.state[i]))

            self.state[i] = new_position
