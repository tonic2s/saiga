import usb_hid

from task import Task
from adafruit_hid.consumer_control import ConsumerControl
from messaging import CommandBus, InputType, CommandType


class ConsumerControlDevice(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_bus = command_bus
        self.command_reader = self.command_bus.subscribe()

        # Setup keyboard device
        self.cc = ConsumerControl(usb_hid.devices)

    async def advance(self):
        for command in self.command_reader:
            try:
                if command.type == CommandType.SEND_CONSUMER_CONTROL:
                    self.cc.send(command.metadata["controlcode"])

            except ValueError as e:
                self.cc.release()
                self.command_bus.trigger(InputType.ERROR, source="ConsumerControlDevice", metadata=command.metadata, message=str(e))
