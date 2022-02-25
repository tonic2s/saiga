import config

from task import Task
from keypad import KeyMatrix, Event
from messaging import MessageBus, MessageType
from digitalio import DigitalInOut, Direction, Pull

class AsyncKeyboardProvider(Task):
    SCHEDULE = { "update_time": 0.005, "priority": 50 }

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

    def advance(self, time_delta):
        transition_event = Event()
        while self.matrix.events.get_into(transition_event):
            row_number, column_number = self.matrix.key_number_to_row_column(transition_event.key_number)

            if transition_event.pressed:
                self.message_bus.push(MessageType.KEY_PRESSED, row=row_number, column=column_number, timestamp=transition_event.timestamp)

            elif transition_event.released:
                self.message_bus.push(MessageType.KEY_RELEASED, row=row_number, column=column_number, timestamp=transition_event.timestamp)

            else:
                self.message_bus.push(MessageType.ERROR, source="AsyncKeyboardProvider", message="unknown key transition event", row=row_number, column=column_number, pressed=transition_event.pressed, timestamp=transition_event.timestamp)

class KeyboardProvider(Task):
    SCHEDULE = { "update_time": 0.01, "priority": 50 }

    def __init__(self, message_bus: MessageBus):
        # Setup message bus
        self.message_bus = message_bus

        # Setup Rows
        self.rows = []

        for row_pin in config.KEYBOARD["ROW_PINS"]:
            row = DigitalInOut(row_pin)
            row.direction = Direction.OUTPUT

            self.rows.append(row)

        # Setup Columns
        self.columns = []
        for column_pin in config.KEYBOARD["COLUMN_PINS"]:
            column = DigitalInOut(column_pin)
            column.direction = Direction.INPUT
            column.pull = Pull.DOWN

            self.columns.append(column)

        # Setup State
        self.state = [[0 for i in range(len(self.columns))] for j in range(len(self.rows))]

    def advance(self, time_delta):
        for row_number, row in enumerate(self.rows):
            row.value = True

            for column_number, col in enumerate(self.columns):
                is_pressed = col.value

                if self.state[row_number][column_number] != is_pressed:
                    self.state[row_number][column_number] = int(is_pressed)

                    if is_pressed:
                        self.message_bus.push(MessageType.KEY_RELEASED, row=row_number, column=column_number)
                    else:
                        self.message_bus.push(MessageType.KEY_PRESSED, row=row_number, column=column_number)

            row.value = False
