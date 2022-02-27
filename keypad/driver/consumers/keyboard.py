import usb_hid

from task import Task
from adafruit_hid.keyboard import Keyboard
from messaging import MessageBus, MessageType, CommandType


class USBKeyboardDevice(Task):
    UPDATE_TIME = 0.005

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_bus = message_bus
        self.message_reader = self.message_bus.subscribe()

        # Setup keyboard device
        self.kbd = Keyboard(usb_hid.devices)

    async def advance(self):
        for message in self.message_reader:
            try:
                if message.type == MessageType.COMMAND and message.command == CommandType.SEND_KEYCODE:
                    if message.metadata["press"]:
                        self.kbd.press(*message.metadata["keycode"])
                    elif message.metadata["release"]:
                        self.kbd.release(*message.metadata["keycode"])

            except ValueError as e:
                self.kbd.release_all()
                self.message_bus.push(MessageType.ERROR, source="USBKeyboardDevice", metadata=message.metadata, message=str(e))
