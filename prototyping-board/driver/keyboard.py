import config
import usb_hid

from task import Task
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard


class SaigaKeyboard(Task):
    def __init__(self):
        # Setup keyboard device
        self.kbd = Keyboard(usb_hid.devices)

        self.keymap = config.KEYBOARD.KEYMAP

        # Setup Rows
        self.rows = []

        for row_pin in config.KEYBOARD.ROW_PINS:
            row = DigitalInOut(row_pin)
            row.direction = Direction.OUTPUT

            self.rows.append(row)

        # Setup Columns
        self.columns = []
        for column_pin in config.KEYBOARD.COLUMN_PINS:
            column = DigitalInOut(column_pin)
            column.direction = Direction.INPUT
            column.pull = Pull.DOWN

            self.columns.append(column)

        # Setup State
        self.state = [[0 for i in range(len(self.columns))] for j in range(len(self.rows))]

        # Setup update variables
        self.state_has_changed = False

    def is_key_pressed(self, row, column):
        return bool(self.state[row][column])

    def advance(self, time_delta):
        for row_number, row in enumerate(rows):
            row.value = True

            for column_number, col in enumerate(columns):
                is_pressed = col.value

                if state[row_number][column_number] != is_pressed:
                    state[row_number][column_number] = int(is_pressed)

                    try:
                        if is_pressed:
                            kbd.press(*keymap[row_number][column_number])
                        else:
                            kbd.release(*keymap[row_number][column_number])
                    except ValueError as e:
                        kbd.release_all()
                        print(e)

                    self.state_has_changed = True

            row.value = False

        if self.state_has_changed:
            print(state)
            self.state_has_changed = False
