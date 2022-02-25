import config
import usb_hid

from task import Task
from adafruit_hid.keyboard import Keyboard
from messaging import MessageBus, MessageType


class USBKeyboardDevice(Task):
    SCHEDULE = { "update_time": 0.005, "priority": 50 }

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_bus = message_bus
        self.message_reader = self.message_bus.subscribe()

        # Setup keyboard device
        self.kbd = Keyboard(usb_hid.devices)

        self.keymap = config.KEYBOARD["KEYMAP"]

    def advance(self, time_delta):
        for message in self.message_reader:
            try:
                if message.type == MessageType.KEY_PRESSED:
                    self.kbd.press(*self.keymap[message.metadata["row"]][message.metadata["column"]])
                elif message.type == MessageType.KEY_RELEASED:
                    self.kbd.release(*self.keymap[message.metadata["row"]][message.metadata["column"]])

            except ValueError as e:
                self.kbd.release_all()
                self.message_bus.push(MessageType.ERROR, source="USBKeyboardDevice", row=message.metadata["row"], column=message.metadata["column"], message=str(e))
