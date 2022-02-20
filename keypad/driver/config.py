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
        ["Num Lk", "/", "*", "-", "Upper Encoder"],
        ["7", "8", "9", None, "Lower Encoder"],
        ["4", "5", "6", "+", None],
        ["1", "2", "3", None, None],
        ["0", None, ",", "Enter", None],
    ],
    "SCHEDULE": {
        "refresh_time": 0.01,
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
        "refresh_time": 0.25,
        "priority": 1
    }
}
