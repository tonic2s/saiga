import config

from task import Task
from keypad import KeyMatrix, Event
from messaging import MessageBus, MessageType


class AsyncKeyboardProvider(Task):
    UPDATE_TIME = 0.1

    def __init__(self, message_bus: MessageBus):
        # Setup message bus
        self.message_bus = message_bus

        # Setup scaning key matrix
        self.matrix = KeyMatrix(
            row_pins=config.KEYBOARD["ROW_PINS"],
            column_pins=config.KEYBOARD["COLUMN_PINS"],
            columns_to_anodes=False,
            interval=0.02
        )

        self.transition_event = Event()

    async def advance(self):
        try:
            while self.matrix.events.get_into(self.transition_event):
                row_number, column_number = self.matrix.key_number_to_row_column(self.transition_event.key_number)

                if self.transition_event.pressed:
                    self.message_bus.push(MessageType.KEY_PRESSED, row=row_number, column=column_number, timestamp=self.transition_event.timestamp)

                elif self.transition_event.released:
                    self.message_bus.push(MessageType.KEY_RELEASED, row=row_number, column=column_number, timestamp=self.transition_event.timestamp)

                else:
                    self.message_bus.push(MessageType.ERROR, source="AsyncKeyboardProvider", message="unknown key transition event", row=row_number, column=column_number, pressed=self.transition_event.pressed, timestamp=self.transition_event.timestamp)

        except Exception as e:
            print(e)
