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
        board.GP18,
        board.GP17,
        board.GP16
    ],
    "COLUMN_PINS": [
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
        board.GP26
    ],
    "KEYMAP": [
        [(Keycode.SEVEN, ), (Keycode.EIGHT, ), (Keycode.NINE, ),  (Keycode.Q, ), (Keycode.W, )],
        [(Keycode.FOUR, ),  (Keycode.FIVE, ),  (Keycode.SIX, ),   (Keycode.A, ), (Keycode.S, )],
        [(Keycode.ONE, ),   (Keycode.TWO, ),   (Keycode.THREE, ), (Keycode.Y, ), (Keycode.X, )]
    ],
    "SCHEDULE": {
        "refresh_time": 0.01,
        "priority": 50
    }
}

BACKLIGHT = {
    "LED_PINS": [
        board.GP15,
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11
    ],
    "SCHEDULE": {
        "refresh_time": 0.25,
        "priority": 1
    }
}

RGB_LIGHTS = {
    "DATA_PIN": board.GP10,
    "COUNT": 5,
    "BRIGHTNESS": 0.1,
    "SCHEDULE": {
        "refresh_time": 0.25,
        "priority": 1
    }
}
