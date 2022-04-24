from adafruit_hid.keycode import Keycode
from actions.action import HIDKeyboardAction

# See:
# https://docs.qmk.fm/#/keycodes_basic
# https://usb.org/sites/default/files/hut1_21_0.pdf#page=83

# Ignore this key (NOOP)
KC_NO = None
XXXXXXX = KC_NO

# Use the next lowest non-transparent key
KC_TRANSPARENT = None
KC_TRNS = KC_TRANSPARENT
_______ = KC_TRANSPARENT

# a and A
KC_A = HIDKeyboardAction(Keycode.A)
# b and B
KC_B = HIDKeyboardAction(Keycode.B)
# c and C
KC_C = HIDKeyboardAction(Keycode.C)
# d and D
KC_D = HIDKeyboardAction(Keycode.D)
# e and E
KC_E = HIDKeyboardAction(Keycode.E)
# f and F
KC_F = HIDKeyboardAction(Keycode.F)
# g and G
KC_G = HIDKeyboardAction(Keycode.G)
# h and H
KC_H = HIDKeyboardAction(Keycode.H)
# i and I
KC_I = HIDKeyboardAction(Keycode.I)
# j and J
KC_J = HIDKeyboardAction(Keycode.J)
# k and K
KC_K = HIDKeyboardAction(Keycode.K)
# l and L
KC_L = HIDKeyboardAction(Keycode.L)
# m and M
KC_M = HIDKeyboardAction(Keycode.M)
# n and N
KC_N = HIDKeyboardAction(Keycode.N)
# o and O
KC_O = HIDKeyboardAction(Keycode.O)
# p and P
KC_P = HIDKeyboardAction(Keycode.P)
# q and Q
KC_Q = HIDKeyboardAction(Keycode.Q)
# r and R
KC_R = HIDKeyboardAction(Keycode.R)
# s and S
KC_S = HIDKeyboardAction(Keycode.S)
# t and T
KC_T = HIDKeyboardAction(Keycode.T)
# u and U
KC_U = HIDKeyboardAction(Keycode.U)
# v and V
KC_V = HIDKeyboardAction(Keycode.V)
# w and W
KC_W = HIDKeyboardAction(Keycode.W)
# x and X
KC_X = HIDKeyboardAction(Keycode.X)
# y and Y
KC_Y = HIDKeyboardAction(Keycode.Y)
# z and Z
KC_Z = HIDKeyboardAction(Keycode.Z)
# 1 and !
KC_1 = HIDKeyboardAction(Keycode.ONE)
# 2 and @
KC_2 = HIDKeyboardAction(Keycode.TWO)
# 3 and #
KC_3 = HIDKeyboardAction(Keycode.THREE)
# 4 and $
KC_4 = HIDKeyboardAction(Keycode.FOUR)
# 5 and %
KC_5 = HIDKeyboardAction(Keycode.FIVE)
# 6 and ^
KC_6 = HIDKeyboardAction(Keycode.SIX)
# 7 and &
KC_7 = HIDKeyboardAction(Keycode.SEVEN)
# 8 and *
KC_8 = HIDKeyboardAction(Keycode.EIGHT)
# 9 and (
KC_9 = HIDKeyboardAction(Keycode.NINE)
# 0 and )
KC_0 = HIDKeyboardAction(Keycode.ZERO)

# Return (Enter)
KC_ENTER = HIDKeyboardAction(Keycode.ENTER)
KC_ENT = KC_ENTER
# Escape
KC_ESCAPE = HIDKeyboardAction(Keycode.ESCAPE)
KC_ESC = KC_ESCAPE
# Delete (Backspace)
KC_BACKSPACE = HIDKeyboardAction(Keycode.BACKSPACE)
KC_BSPC = KC_BACKSPACE
# Tab
KC_TAB = HIDKeyboardAction(Keycode.TAB)
# Spacebar
KC_SPACE = HIDKeyboardAction(Keycode.SPACE)
KC_SPC = KC_SPACE

# - and _
KC_MINUS = HIDKeyboardAction(Keycode.MINUS)
KC_MINS = KC_MINUS
# = and +
KC_EQUAL = HIDKeyboardAction(Keycode.EQUALS)
KC_EQL = KC_EQUAL
# [ and {
KC_LEFT_BRACKET = HIDKeyboardAction(Keycode.LEFT_BRACKET)
KC_LBRC = KC_LEFT_BRACKET
# ] and }
KC_RIGHT_BRACKET = HIDKeyboardAction(Keycode.RIGHT_BRACKET)
KC_RBRC = KC_RIGHT_BRACKET
# \ and |
KC_BACKSLASH = HIDKeyboardAction(Keycode.BACKSLASH)
KC_BSLS = KC_BACKSLASH
# Non-US # and ~
KC_NONUS_HASH = HIDKeyboardAction(Keycode.POUND)
KC_NUHS = KC_NONUS_HASH
# ; and :
KC_SEMICOLON = HIDKeyboardAction(Keycode.SEMICOLON)
KC_SCLN = KC_SEMICOLON
# ' and "
KC_QUOTE = HIDKeyboardAction(Keycode.QUOTE)
KC_QUOT = KC_QUOTE
# ` and ~
KC_GRAVE = HIDKeyboardAction(Keycode.GRAVE_ACCENT)
KC_GRV = KC_GRAVE
# , and <
KC_COMMA = HIDKeyboardAction(Keycode.COMMA)
KC_COMM = KC_COMMA
# . and >
KC_DOT = HIDKeyboardAction(Keycode.PERIOD)
# / and ?
KC_SLASH = HIDKeyboardAction(Keycode.FORWARD_SLASH)
KC_SLSH = KC_SLASH

#Caps Lock
KC_CAPS_LOCK = HIDKeyboardAction(Keycode.CAPS_LOCK)
KC_CAPS = KC_CAPS_LOCK

# F1
KC_F1 = HIDKeyboardAction(Keycode.F1)
# F2
KC_F2 = HIDKeyboardAction(Keycode.F2)
# F3
KC_F3 = HIDKeyboardAction(Keycode.F3)
# F4
KC_F4 = HIDKeyboardAction(Keycode.F4)
# F5
KC_F5 = HIDKeyboardAction(Keycode.F5)
# F6
KC_F6 = HIDKeyboardAction(Keycode.F6)
# F7
KC_F7 = HIDKeyboardAction(Keycode.F7)
# F8
KC_F8 = HIDKeyboardAction(Keycode.F8)
# F9
KC_F9 = HIDKeyboardAction(Keycode.F9)
# F10
KC_F10 = HIDKeyboardAction(Keycode.F10)
# F11
KC_F11 = HIDKeyboardAction(Keycode.F11)
# F12
KC_F12 = HIDKeyboardAction(Keycode.F12)

# Print Screen
KC_PRINT_SCREEN = HIDKeyboardAction(Keycode.PRINT_SCREEN)
KC_PSCR = KC_PRINT_SCREEN
# Scroll Lock, Brightness Down (macOS)
KC_SCROLL_LOCK = HIDKeyboardAction(Keycode.SCROLL_LOCK)
KC_SCRL = KC_SCROLL_LOCK
KC_BRMD = KC_SCROLL_LOCK
# Pause, Brightness Up (macOS)
KC_PAUSE = HIDKeyboardAction(Keycode.PAUSE)
KC_PAUS = KC_PAUSE
KC_BRK = KC_PAUSE
KC_BRMU = KC_PAUSE

# Insert
KC_INSERT = HIDKeyboardAction(Keycode.INSERT)
KC_INS = KC_INSERT
# Home
KC_HOME = HIDKeyboardAction(Keycode.HOME)
# Page Up
KC_PAGE_UP = HIDKeyboardAction(Keycode.PAGE_UP)
KC_PGUP = KC_PAGE_UP
# Forward Delete
KC_DELETE = HIDKeyboardAction(Keycode.DELETE)
KC_DEL = KC_DELETE
# End
KC_END = HIDKeyboardAction(Keycode.END)
# Page Down
KC_PAGE_DOWN = HIDKeyboardAction(Keycode.PAGE_DOWN)
KC_PGDN = KC_PAGE_DOWN

# Right Arrow
KC_RIGHT = HIDKeyboardAction(Keycode.RIGHT_ARROW)
KC_RGHT = KC_RIGHT
# Left Arrow
KC_LEFT = HIDKeyboardAction(Keycode.LEFT_ARROW)
# Down Arrow
KC_DOWN = HIDKeyboardAction(Keycode.DOWN_ARROW)
# Up Arrow
KC_UP = HIDKeyboardAction(Keycode.UP_ARROW)

# Keypad Num Lock and Clear
KC_NUM_LOCK = HIDKeyboardAction(Keycode.KEYPAD_NUMLOCK)
KC_NUM = KC_NUM_LOCK
# Keypad /
KC_KP_SLASH = HIDKeyboardAction(Keycode.KEYPAD_FORWARD_SLASH)
KC_PSLS = KC_KP_SLASH
# Keypad *
KC_KP_ASTERISK = HIDKeyboardAction(Keycode.KEYPAD_ASTERISK)
KC_PAST = KC_KP_ASTERISK
# Keypad -
KC_KP_MINUS = HIDKeyboardAction(Keycode.KEYPAD_MINUS)
KC_PMNS = KC_KP_MINUS
# Keypad +
KC_KP_PLUS = HIDKeyboardAction(Keycode.KEYPAD_PLUS)
KC_PPLS = KC_KP_PLUS
# Keypad Enter
KC_KP_ENTER = HIDKeyboardAction(Keycode.KEYPAD_ENTER)
KC_PENT = KC_KP_ENTER
# Keypad 1 and End
KC_KP_1 = HIDKeyboardAction(Keycode.KEYPAD_ONE)
KC_P1 = KC_KP_1
# Keypad 2 and Down Arrow
KC_KP_2 = HIDKeyboardAction(Keycode.KEYPAD_TWO)
KC_P2 = KC_KP_2
# Keypad 3 and Page Down
KC_KP_3 = HIDKeyboardAction(Keycode.KEYPAD_THREE)
KC_P3 = KC_KP_3
# Keypad 4 and Left Arrow
KC_KP_4 = HIDKeyboardAction(Keycode.KEYPAD_FOUR)
KC_P4 = KC_KP_4
# Keypad 5
KC_KP_5 = HIDKeyboardAction(Keycode.KEYPAD_FIVE)
KC_P5 = KC_KP_5
# Keypad 6 and Right Arrow
KC_KP_6 = HIDKeyboardAction(Keycode.KEYPAD_SIX)
KC_P6 = KC_KP_6
# Keypad 7 and Home
KC_KP_7 = HIDKeyboardAction(Keycode.KEYPAD_SEVEN)
KC_P7 = KC_KP_7
# Keypad 8 and Up Arrow
KC_KP_8 = HIDKeyboardAction(Keycode.KEYPAD_EIGHT)
KC_P8 = KC_KP_8
# Keypad 9 and Page Up
KC_KP_9 = HIDKeyboardAction(Keycode.KEYPAD_NINE)
KC_P9 = KC_KP_9
# Keypad 0 and Insert
KC_KP_0 = HIDKeyboardAction(Keycode.KEYPAD_ZERO)
KC_P0 = KC_KP_0
# Keypad . and Delete
KC_KP_DOT = HIDKeyboardAction(Keycode.KEYPAD_PERIOD)
KC_PDOT = KC_KP_DOT
# Non-US \ and |
KC_NONUS_BACKSLASH = HIDKeyboardAction(Keycode.KEYPAD_BACKSLASH)
KC_NUBS = KC_NONUS_BACKSLASH

# Application (Windows Context Menu Key)
KC_APPLICATION = HIDKeyboardAction(Keycode.APPLICATION)
KC_APP = KC_APPLICATION
# System Power (Mac)
KC_KB_POWER = HIDKeyboardAction(Keycode.POWER)
# Keypad =
KC_KP_EQUAL = HIDKeyboardAction(Keycode.KEYPAD_EQUALS)
KC_PEQL = KC_KP_EQUAL

# F13
KC_F13 = HIDKeyboardAction(Keycode.F13)
# F14
KC_F14 = HIDKeyboardAction(Keycode.F14)
# F15
KC_F15 = HIDKeyboardAction(Keycode.F15)
# F16
KC_F16 = HIDKeyboardAction(Keycode.F16)
# F17
KC_F17 = HIDKeyboardAction(Keycode.F17)
# F18
KC_F18 = HIDKeyboardAction(Keycode.F18)
# F19
KC_F19 = HIDKeyboardAction(Keycode.F19)
# F20
KC_F20 = HIDKeyboardAction(Keycode.F20)
# F21
KC_F21 = HIDKeyboardAction(Keycode.F21)
# F22
KC_F22 = HIDKeyboardAction(Keycode.F22)
# F23
KC_F23 = HIDKeyboardAction(Keycode.F23)
# F24
KC_F24 = HIDKeyboardAction(Keycode.F24)

# Left Control
KC_LEFT_CTRL = HIDKeyboardAction(Keycode.LEFT_CONTROL)
KC_LCTL = KC_LEFT_CTRL
# Left Shift
KC_LEFT_SHIFT = HIDKeyboardAction(Keycode.LEFT_SHIFT)
KC_LSFT = KC_LEFT_SHIFT
# Left Alt (Option)
KC_LEFT_ALT = HIDKeyboardAction(Keycode.LEFT_ALT)
KC_LALT = KC_LEFT_ALT
KC_LOPT = KC_LEFT_ALT
# Left GUI (Windows/Command/Meta key)
KC_LEFT_GUI = HIDKeyboardAction(Keycode.LEFT_GUI)
KC_LGUI = KC_LEFT_GUI
KC_LCMD = KC_LEFT_GUI
KC_LWIN = KC_LEFT_GUI
# Right Control
KC_RIGHT_CTRL = HIDKeyboardAction(Keycode.RIGHT_CONTROL)
KC_RCTL = KC_RIGHT_CTRL
# Right Shift
KC_RIGHT_SHIFT = HIDKeyboardAction(Keycode.RIGHT_SHIFT)
KC_RSFT = KC_RIGHT_SHIFT
# Right Alt (Option/AltGr)
KC_RIGHT_ALT = HIDKeyboardAction(Keycode.RIGHT_ALT)
KC_RALT = KC_RIGHT_ALT
KC_ROPT = KC_RIGHT_ALT
KC_ALGR = KC_RIGHT_ALT
# Right GUI (Windows/Command/Meta key)
KC_RIGHT_GUI = HIDKeyboardAction(Keycode.RIGHT_GUI)
KC_RGUI = KC_RIGHT_GUI
KC_RCMD = KC_RIGHT_GUI
KC_RWIN = KC_RIGHT_GUI

# Mute
KC_KB_MUTE = HIDKeyboardAction(0x7F)
# Volume Up
KC_KB_VOLUME_UP = HIDKeyboardAction(0x80)
# Volume Down
KC_KB_VOLUME_DOWN = HIDKeyboardAction(0x81)
