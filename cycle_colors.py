import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

colors = [BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]
pixels = neopixel.NeoPixel(board.GP15, 17, brightness=0.1, auto_write=False)

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

while True:
    led.value = not led.value
    
    for color in colors:
        pixels.fill(color)
        pixels.show()
        time.sleep(0.5)
