import board
from adafruit_hid.keycode import Keycode

WATCHDOG = {
    "ENABLED": False,
    "TIMEOUT": 30,
    "SCHEDULE": {
        "refresh_time": 10,
        "priority": 100
    }
}

KEYBOARD = {
    "ROW_PINS": [
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP21,
    ],
    "COLUMN_PINS": [
        board.GP20,
        board.GP19,
        board.GP18,
        board.GP17,
        board.GP16
    ],
    "KEYMAP": [
        [(Keycode.KEYPAD_NUMLOCK, ), (Keycode.KEYPAD_FORWARD_SLASH, ), (Keycode.KEYPAD_ASTERISK, ), (Keycode.KEYPAD_MINUS, ), (Keycode.A, )],
        [(Keycode.KEYPAD_SEVEN, ), (Keycode.KEYPAD_EIGHT, ), (Keycode.KEYPAD_NINE, ), None, (Keycode.B, )],
        [(Keycode.KEYPAD_FOUR, ), (Keycode.KEYPAD_FIVE, ), (Keycode.KEYPAD_SIX, ), (Keycode.KEYPAD_PLUS, ), None],
        [(Keycode.KEYPAD_ONE, ), (Keycode.KEYPAD_TWO, ), (Keycode.KEYPAD_THREE, ), None, None],
        [(Keycode.KEYPAD_ZERO, ), None, (Keycode.KEYPAD_PERIOD, ), (Keycode.KEYPAD_ENTER, ), None],
    ],
    "SCHEDULE": {
        "refresh_time": 0.01,
        "priority": 50
    }
}

ENCODERS = {
    "AB_PINS": [
        (board.GP0, board.GP1),
        (board.GP2, board.GP3)
    ],
    "SCHEDULE": {
        "refresh_time": 0.25,
        "priority": 50
    }
}

BACKLIGHT = {
    "ENABLED": False,
    "LED_PIN": board.GP4,
    "BRIGHTNESS": 0.1,
    "SCHEDULE": {
        "refresh_time": 0.25,
        "priority": 1
    }
}

RGB_LIGHTS = {
    "ENABLED": True,
    "DATA_PIN": board.GP15,
    "COUNT": 17,
    "BRIGHTNESS": 0.1,
    "SCHEDULE": {
        "refresh_time": 0.1,
        "priority": 1
    }
}
