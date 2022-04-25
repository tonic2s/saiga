from messaging import CommandType
from actions.action import CommandAction

# See: https://docs.qmk.fm/#/feature_rgblight

# Toggle RGB lighting on or off
RGB_TOG = CommandAction(CommandType.BRIGHTNESS_SET, value=0)
# Cycle through modes, reverse direction when Shift is held
RGB_MODE_FORWARD = CommandAction(CommandType.LIGHTING_PROGRAM_NEXT)
RGB_MOD = RGB_MODE_FORWARD
# Cycle through modes in reverse, forward direction when Shift is held
RGB_MODE_REVERSE = CommandAction(CommandType.LIGHTING_PROGRAM_LAST)
RGB_RMOD = RGB_MODE_REVERSE

# Increase hue, decrease hue when Shift is held
RGB_HUI = CommandAction(CommandType.HUE_CHANGE, delta=0.015)
# Decrease hue, increase hue when Shift is held
RGB_HUD = CommandAction(CommandType.HUE_CHANGE, delta=-0.015)
# Increase saturation, decrease saturation when Shift is held
RGB_SAI = CommandAction(CommandType.SATURATION_CHANGE, delta=0.05)
# Decrease saturation, increase saturation when Shift is held
RGB_SAD = CommandAction(CommandType.SATURATION_CHANGE, delta=-0.05)
# Increase value (brightness), decrease value when Shift is held
RGB_VAI = CommandAction(CommandType.BRIGHTNESS_CHANGE, delta=0.025)
# Decrease value (brightness), increase value when Shift is held
RGB_VAD = CommandAction(CommandType.BRIGHTNESS_CHANGE, delta=-0.025)

# Static (no animation) mode
RGB_MODE_PLAIN = None
RGB_M_P = RGB_MODE_PLAIN
# Breathing animation mode
RGB_MODE_BREATHE = None
RGB_M_B = RGB_MODE_BREATHE
# Rainbow animation mode
RGB_MODE_RAINBOW = None
RGB_M_R = RGB_MODE_RAINBOW
# Swirl animation mode
RGB_MODE_SWIRL = None
RGB_M_SW = RGB_MODE_SWIRL
# Snake animation mode
RGB_MODE_SNAKE = None
RGB_M_SN = RGB_MODE_SNAKE
# “Knight Rider” animation mode
RGB_MODE_KNIGHT = None
RGB_M_K = RGB_MODE_KNIGHT
# Christmas animation mode
RGB_MODE_XMAS = None
RGB_M_X = RGB_MODE_XMAS
# Static gradient animation mode
RGB_MODE_GRADIENT = None
RGB_M_G = RGB_MODE_GRADIENT
# Red,Green,Blue test animation mode
RGB_MODE_RGBTEST = None
RGB_M_T = RGB_MODE_RGBTEST
