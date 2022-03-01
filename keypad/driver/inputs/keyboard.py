import config

from task import Task
from keypad import KeyMatrix, Event
from messaging import CommandBus, InputType


class KeyboardInput(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command bus
        self.command_bus = command_bus

        # Setup scaning key matrix
        self.matrix = KeyMatrix(
            row_pins=config.KEYBOARD["ROW_PINS"],
            column_pins=config.KEYBOARD["COLUMN_PINS"],
            columns_to_anodes=False,
            interval=0.02
        )

        self.transition_event = Event()

    async def advance(self):
        while self.matrix.events.get_into(self.transition_event):
            row_number, column_number = self.matrix.key_number_to_row_column(self.transition_event.key_number)

            if self.transition_event.pressed:
                self.command_bus.trigger(InputType.KEY_PRESSED, row=row_number, column=column_number, timestamp=self.transition_event.timestamp)

            elif self.transition_event.released:
                self.command_bus.trigger(InputType.KEY_RELEASED, row=row_number, column=column_number, timestamp=self.transition_event.timestamp)

            else:
                self.command_bus.trigger(InputType.ERROR, source="AsyncKeyboardProvider", message="invalid key transition event", row=row_number, column=column_number, pressed=self.transition_event.pressed, timestamp=self.transition_event.timestamp)

