import board
from actions.midi import *
from actions.basic import *
from actions.media import *
from actions.mouse import *
from actions.modifiers import *
from actions.rgb_lighting import *
from actions.layer_switching import *
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
            (MO("RGB"),        TG("NUM"),        KC_KP_SLASH,      KC_KP_ASTERISK,   KC_KP_MINUS       ),
            (TG("MIDI"),       KC_KP_7,          KC_KP_8,          KC_KP_9,          XXXXXXX           ),
            (XXXXXXX,          KC_KP_4,          KC_KP_5,          KC_KP_6,          KC_KP_PLUS        ),
            (XXXXXXX,          KC_KP_1,          KC_KP_2,          KC_KP_3,          XXXXXXX           ),
            (XXXXXXX,          KC_KP_0,          XXXXXXX,          KC_KP_DOT,        KC_KP_ENTER       )
        ),
        NUM=KeyboardActionLayer(
            (KC_TRNS,          KC_TRNS,          KC_TRNS,          KC_TRNS,          KC_TRNS           ),
            (KC_TRNS,          KC_HOME,          KC_UP,            KC_PAGE_UP,       XXXXXXX           ),
            (XXXXXXX,          KC_LEFT,          KC_TRNS,          KC_RIGHT,         KC_TRNS           ),
            (XXXXXXX,          KC_END,           KC_DOWN,          KC_PAGE_DOWN,     XXXXXXX           ),
            (XXXXXXX,          KC_INSERT,        XXXXXXX,          KC_TRNS,          KC_TRNS           )
        ),
        MIDI=KeyboardActionLayer(
            (KC_TRNS,          KC_TRNS,          MI_ALLOFF,        KC_TRNS,          KC_TRNS           ),
            (KC_TRNS,          MI_D_1,           MI_C_1,           MI_B,             XXXXXXX           ),
            (XXXXXXX,          MI_A,             MI_G,             MI_F,             KC_TRNS           ),
            (XXXXXXX,          MI_E,             MI_D,             MI_C,             XXXXXXX           ),
            (XXXXXXX,          MI_SUS,           XXXXXXX,          KC_TRNS,          KC_TRNS           )
        ),
        RGB=KeyboardActionLayer(
            (KC_TRNS,          KC_NUM_LOCK,      KC_TRNS,          KC_TRNS,          RGB_S_D           ),
            (KC_TRNS,          RGB_TOG,          RGB_HUI,          KC_TRNS,          XXXXXXX           ),
            (XXXXXXX,          RGB_SAD,          KC_TRNS,          RGB_SAI,          RGB_S_I           ),
            (XXXXXXX,          KC_TRNS,          RGB_HUI,          KC_TRNS,          XXXXXXX           ),
            (XXXXXXX,          KC_TRNS,          XXXXXXX,          KC_TRNS,          KC_TRNS           )
        )
    )
}

MOUSE = {
    "ENABLED": False
}

CONSUMER_CONTROL = {
    "ENABLED": True
}

MIDI = {
    "ENABLED": True,
    "OCTAVE": 4, # Corresponds to MI_OCT_2
    "TRANSPOSITION": 0,
    "VELOCITY": 127,
    "CHANNEL": 0,
    "MODULATION_INTERVAL": 8
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
            (KC_AUDIO_VOL_UP,     KC_AUDIO_VOL_DOWN  ),
            (KC_MEDIA_NEXT_TRACK, KC_MEDIA_PREV_TRACK)
        ),
        NUM=EncoderActionLayer(
            (KC_TRNS,             KC_TRNS            ),
            (KC_TRNS,             KC_TRNS            )
        ),
        MIDI=EncoderActionLayer(
            (MI_OCTU,             MI_OCTD            ),
            (MI_TRNSU,            MI_TRNSD           )
        ),
        RGB=EncoderActionLayer(
            (RGB_MODE_FORWARD,    RGB_MODE_REVERSE   ),
            (RGB_VAI,             RGB_VAD            )
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
    "IMAGES": {
        "WHITE":        [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff],
        "FLAG_UKRAINE": [0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0x005bbb,0xffd500,0xffd500,0xffd500,0xffd500,0xffd500,0xffd500],
        "FLAG_JAPAN":   [0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xbc002d,0xbc002d,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff],
        "FLAG_TAIWAN":  [0xfe0000,0x000097,0x000097,0x000097,0x000097,0xffffff,0x000097,0xfe0000,0x000097,0x000097,0x000097,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000,0xfe0000]
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
