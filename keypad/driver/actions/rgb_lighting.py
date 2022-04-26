from messaging import CommandType
from actions.action import CommandAction, SequenceAction

# See: https://docs.qmk.fm/#/feature_rgblight


# Toggle RGB lighting on or off
RGB_TOG = SequenceAction(
    CommandAction(CommandType.LIGHTING_CHANGE_BRIGHTNESS, brightness=0),
    CommandAction(CommandType.LIGHTING_CHANGE_BRIGHTNESS, brightness=1)
)
# Cycle through modes
RGB_MODE_FORWARD = CommandAction(CommandType.LIGHTING_CHANGE_PROGRAM, delta=1)
RGB_MOD = RGB_MODE_FORWARD
# Cycle through modes in reverse
RGB_MODE_REVERSE = CommandAction(CommandType.LIGHTING_CHANGE_PROGRAM, delta=-1)
RGB_RMOD = RGB_MODE_REVERSE

# Increase hue
RGB_HUI = CommandAction(CommandType.LIGHTING_CHANGE_HUE, delta=0.015)
# Decrease hue
RGB_HUD = CommandAction(CommandType.LIGHTING_CHANGE_HUE, delta=-0.015)
# Increase saturation
RGB_SAI = CommandAction(CommandType.LIGHTING_CHANGE_SATURATION, delta=0.05)
# Decrease saturation
RGB_SAD = CommandAction(CommandType.LIGHTING_CHANGE_SATURATION, delta=-0.05)
# Increase value (brightness)
RGB_VAI = CommandAction(CommandType.LIGHTING_CHANGE_BRIGHTNESS, delta=0.025)
# Decrease value (brightness)
RGB_VAD = CommandAction(CommandType.LIGHTING_CHANGE_BRIGHTNESS, delta=-0.025)

# Increase value of secondary lighting program function
RGB_SECONDARY_INCREASE = CommandAction(CommandType.LIGHTING_CHANGE_SECONDARY, delta=0.25)
RGB_S_I = RGB_SECONDARY_INCREASE
# Decrease value of secondary lighting program function
RGB_SECONDARY_DECREASE = CommandAction(CommandType.LIGHTING_CHANGE_SECONDARY, delta=-0.25)
RGB_S_D = RGB_SECONDARY_DECREASE

# Static (no animation) mode
RGB_MODE_PLAIN = CommandAction(CommandType.LIGHTING_CHANGE_PROGRAM, program=0)
RGB_M_P = RGB_MODE_PLAIN
# Breathing animation mode
RGB_MODE_BREATHE = CommandAction(CommandType.LIGHTING_CHANGE_PROGRAM, program=1)
RGB_M_B = RGB_MODE_BREATHE
# Rainbow animation mode
RGB_MODE_RAINBOW = CommandAction(CommandType.LIGHTING_CHANGE_PROGRAM, program=2)
RGB_M_R = RGB_MODE_RAINBOW
# Swirl animation mode
RGB_MODE_SWIRL = NotImplementedError()
RGB_M_SW = RGB_MODE_SWIRL
# Snake animation mode
RGB_MODE_SNAKE = NotImplementedError()
RGB_M_SN = RGB_MODE_SNAKE
# “Knight Rider” animation mode
RGB_MODE_KNIGHT = NotImplementedError()
RGB_M_K = RGB_MODE_KNIGHT
# Christmas animation mode
RGB_MODE_XMAS = NotImplementedError()
RGB_M_X = RGB_MODE_XMAS
# Static gradient animation mode
RGB_MODE_GRADIENT = NotImplementedError()
RGB_M_G = RGB_MODE_GRADIENT
# Red,Green,Blue test animation mode
RGB_MODE_RGBTEST = NotImplementedError()
RGB_M_T = RGB_MODE_RGBTEST
