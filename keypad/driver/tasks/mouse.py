import usb_hid

from task import Task
from adafruit_hid.mouse import Mouse
from messaging import CommandBus, InputType, CommandType


class MouseDevice(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_bus = command_bus
        self.command_reader = self.command_bus.subscribe()

        # Setup mouse device
        self.mouse = Mouse(usb_hid.devices)

    async def advance(self):
        for command in self.command_reader:
            try:
                if command.type == CommandType.MOUSE_MOVE:
                    self.mouse.move(command.metadata["x"], command.metadata["y"], command.metadata["wheel"])

                if command.type == CommandType.SEND_MOUSE_BUTTON:
                    if command.metadata["press"]:
                        self.mouse.press(command.metadata["button"])
                    if command.metadata["release"]:
                        self.mouse.release(command.metadata["button"])

            except ValueError as e:
                self.mouse.release_all()
                self.command_bus.trigger(InputType.ERROR, source="MouseDevice", metadata=command.metadata, message=str(e))
