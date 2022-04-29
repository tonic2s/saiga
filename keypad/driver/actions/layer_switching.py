from actions.action import MomentaryLayerEnableAction, LayerToggleAction, LayerCycleAction


# Set the base (default) layer
def DF(layer):
    raise NotImplementedError()

# Momentarily turn on layer when pressed (requires KC_TRNS on destination layer)
def MO(layer):
    return MomentaryLayerEnableAction(layer)

# Momentarily activates layer until a key is pressed. See One Shot Keys for details.
def OSL(layer):
    raise NotImplementedError()

# Momentarily turn on layer (like MO) with mod active as well. Where mod is a mods_bit. Mods can be viewed here. Example Implementation: LM(LAYER_1, MOD_LALT)
def LM(layer, mod):
    raise NotImplementedError()

# Turn on layer when held, kc when tapped
def LT(layer, kc):
    raise NotImplementedError()

# Toggle layer on or off
def TG(layer):
    return LayerToggleAction(layer)

# Turns on layer and turns off all other layers, except the default layer
def TO(layer):
    raise NotImplementedError()

# Normally acts like MO unless it’s tapped multiple times, which toggles layer on
def TT(layer):
    raise NotImplementedError()


# Cycle though layer list and allways keep the current one enabled. Use None to have a step where all others are turnd off
def CY(*layers):
    return LayerCycleAction(*layers)
