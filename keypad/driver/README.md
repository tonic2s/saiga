# Saiga Raspberry Pico Keyboard Driver

HID keyboard driver for the Saiga Keypad

## Install CircuitPython
Copy `.UF2` file to the Raspbery Pico. It can be downloaded from https://circuitpython.org/board/raspberry_pi_pico/

## Install Librarys
Install needed librarys from https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

## TODO
- Frequency modulation to dimm LED backlight
- Use non-volatile memory to store light program
    - https://docs.circuitpython.org/en/latest/shared-bindings/microcontroller/index.html#microcontroller.nvm
- Handle releasing key when not released before layer switch
    - release all on layer switch?
