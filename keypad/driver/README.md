# Saiga Raspberry Pico Keyboard Driver

HID keyboard driver for the Saiga Keypad

## Install CircuitPython
Copy `.UF2` file to the Raspbery Pico. It can be downloaded from https://circuitpython.org/board/raspberry_pi_pico/

## Install Librarys
Install needed librarys from https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

- [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- [adafruit_led_animation](https://docs.circuitpython.org/projects/led-animation/en/latest/api.html)
- [adafruit_midi](https://docs.circuitpython.org/projects/midi/en/latest/api.html)
- [asyncio](https://github.com/adafruit/Adafruit_CircuitPython_asyncio)
    - [adafruit_ticks](https://docs.circuitpython.org/projects/ticks/en/latest/api.html)
- [neopixel](https://docs.circuitpython.org/projects/neopixel/en/latest/)

## Class Diagrams
![driver class diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/tonic2s/saiga/main/keypad/docs/driver.puml)
![actions diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/tonic2s/saiga/main/keypad/docs/actions.puml)

## TODO
- Frequency modulation to dimm LED backlight
- Use non-volatile memory to store light program
    - https://docs.circuitpython.org/en/latest/shared-bindings/microcontroller/index.html#microcontroller.nvm
- Handle releasing key when not released before layer switch
    - release all on layer switch?
