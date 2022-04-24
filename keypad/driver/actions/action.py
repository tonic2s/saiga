from messaging import Command, CommandType

class AbstractAction:
    def activate(self) -> tuple[Command]:
        raise NotImplementedError()
    def deactivate(self) -> tuple[Command]:
        raise NotImplementedError()


class HIDKeyboardAction(AbstractAction):
    def __init__(self, hid_keycode):
        self.hid_keycode = hid_keycode

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.SEND_KEYCODE, press=True, release=False, keycode=self.hid_keycode), )

    def deactivate(self) -> tuple[Command]:
        return (Command(CommandType.SEND_KEYCODE, press=False, release=True, keycode=self.hid_keycode), )


class HIDConsumerControlAction(AbstractAction):
    def __init__(self, hid_controlcode):
        self.hid_controlcode = hid_controlcode

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.SEND_CONSUMER_CONTROL, controlcode=self.hid_controlcode), )

    def deactivate(self) -> tuple[Command]:
        return tuple()


class CommandAction(AbstractAction):
    def __init__(self, command_type: CommandType, **metadata: dict):
        self.command = Command(command_type, metadata)

    def activate(self) -> tuple[Command]:
        return (self.command, )

    def deactivate(self) -> tuple[Command]:
        return tuple()
