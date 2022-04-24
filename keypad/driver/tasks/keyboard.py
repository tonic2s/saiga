import usb_hid

from task import Task
from adafruit_hid.keyboard import Keyboard
from messaging import CommandBus, InputType, CommandType


class USBKeyboardDevice(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_bus = command_bus
        self.command_reader = self.command_bus.subscribe()

        # Setup keyboard device
        self.kbd = Keyboard(usb_hid.devices)

    async def advance(self):
        for command in self.command_reader:
            try:
                if command.type == CommandType.SEND_KEYCODE:
                    if command.metadata["press"]:
                        self.kbd.press(command.metadata["keycode"])
                    elif command.metadata["release"]:
                        self.kbd.release(command.metadata["keycode"])

            except ValueError as e:
                self.kbd.release_all()
                self.command_bus.trigger(InputType.ERROR, source="USBKeyboardDevice", metadata=command.metadata, message=str(e))
