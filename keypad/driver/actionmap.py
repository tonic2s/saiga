from actions import *
from actions.action import AbstractAction
from messaging import AbstractInputHandler, Command, InputType


class KeyboardActionLayer:
    def __init__(self, *map_rows: list[list[AbstractAction]], is_enabled=False):
        self.is_enabled = is_enabled
        self.action_lookup: list[list[AbstractAction]] = map_rows

    def activate(self, row, column) -> tuple[Command]:
        keycode = self.action_lookup[row][column]

        if keycode:
            return keycode.activate()
        return tuple()

    def deactivate(self, row, column) -> tuple[Command]:
        keycode = self.action_lookup[row][column]

        if keycode:
            return keycode.deactivate()
        return tuple()

class KeyboardActionMap(AbstractInputHandler):
    def __init__(self, **layers: dict[str, KeyboardActionLayer]):
        self.layers: dict[str, KeyboardActionLayer] = layers

        # Assumes function parameter are ordered!
        self.layer_order = list(self.layers.keys())
        self.default_layer = self.layer_order[0]
        self.layers[self.default_layer].is_enabled = True

    def handle_input(self, message_type: InputType, metadata: dict):
        if message_type == InputType.KEY_PRESSED:
            return self.layers[self.default_layer].activate(metadata["row"], metadata["column"])

        elif message_type == InputType.KEY_RELEASED:
            return self.layers[self.default_layer].deactivate(metadata["row"], metadata["column"])

        else:
            return tuple()


class EncoderActionLayer:
    def __init__(self, *action_lookup: list[tuple[AbstractAction]], is_enabled=False):
        self.is_enabled = is_enabled
        self.action_lookup = action_lookup

    def activate(self, id, delta) -> tuple[Command]:
        if delta > 0:
            # encoder position increased
            action = self.action_lookup[id][0]
        else:
            # encoder position decreased
            action = self.action_lookup[id][1]

        return action.activate() + action.deactivate()

    def deactivate(self, row, column) -> tuple[Command]:
        return tuple()


class EncoderActionMap(AbstractInputHandler):
    def __init__(self, **layers: dict[str, EncoderActionLayer]):
        self.layers: dict[str, EncoderActionLayer] = layers

        # Assumes function parameter are ordered!
        self.layer_order = list(self.layers.keys())
        self.default_layer = self.layer_order[0]
        self.layers[self.default_layer].is_enabled = True

    def handle_input(self, message_type: InputType, metadata: dict):
        if message_type == InputType.ENCODER_CHANGED:
            return self.layers[self.default_layer].activate(metadata["id"], metadata["delta"])

        else:
            return tuple()



# a = LayeredKeyMap(
#     # Keymap _BL: Base Layer (Default Layer)
#     _BL=KeyMap(
#         F(0),    KC_1,    KC_2,   KC_3,   KC_4,   KC_5,   KC_6,   KC_7,   KC_8,   KC_9,    KC_0,     KC_MINS,  KC_EQL,   KC_GRV,    KC_BSPC,        KC_PGUP,
#         KC_TAB,  KC_Q,    KC_W,   KC_E,   KC_R,   KC_T,   KC_Y,   KC_U,   KC_I,   KC_O,    KC_P,     KC_LBRC,  KC_RBRC,  KC_BSLS,                   KC_PGDN,
#         KC_CAPS, KC_A,    KC_S,   KC_D,   KC_F,   KC_G,   KC_H,   KC_J,   KC_K,   KC_L,    KC_SCLN,  KC_QUOT,  KC_NUHS,  KC_ENT,
#         KC_LSFT, KC_NUBS, KC_Z,   KC_X,   KC_C,   KC_V,   KC_B,   KC_N,   KC_M,   KC_COMM, KC_DOT,   KC_SLSH,  KC_ROPT,  KC_RSFT,             KC_UP,
#         KC_LCTL, KC_LGUI, KC_LALT, _______,          KC_SPC,KC_SPC,                        _______,  KC_RALT,  KC_RCTL,  MO("_FL"), KC_LEFT, KC_DOWN, KC_RGHT
#     ),
#     # Keymap _FL: Function Layer
#     _FL=KeyMap(
#         KC_GRV,  KC_F1,   KC_F2,    KC_F3,  KC_F4,  KC_F5,  KC_F6,  KC_F7,  KC_F8,  KC_F9,   KC_F10,   KC_F11,   KC_F12,   _______, KC_DEL,           _______,
#         _______, _______, _______  ,_______,_______,_______,_______,_______,KC_PSCR,KC_SCRL, KC_PAUS,  _______,  _______,  _______,                   _______,
#         _______, _______, MO("_CL"),_______,_______,_______,_______,_______,_______,_______, _______,  _______,  _______,  _______,
#         _______, _______, _______  ,_______,_______,_______,_______,_______,_______,_______, _______,  _______,  _______,  _______,          KC_PGUP,
#         _______, _______, _______  ,_______,        _______,_______,                        _______,  _______,  _______,  MO("_FL"), KC_HOME, KC_PGDN, KC_END
#     ),
#     # Keymap _CL: Control layer
#     _CL=KeyMap(
#         _______,   _______, _______,  _______,_______,_______,_______,_______,_______,_______, _______,  _______,  _______,  _______, RGB_TOG,          RGB_VAI,
#         _______,   _______, _______,  _______,_______,_______,_______,_______,_______,_______, _______,  _______,  _______,  _______,                   RGB_VAD,
#         _______,   _______, MO("_CL"),_______,_______,_______,_______,_______,_______,_______, _______,  _______,  _______,  _______,
#         MO("_FL"), _______, _______,  _______,_______,_______,_______,_______,_______,_______, _______,  _______,  _______,  MO("_FL"),          RGB_SAI,
#         _______,   _______, _______,  _______,        RGB_MOD,   RGB_MOD,                            _______,  _______,  _______,  _______, RGB_HUD,    RGB_SAD,    RGB_HUI
#     )
# )
