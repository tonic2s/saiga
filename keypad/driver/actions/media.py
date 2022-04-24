from adafruit_hid.consumer_control_code import ConsumerControlCode
from actions.action import HIDConsumerControlAction

# Note: CONSUMER_CONTROL has to be enabled in the config for these actions to work
# See:
# https://docs.qmk.fm/#/keycodes_basic
# https://usb.org/sites/default/files/hut1_21_0.pdf#page=118


# Mute
KC_AUDIO_MUTE = HIDConsumerControlAction(ConsumerControlCode.MUTE)
KC_MUTE = KC_AUDIO_MUTE
# Volume Up
KC_AUDIO_VOL_UP = HIDConsumerControlAction(ConsumerControlCode.VOLUME_INCREMENT)
KC_VOLU = KC_AUDIO_VOL_UP
# Volume Down
KC_AUDIO_VOL_DOWN = HIDConsumerControlAction(ConsumerControlCode.VOLUME_DECREMENT)
KC_VOLD = KC_AUDIO_VOL_DOWN

# Next Track
KC_MEDIA_NEXT_TRACK = HIDConsumerControlAction(ConsumerControlCode.SCAN_NEXT_TRACK)
KC_MNXT = KC_MEDIA_NEXT_TRACK
# Previous Track
KC_MEDIA_PREV_TRACK = HIDConsumerControlAction(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
KC_MPRV = KC_MEDIA_PREV_TRACK
# Fast Forward
KC_MEDIA_FAST_FORWARD = HIDConsumerControlAction(ConsumerControlCode.FAST_FORWARD)
KC_MFFD = KC_MEDIA_FAST_FORWARD
# Rewind
KC_MEDIA_REWIND = HIDConsumerControlAction(ConsumerControlCode.REWIND)
KC_MRWD = KC_MEDIA_REWIND

# Stop Track
KC_MEDIA_STOP = HIDConsumerControlAction(ConsumerControlCode.STOP)
KC_MSTP = KC_MEDIA_STOP
# Play/Pause Track
KC_MEDIA_PLAY_PAUSE = HIDConsumerControlAction(ConsumerControlCode.PLAY_PAUSE)
KC_MPLY = KC_MEDIA_PLAY_PAUSE

# Eject
KC_MEDIA_EJECT = HIDConsumerControlAction(ConsumerControlCode.EJECT)
KC_EJCT = KC_MEDIA_EJECT

# Record
KC_MEDIA_RECORD = HIDConsumerControlAction(ConsumerControlCode.RECORD)

# Brightness Up
KC_BRIGHTNESS_UP = HIDConsumerControlAction(ConsumerControlCode.BRIGHTNESS_INCREMENT)
KC_BRIU = KC_BRIGHTNESS_UP
# Brightness Down
KC_BRIGHTNESS_DOWN = HIDConsumerControlAction(ConsumerControlCode.BRIGHTNESS_DECREMENT)
KC_BRID = KC_BRIGHTNESS_DOWN
