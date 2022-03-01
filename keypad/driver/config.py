import board
from adafruit_hid.keycode import Keycode

WATCHDOG = {
    "ENABLED": False,
    "TIMEOUT": 3
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
        [(Keycode.KEYPAD_SEVEN, ),   (Keycode.KEYPAD_EIGHT, ),         (Keycode.KEYPAD_NINE, ),     None,                     (Keycode.B, )],
        [(Keycode.KEYPAD_FOUR, ),    (Keycode.KEYPAD_FIVE, ),          (Keycode.KEYPAD_SIX, ),      (Keycode.KEYPAD_PLUS, ),  None],
        [(Keycode.KEYPAD_ONE, ),     (Keycode.KEYPAD_TWO, ),           (Keycode.KEYPAD_THREE, ),    None,                     None],
        [(Keycode.KEYPAD_ZERO, ),    None,                             (Keycode.KEYPAD_PERIOD, ),   (Keycode.KEYPAD_ENTER, ), None],
    ]
}

ENCODERS = {
    "AB_PINS": [
        (board.GP0, board.GP1),
        (board.GP2, board.GP3)
    ],
    "DIVISOR": 2
}

BACKLIGHT = {
    "ENABLED": False,
    "LED_PIN": board.GP4,
    "BRIGHTNESS": 0.1
}

RGB_LIGHTS = {
    "DATA_PIN": board.GP15,
    "COUNT": 17,
    "BRIGHTNESS": 0.1,
    "DEFAULT_HUE": 0.085,
    "FLAGS": {
        "UKRAINE": [0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0xffd500,0xffd500,0xffd500,0xffd500,0xffd500,0xffd500],
        "BLANK": [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff],
        "JAPAN": [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xbc002d,0xbc002d,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff],
        "TAIWAN": [0xfe0000,0x000097,0x000097,0x000097,0x000097,0xffffff,0x000097,0xfe0000,0x000097,0x000097,0x000097,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000]
    }
}

ANIMATION = {
    "CYCLE_TIME" : 10,
    "DEPTH" : 0.5
}

COMMAND_BUS = {
    "BUFFER_SIZE": 1000
}

STATUS_LIGHT = {
    "BLINK_PEROOD": 0.25
}

LOGGER = {
    "LOG_FILE_PATH": "error_log.txt"
}
