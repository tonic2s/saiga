import board
from actions.basic import *
from actions.media import *
from actions.modifiers import *
from actions.rgb_lighting import *
from actionmap import EncoderActionLayer, EncoderActionMap, KeyboardActionLayer, KeyboardActionMap

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
        board.GP16,
        board.GP20,
        board.GP19,
        board.GP18,
        board.GP17
    ],
    "ACTION_MAP": KeyboardActionMap(
        BASE=KeyboardActionLayer(
            (RGB_MODE_FORWARD, KC_NUM,  RGB_SAI,     RGB_SAD,        KC_KP_MINUS),
            (RGB_MODE_REVERSE, KC_KP_7, KC_KP_8,     KC_KP_9,        XXXXXXX    ),
            (XXXXXXX         , KC_KP_4, KC_KP_5,     KC_KP_6,        KC_KP_PLUS ),
            (XXXXXXX         , KC_KP_1, KC_KP_2,     KC_KP_3,        XXXXXXX    ),
            (XXXXXXX         , KC_KP_0, XXXXXXX,     KC_KP_DOT,      KC_KP_ENTER)
        ),
        CONTROL=KeyboardActionLayer(
            (KC_A,    KC_NUM,  KC_KP_SLASH, KC_KP_ASTERISK, KC_KP_MINUS),
            (KC_B,    KC_KP_7, KC_KP_8,     KC_KP_9,        XXXXXXX    ),
            (XXXXXXX, KC_KP_4, KC_KP_5,     KC_KP_6,        KC_KP_PLUS ),
            (XXXXXXX, KC_KP_1, KC_KP_2,     KC_KP_3,        XXXXXXX    ),
            (XXXXXXX, KC_KP_0,              KC_KP_DOT,      KC_KP_ENTER)
        )
    )
}

CONSUMER_CONTROL = {
    "ENABLED": True
}

ENCODERS = {
    "A_PINS": [
        board.GP2,
        board.GP0
    ],
    "B_PINS": [
        board.GP3,
        board.GP1
    ],
    "DIVISOR": 2,
    "ACTION_MAP": EncoderActionMap(
        BASE=EncoderActionLayer(
            (KC_AUDIO_VOL_UP, KC_AUDIO_VOL_DOWN),
            (KC_MEDIA_NEXT_TRACK, KC_MEDIA_PREV_TRACK)
        ),
        CONTROL=EncoderActionLayer(
            (KC_KP_1, KC_KP_2),
            (KC_KP_3, KC_KP_4)
        )
    )
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
        "BLANK":   [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff],
        "JAPAN":   [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xbc002d,0xbc002d,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff],
        "TAIWAN":  [0xfe0000,0x000097,0x000097,0x000097,0x000097,0xffffff,0x000097,0xfe0000,0x000097,0x000097,0x000097,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000]
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
    "BLINK_PEROOD": 0.25,
    "ON_BY_DEFAULT": True
}

LOGGER = {
    "LOG_FILE_PATH": "/error_log.txt"
}
