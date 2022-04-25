from actions.action import AbstractAction, AbstractLayerAction
from messaging import AbstractInputHandler, InputType


class LayerStateManager:
    def __init__(self):
        self.layer_enabled = {}

    def register_layers(self, layer_state: dict[str, bool]):
        for layer_name, enabled in layer_state.items():
            self.layer_enabled[layer_name] = enabled

    def is_layer_enabled(self, layer_name) -> bool:
        return self.layer_enabled[layer_name]

    def set_layer_state(self, layer_name, is_enabled):
        self.layer_enabled[layer_name] = is_enabled

    def toggle_layer_state(self, layer_name):
        self.layer_enabled[layer_name] = not self.layer_enabled[layer_name]

LAYER_STATE_MANAGER = LayerStateManager()


class KeyboardActionLayer:
    def __init__(self, *map_rows: list[list[AbstractAction]], default_enabled=False):
        self.default_enabled = default_enabled
        self.action_lookup: list[list[AbstractAction]] = map_rows

    def get_action(self, row, column) -> AbstractAction:
        return self.action_lookup[row][column]

class KeyboardActionMap(AbstractInputHandler):
    def __init__(self, **layers: dict[str, KeyboardActionLayer]):
        # NOTE: Assumes that function parameter and dicts are ordered

        self.layers: dict[str, KeyboardActionLayer] = layers
        self.default_layer = next(iter(self.layers))

        layer_enabled = { layer_name: layer.default_enabled for layer_name, layer in self.layers.items() }
        layer_enabled[self.default_layer] = True

        LAYER_STATE_MANAGER.register_layers(layer_enabled)

    def is_layer_enabled(self, layer_name):
        return LAYER_STATE_MANAGER.is_layer_enabled(layer_name)

    def get_action(self, row, column):
        result_action = None

        # NOTE: Assumes that the default layer is always enabled
        for layer_name, layer in self.layers.items():
            if self.is_layer_enabled(layer_name):
                action = layer.get_action(row, column)

                if action is not None:
                    result_action = action

        return result_action

    def handle_input(self, message_type: InputType, metadata: dict):
        if message_type == InputType.KEY_PRESSED:
            action = self.get_action(metadata["row"], metadata["column"])
            if action is None:
                return tuple()
            elif isinstance(action, AbstractLayerAction):
                action.activate(LAYER_STATE_MANAGER)
                return tuple()
            else:
                return action.activate()

        elif message_type == InputType.KEY_RELEASED:
            action = self.get_action(metadata["row"], metadata["column"])
            if action is None:
                return tuple()
            elif isinstance(action, AbstractLayerAction):
                action.deactivate(LAYER_STATE_MANAGER)
                return tuple()
            else:
                return action.deactivate()

        return tuple()


class EncoderActionLayer:
    def __init__(self, *action_lookup: list[tuple[AbstractAction]], default_enabled=False):
        self.default_enabled = default_enabled
        self.action_lookup = action_lookup

    def get_action(self, id, delta) -> AbstractAction:
        if delta > 0:
            # encoder position increased
            return self.action_lookup[id][0]
        else:
            # encoder position decreased
            return self.action_lookup[id][1]


class EncoderActionMap(AbstractInputHandler):
    def __init__(self, **layers: dict[str, EncoderActionLayer]):
        # NOTE: Assumes that function parameter and dicts are ordered

        self.layers: dict[str, EncoderActionLayer] = layers
        self.default_layer = next(iter(self.layers))

        layer_enabled = { layer_name: layer.default_enabled for layer_name, layer in self.layers.items() }
        layer_enabled[self.default_layer] = True

        LAYER_STATE_MANAGER.register_layers(layer_enabled)

    def is_layer_enabled(self, layer_name):
        return LAYER_STATE_MANAGER.is_layer_enabled(layer_name)

    def get_action(self, id, delta):
        result_action = None

        # NOTE: Assumes that default layer is always enabled
        for layer_name, layer in self.layers.items():
            if self.is_layer_enabled(layer_name):
                action = layer.get_action(id, delta)

                if action is not None:
                    result_action = action

        return result_action

    def handle_input(self, message_type: InputType, metadata: dict):
        if message_type == InputType.ENCODER_CHANGED:
            action = self.get_action(metadata["id"], metadata["delta"])

            if action is not None:
                return action.activate() + action.deactivate()

        return tuple()
