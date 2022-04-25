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


class HIDMouseButtonAction(AbstractAction):
    def __init__(self, button):
        self.button = button

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.SEND_MOUSE_BUTTON, press=True, release=False, button=self.button), )

    def deactivate(self) -> tuple[Command]:
        return (Command(CommandType.SEND_MOUSE_BUTTON, press=False, release=True, button=self.button), )


class HIDMouseMoveAction(AbstractAction):
    def __init__(self, x: int = 0, y: int = 0, wheel: int = 0):
        self.x = x
        self.y = y
        self.wheel = wheel

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.MOUSE_MOVE, x=self.x, y=self.y, wheel=self.wheel), )

    def deactivate(self) -> tuple[Command]:
        return tuple()


class CommandAction(AbstractAction):
    def __init__(self, command_type: CommandType, **metadata: dict):
        self.command = Command(command_type, metadata)

    def activate(self) -> tuple[Command]:
        return (self.command, )

    def deactivate(self) -> tuple[Command]:
        return tuple()


class WrappedAction(AbstractAction):
    def __init__(self, outer_action: AbstractAction, inner_action: AbstractAction):
        self.inner_action = inner_action
        self.outer_action = outer_action

    def activate(self) -> tuple[Command]:
        return self.outer_action.activate() + self.inner_action.activate()

    def deactivate(self) -> tuple[Command]:
        return self.inner_action.deactivate() + self.outer_action.deactivate()
