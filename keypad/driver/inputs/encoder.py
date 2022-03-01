import config
import rotaryio

from task import Task
from messaging import CommandBus, InputType


class RotaryEncoderInput(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command bus
        self.command_bus = command_bus

        # Setup encoders
        self.encoders = []

        for a_pin, b_pin in config.ENCODERS["AB_PINS"]:
            self.encoders.append(
                rotaryio.IncrementalEncoder(a_pin, b_pin, divisor=config.ENCODERS["DIVISOR"])
            )

        # Setup State
        self.state = [0 for i in range(len(self.encoders))]

    async def advance(self):
        for i, encoder in enumerate(self.encoders):
            new_position = encoder.position

            if new_position != self.state[i]:
                self.command_bus.trigger(InputType.ENCODER_CHANGED, id=i, position=new_position, delta=(new_position - self.state[i]))

            self.state[i] = new_position
