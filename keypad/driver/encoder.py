import config
import rotaryio

from task import Task
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard


class RotaryEncoder(Task):
    def __init__(self):
        # Setup encoders
        self.encoders = []

        for a_pin, b_pin in config.ENCODERS["AB_PINS"]:
            self.encoders.append(
                rotaryio.IncrementalEncoder(a_pin, b_pin, divisor=2)
            )

        # Setup State
        self.state = [0 for i in range(len(self.encoders))]

        # Setup update variables
        self.state_has_changed = False

    def advance(self, time_delta):
        for i, encoder in enumerate(self.encoders):
            new_position = encoder.position

            if new_position != self.state[i]:
                self.state_has_changed = True

            self.state[i] = new_position

        if self.state_has_changed:
            print(self.state)
            self.state_has_changed = False
