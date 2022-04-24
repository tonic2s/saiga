from actions.action import AbstractAction, WrappedAction
from actions.basic import KC_LEFT_CTRL, KC_LEFT_SHIFT, KC_LEFT_ALT, KC_LEFT_GUI, KC_RIGHT_CTRL, KC_RIGHT_SHIFT, KC_RIGHT_ALT, KC_RIGHT_GUI

# Hold Left Control and press kc
def LCTL(kc: AbstractAction):
    return WrappedAction(KC_LEFT_CTRL, kc)
C = LCTL

# Hold Left Shift and press kc
def LSFT(kc: AbstractAction):
    return WrappedAction(KC_LEFT_SHIFT, kc)
S = LSFT

# Hold Left Alt and press kc
def LALT(kc: AbstractAction):
    return WrappedAction(KC_LEFT_ALT, kc)
A = LALT
LOPT = LALT

# Hold Left GUI and press kc
def LGUI(kc: AbstractAction):
    return WrappedAction(KC_LEFT_GUI, kc)
G = LGUI
LCMD = LGUI
LWIN = LGUI

# Hold Right Control and press kc
def RCTL(kc: AbstractAction):
    return WrappedAction(KC_RIGHT_CTRL, kc)

# Hold Right Shift and press kc
def RSFT(kc: AbstractAction):
    return WrappedAction(KC_RIGHT_SHIFT, kc)

# Hold Right Alt and press kc
def RALT(kc: AbstractAction):
    return WrappedAction(KC_RIGHT_ALT, kc)
ROPT = RALT
ALGR = RALT

# Hold Right GUI and press kc
def RGUI(kc: AbstractAction):
    return WrappedAction(KC_RIGHT_GUI, kc)
RCMD = RGUI
LWIN = RGUI

# Hold Left Shift and GUI and press kc
def LSG(kc: AbstractAction):
    return WrappedAction(KC_LEFT_SHIFT, LGUI(kc))
SGUI = LSG
SCMD = LSG
SWIN = LSG

# Hold Left Alt and Left GUI and press kc
def LAG(kc: AbstractAction):
    return LALT(LGUI(kc))

# Hold Right Shift and Right GUI and press kc
def RSG(kc: AbstractAction):
    return RSFT(RGUI(kc))

# Hold Right Alt and Right GUI and press kc
def RAG(kc: AbstractAction):
    return RALT(RGUI(kc))

# Hold Left Control and Alt and press kc
def LCA(kc: AbstractAction):
    return LCTL(LALT(kc))

# Hold Left Shift and Left Alt and press kc
def LSA(kc: AbstractAction):
    return LSFT(LALT(kc))

# Hold Right Shift and Right Alt (AltGr) and press kc
def RSA(kc: AbstractAction):
    return RSFT(RALT(kc))
SAGR = RSA

# Hold Right Control and Right Shift and press kc
def RCS(kc: AbstractAction):
    return RCTL(RSFT(kc))

# Hold Left Control and Left Shift and press kc
def LCS(kc: AbstractAction):
    return LCTL(LSFT(kc))

# Hold Left Control, Alt and GUI and press kc
def LCAG(kc: AbstractAction):
    return LCTL(LAG(kc))

# Hold Left Control, Shift and Alt and press kc
def MEH(kc: AbstractAction):
    return LCTL(LSA(kc))

# Hold Left Control, Shift, Alt and GUI and press kc
def HYPR(kc: AbstractAction):
    return MEH(LGUI(kc))
