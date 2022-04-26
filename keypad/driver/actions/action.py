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
        return (Command(CommandType.KEYBOARD_SEND_KEYCODE, press=True, release=False, keycode=self.hid_keycode), )

    def deactivate(self) -> tuple[Command]:
        return (Command(CommandType.KEYBOARD_SEND_KEYCODE, press=False, release=True, keycode=self.hid_keycode), )


class HIDConsumerControlAction(AbstractAction):
    def __init__(self, hid_controlcode):
        self.hid_controlcode = hid_controlcode

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.CONSUMER_CONTROL_SEND, controlcode=self.hid_controlcode), )

    def deactivate(self) -> tuple[Command]:
        return tuple()


class HIDMouseButtonAction(AbstractAction):
    def __init__(self, button):
        self.button = button

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.MOUSE_SEND_BUTTON, press=True, release=False, button=self.button), )

    def deactivate(self) -> tuple[Command]:
        return (Command(CommandType.MOUSE_SEND_BUTTON, press=False, release=True, button=self.button), )


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


class SequenceAction(AbstractAction):
    def __init__(self, *actions: AbstractAction):
        self.actions = actions
        self.current_action_index = 0

    def activate(self) -> tuple[Command]:
        action = self.actions[self.current_action_index]
        self.current_action_index = (self.current_action_index + 1) % len(self.actions)

        return action.activate() + action.deactivate()

    def deactivate(self) -> tuple[Command]:
        return tuple()


class MidiNoteAction(AbstractAction):
    def __init__(self, pitch: int):
        self.pitch = pitch

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.MIDI_PLAY_NOTE, on=True, pitch=self.pitch), )

    def deactivate(self) -> tuple[Command]:
        return (Command(CommandType.MIDI_PLAY_NOTE, on=False, pitch=self.pitch), )


class MidiControllerAction(AbstractAction):
    def __init__(self, controller: int, activation_value, deactivation_value = None):
        self.controller = controller
        self.activation_value = activation_value
        self.deactivation_value = deactivation_value

    def activate(self) -> tuple[Command]:
        return (Command(CommandType.MIDI_CONTROLLER, controller=self.controller, value=self.activation_value), )

    def deactivate(self) -> tuple[Command]:
        if self.activation_value is None:
            return tuple()
        else:
            return (Command(CommandType.MIDI_CONTROLLER, controller=self.controller, value=self.activation_value), )



class AbstractLayerAction:
    def activate(self, layer_state_manager):
        raise NotImplementedError()
    def deactivate(self, layer_state_manager):
        raise NotImplementedError()


class MomentaryLayerEnableAction(AbstractLayerAction):
    def __init__(self, target_layer):
        self.target_layer = target_layer

    def activate(self, layer_state_manager):
        layer_state_manager.set_layer_state(self.target_layer, True)

    def deactivate(self, layer_state_manager):
        layer_state_manager.set_layer_state(self.target_layer, False)


class LayerToggleAction(AbstractLayerAction):
    def __init__(self, target_layer):
        self.target_layer = target_layer

    def activate(self, layer_state_manager):
        layer_state_manager.toggle_layer_state(self.target_layer)

    def deactivate(self, layer_state_manager):
        pass
