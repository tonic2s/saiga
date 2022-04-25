import usb_midi

from task import Task
from messaging import CommandBus, InputType, CommandType

import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange


class MIDIDevice(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_bus = command_bus
        self.command_reader = self.command_bus.subscribe()

        # Corresponds to MI_OCT_2
        self.octave = 4
        self.transposition = 0
        self.velocity = 127
        self.channel = 0
        self.modulation_interval = 8

        # Setup mouse device
        self.midi = adafruit_midi.MIDI(
            midi_in=usb_midi.ports[0], in_channel=0,
            midi_out=usb_midi.ports[1], out_channel=self.channel
        )

    async def advance(self):
        for command in self.command_reader:
            try:
                if command.type == CommandType.MIDI_PLAY_NOTE:
                    if command.metadata["on"]:
                        self.midi.send(NoteOn(command.metadata["pitch"] + 12 * (self.octave - 1) + self.transposition, self.velocity), channel=self.channel)
                    else:
                        self.midi.send(NoteOff(command.metadata["pitch"] + 12 * (self.octave - 1) + self.transposition, self.velocity), channel=self.channel)

                elif command.type == CommandType.MIDI_CHANGE_OCTAVE:
                    if "delta" in command.metadata:
                        if command.metadata["delta"] > 0:
                            self.octave = min(8, max(-1, self.octave + 1))
                        else:
                            self.octave = min(8, max(-1, self.octave - 1))
                    elif "octave" in command.metadata:
                        self.octave = min(8, max(-1, command.metadata["octave"]))

                elif command.type == CommandType.MIDI_CHANGE_TRANSPOSITION:
                    if "delta" in command.metadata:
                        if command.metadata["delta"] > 0:
                            self.transposition = min(6, max(-6, self.transposition + 1))
                        else:
                            self.transposition = min(6, max(-6, self.transposition - 1))
                    elif "transposition" in command.metadata:
                        self.transposition = min(6, max(-6, command.metadata["transposition"]))

                elif command.type == CommandType.MIDI_CHANGE_VELOCITY:
                    if "delta" in command.metadata:
                        if command.metadata["delta"] > 0:
                            self.velocity = min(127, max(0, self.velocity + 1))
                        else:
                            self.velocity = min(127, max(0, self.velocity - 1))
                    elif "velocity" in command.metadata:
                        self.velocity = min(127, max(0, command.metadata["velocity"]))

                elif command.type == CommandType.MIDI_CHANGE_CHANNEL:
                    if "delta" in command.metadata:
                        if command.metadata["delta"] > 0:
                            self.channel = min(15, max(0, self.channel + 1))
                        else:
                            self.channel = min(15, max(0, self.channel - 1))
                    elif "channel" in command.metadata:
                        self.channel = min(15, max(0, command.metadata["channel"]))

                elif command.type == CommandType.MIDI_CONTROLLER:
                    self.midi.send(ControlChange(command.metadata["controller"], command.metadata["value"]), self.channel)

            except Exception as e:
                self.command_bus.trigger(InputType.ERROR, source="MIDIDevice", metadata=command.metadata, message=str(e))
