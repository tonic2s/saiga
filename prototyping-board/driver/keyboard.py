import time
import board
import usb_hid

import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.colorcycle import ColorCycle

from microcontroller import watchdog
from watchdog import WatchDogMode

# Setup watchdog (reset system if broken)
# watchdog.timeout = 2.5 # Set a timeout of 2.5 seconds
watchdog.mode = WatchDogMode.RESET
watchdog.feed()

# Setup Raspberry Pico board LED
board_status_led = DigitalInOut(board.GP25)
board_status_led.direction = Direction.OUTPUT

# Setup RGB LED's
num_pixels = 5
pixels = neopixel.NeoPixel(board.GP10, num_pixels, brightness=0.1, auto_write=False)

# pixel_animation = Pulse(pixels, 0.1, (255, 0, 0))

# pixel_animation = RainbowSparkle(pixels, 0.1)
# pixel_animation.generate_rainbow()

# pixel_animation = RainbowComet(pixels, 0.1, 2)

# pixel_animation = RainbowChase(pixels, 0.1)

pixel_animation = Rainbow(pixels, 0.05)

# pixel_animation = ColorCycle(pixels, 0.5, ((255, 0, 0), (255, 40, 0), (255, 150, 0), (0, 255, 0), (0, 0, 255), (180, 0, 255)))

def step_rgb_animation():
    pixel_animation.draw()
    pixel_animation.show()

# Setup background LED's
background_leds = [
    DigitalInOut(board.GP15),
    DigitalInOut(board.GP14),
    DigitalInOut(board.GP13),
    DigitalInOut(board.GP12),
    DigitalInOut(board.GP11),
]

for led in background_leds:
    led.direction = Direction.OUTPUT

background_speed = 0.25

background_led_index = 0
background_led_last_time = time.monotonic()
def step_backgound_animation():
    global background_led_index
    global background_led_last_time

    current_time = time.monotonic()
    if current_time - background_led_last_time > background_speed:
        background_led_last_time = current_time

        background_led = background_leds[background_led_index]
        background_led.value = not background_led.value

        background_led_index = (background_led_index + 1) % len(background_leds)

# Setup keyboard device
kbd = Keyboard(usb_hid.devices)

keymap = [
    [(Keycode.SEVEN, ), (Keycode.EIGHT, ), (Keycode.NINE, ),  (Keycode.Q, ), (Keycode.W, )],
    [(Keycode.FOUR, ),  (Keycode.FIVE, ),  (Keycode.SIX, ),   (Keycode.A, ), (Keycode.S, )],
    [(Keycode.ONE, ),   (Keycode.TWO, ),   (Keycode.THREE, ), (Keycode.Y, ), (Keycode.X, )]
]

# Setup Rows
rows = [
    DigitalInOut(board.GP18),
    DigitalInOut(board.GP17),
    DigitalInOut(board.GP16)
]

for row in rows:
    row.direction = Direction.OUTPUT

# Setup Columns
columns = [
    DigitalInOut(board.GP19),
    DigitalInOut(board.GP20),
    DigitalInOut(board.GP21),
    DigitalInOut(board.GP22),
    DigitalInOut(board.GP26)
]

for column in columns:
    column.direction = Direction.INPUT
    column.pull = Pull.DOWN

# Core Loop
state = [[0 for i in range(len(columns))] for j in range(len(rows))]

watchdog_last_feed_time = time.monotonic()
state_has_changed = False
while True:
    for row_number, row in enumerate(rows):
        row.value = True

        for column_number, col in enumerate(columns):
            is_pressed = col.value

            if state[row_number][column_number] != is_pressed:
                state[row_number][column_number] = int(is_pressed)

                try:
                    if is_pressed:
                        if row_number == column_number == 0:
                            time.sleep(3)
                        kbd.press(*keymap[row_number][column_number])
                    else:
                        kbd.release(*keymap[row_number][column_number])
                except ValueError as e:
                    kbd.release_all()
                    print(e)


                state_has_changed = True

        row.value = False

    if state_has_changed:
        print(state)
        state_has_changed = False


    current_time = time.monotonic()
    if current_time - watchdog_last_feed_time > 1:
        watchdog_last_feed_time = current_time
        watchdog.feed()

    step_rgb_animation()
    step_backgound_animation()

    time.sleep(0.001)
