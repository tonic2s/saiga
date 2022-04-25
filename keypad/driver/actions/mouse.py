from actions.action import HIDMouseButtonAction, HIDMouseMoveAction

# See:
# https://docs.qmk.fm/#/feature_mouse_keys
# https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-mouse-mouse


SPEED = 5

# Move cursor up
KC_MS_UP = HIDMouseMoveAction(y=-1 * SPEED)
KC_MS_U = KC_MS_UP
# Move cursor down
KC_MS_DOWN = HIDMouseMoveAction(y=1 * SPEED)
KC_MS_D = KC_MS_DOWN
# Move cursor left
KC_MS_LEFT = HIDMouseMoveAction(x=-1 * SPEED)
KC_MS_L = KC_MS_LEFT
# Move cursor right
KC_MS_RIGHT = HIDMouseMoveAction(x=1 * SPEED)
KC_MS_R = KC_MS_RIGHT

# Press button 1 | Left Button
KC_MS_BTN1 = HIDMouseButtonAction(2**0)
KC_MS_BTN_LEFT = KC_MS_BTN1
KC_BTN1 = KC_MS_BTN1
# Press button 2 | Right Button
KC_MS_BTN2 = HIDMouseButtonAction(2**1)
KC_MS_BTN_RIGHT = KC_MS_BTN2
KC_BTN2 = KC_MS_BTN2
# Press button 3 | Middle Button
KC_MS_BTN3 = HIDMouseButtonAction(2**2)
KC_MS_BTN_MIDDLE = KC_MS_BTN3
KC_BTN3 = KC_MS_BTN3
# Press button 4
KC_MS_BTN4 = HIDMouseButtonAction(2**3)
KC_BTN4 = KC_MS_BTN4
# Press button 5
KC_MS_BTN5 = HIDMouseButtonAction(2**4)
KC_BTN5 = KC_MS_BTN5
# Press button 6
KC_MS_BTN6 = HIDMouseButtonAction(2**5)
KC_BTN6 = KC_MS_BTN6
# Press button 7
KC_MS_BTN7 = HIDMouseButtonAction(2**6)
KC_BTN7 = KC_MS_BTN7
# Press button 8
KC_MS_BTN8 = HIDMouseButtonAction(2**7)
KC_BTN8 = KC_MS_BTN8

# Move wheel up
KC_MS_WH_UP = HIDMouseMoveAction(wheel=1 * SPEED)
KC_WH_U = KC_MS_WH_UP
# Move wheel down
KC_MS_WH_DOWN = HIDMouseMoveAction(wheel=-1 * SPEED)
KC_WH_D = KC_MS_WH_DOWN
