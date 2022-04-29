from actions.action import AbstractAction, CombinedAction, WrappedAction, SequenceAction


def COMBINE(*actions: list[AbstractAction]):
    return CombinedAction(actions)

def WRAP(outer_action: AbstractAction, inner_action: AbstractAction):
    return WrappedAction(outer_action, inner_action)

def SEQUENCE(*actions: list[AbstractAction]):
    return SequenceAction(actions)
