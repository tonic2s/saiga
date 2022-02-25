import config
import storage

from digitalio import DigitalInOut, Direction, Pull


def is_key_pressed(row, column):
    row_pin = DigitalInOut(config.KEYBOARD["ROW_PINS"][row])
    row_pin.direction = Direction.OUTPUT

    column_pin = DigitalInOut(config.KEYBOARD["COLUMN_PINS"][column])
    column_pin.direction = Direction.INPUT
    column_pin.pull = Pull.DOWN

    row_pin.value = True
    is_pressed = column_pin.value
    row_pin.value = False

    row_pin.deinit()
    column_pin.deinit()

    return is_pressed


# Lookup key press to make flash writeable to the pico but read only to host
print("Looking for pressed upper encoder...")
if is_key_pressed(0, 4):
    print("Was pressed, remounting filesystem readonly!")

    # https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/data-logger
    storage.remount("/", readonly=False)

    storage.disable_usb_drive()
else:
    print("Was not pressed")


# Lookup key press to disable watchdog
print("Looking for pressed lower encoder...")
if is_key_pressed(1, 4):
    print("Was pressed, disabling watchdog!")

    config.WATCHDOG["ENABLED"] = False
else:
    print("Was not pressed")
