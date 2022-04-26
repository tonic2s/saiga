import json
import config

from task import Task


class InputType:
    KEY_PRESSED = 1
    KEY_RELEASED = 2
    ENCODER_CHANGED = 3
    ERROR = 4

    def to_string(message_type: int):
        if message_type == InputType.KEY_PRESSED:
            return "KEY_PRESSED"
        elif message_type == InputType.KEY_RELEASED:
            return "KEY_RELEASED"
        elif message_type == InputType.ENCODER_CHANGED:
            return "ENCODER_CHANGED"
        elif message_type == InputType.ERROR:
            return "ERROR"

class CommandType:
    LOG = 1
    STATUS_BLINK = 2
    KEYBOARD_SEND_KEYCODE = 3
    LIGHTING_CHANGE_BRIGHTNESS = 4
    LIGHTING_CHANGE_HUE = 5
    LIGHTING_CHANGE_SATURATION = 6
    LIGHTING_CHANGE_PROGRAM = 7
    LIGHTING_CHANGE_SECONDARY = 8
    CONSUMER_CONTROL_SEND = 9
    MOUSE_MOVE = 10
    MOUSE_SEND_BUTTON = 11
    MIDI_PLAY_NOTE = 12
    MIDI_CHANGE_OCTAVE = 13
    MIDI_CHANGE_TRANSPOSITION = 14
    MIDI_CHANGE_VELOCITY = 15
    MIDI_CHANGE_CHANNEL = 16
    MIDI_CONTROLLER = 17
    MIDI_MODULATION = 18

    def to_string(command_type: int):
        if command_type == CommandType.LOG:
            return "LOG"
        elif command_type == CommandType.STATUS_BLINK:
            return "STATUS_BLINK"
        elif command_type == CommandType.KEYBOARD_SEND_KEYCODE:
            return "KEYBOARD_SEND_KEYCODE"
        elif command_type == CommandType.LIGHTING_CHANGE_BRIGHTNESS:
            return "LIGHTING_CHANGE_BRIGHTNESS"
        elif command_type == CommandType.LIGHTING_CHANGE_HUE:
            return "LIGHTING_CHANGE_HUE"
        elif command_type == CommandType.LIGHTING_CHANGE_SATURATION:
            return "LIGHTING_CHANGE_SATURATION"
        elif command_type == CommandType.LIGHTING_CHANGE_PROGRAM:
            return "LIGHTING_CHANGE_PROGRAM"
        elif command_type == CommandType.LIGHTING_CHANGE_SECONDARY:
            return "LIGHTING_CHANGE_SECONDARY"
        elif command_type == CommandType.CONSUMER_CONTROL_SEND:
            return "CONSUMER_CONTROL_SEND"
        elif command_type == CommandType.MOUSE_MOVE:
            return "MOUSE_MOVE"
        elif command_type == CommandType.MOUSE_SEND_BUTTON:
            return "MOUSE_SEND_BUTTON"
        elif command_type == CommandType.MIDI_PLAY_NOTE:
            return "MIDI_PLAY_NOTE"
        elif command_type == CommandType.MIDI_CHANGE_OCTAVE:
            return "MIDI_CHANGE_OCTAVE"
        elif command_type == CommandType.MIDI_CHANGE_TRANSPOSITION:
            return "MIDI_CHANGE_TRANSPOSITION"
        elif command_type == CommandType.MIDI_CHANGE_VELOCITY:
            return "MIDI_CHANGE_VELOCITY"
        elif command_type == CommandType.MIDI_CHANGE_CHANNEL:
            return "MIDI_CHANGE_CHANNEL"
        elif command_type == CommandType.MIDI_CONTROLLER:
            return "MIDI_CONTROLLER"
        elif command_type == CommandType.MIDI_MODULATION:
            return "MIDI_MODULATION"


class Command:
    def __init__(self, command_type: CommandType, metadata: dict = None, **kwargs: dict):
        self.id: int = None
        self.type: dict = command_type
        self.metadata: dict = metadata if metadata is not None else kwargs

    def __str__(self) -> str:
        return "#{} command={} metadata={}".format(self.id, CommandType.to_string(self.type), json.dumps(self.metadata))

class CommandReader:
    def __init__(self, command_bus):
        self.command_bus = command_bus

        self.read_head = 0

    def __iter__(self):
        return self

    def __next__(self) -> Command:
        if len(self.command_bus.commands) > 0 and self.read_head <= self.command_bus.last_id:
            if self.read_head not in self.command_bus.commands:
                # if the command at the readhead does not exist any more, set the read head to the oldest message
                self.read_head = min(self.command_bus.commands)

            command = self.command_bus.commands[self.read_head]
            self.read_head += 1

            return command
        else:
            raise StopIteration

    def unsubscribe(self):
        self.command_bus.readers.remove(self)

class CommandBus(Task):
    UPDATE_TIME = 1

    def __init__(self):
        self.commands = {}
        self.readers = []
        self.input_handlers: list[AbstractInputHandler] = [
            config.KEYBOARD["ACTION_MAP"],
            config.ENCODERS["ACTION_MAP"]
        ]

        self.last_id = -1

    def trigger(self, input_type: InputType, **metadata: dict):
        for input_handler in self.input_handlers:
            for command in input_handler.handle_input(input_type, metadata):
                self._push_command(command)

        if input_type == InputType.ERROR:
            self.push(CommandType.STATUS_BLINK, count=3)
            self.push(CommandType.LOG, level="ERROR", **metadata)

    def push(self, command_type: CommandType, **metadata: dict):
        command = Command(command_type, metadata)
        self._push_command(command)

    def _push_command(self, command: Command):
        self.last_id += 1
        command.id = self.last_id

        self.commands[command.id] = command

    def subscribe(self) -> CommandReader:
        # Subcribe to the bus. The caller commits to consume all commands as soon as posible

        reader = CommandReader(self)
        self.readers.append(reader)

        return reader

    def _cleanup(self):
        if len(self.readers) == 0:
            return

        oldest_read_head = min(map(lambda r: r.read_head, self.readers))
        newest_command = self.last_id

        # max will remove old commands if buffer size is reached or if every reader consumed them
        # this means some commands meight be lost when buffer size is reached but not every reader consumed them
        newest_allowed_command = max(oldest_read_head, newest_command - config.COMMAND_BUS["BUFFER_SIZE"])

        if len(self.commands) - 2 > config.COMMAND_BUS["BUFFER_SIZE"]:
            self.push(CommandType.LOG, level="WARN", message="The command bus is overflowing, some commands will be lost", source="CommandBus")

        for id, command in list(self.commands.items()):
            if command.id < newest_allowed_command:
                del self.commands[id]

    async def advance(self):
        self._cleanup()


class AbstractInputHandler:
    def handle_input(self, message_type: InputType, metadata: dict):
        raise NotImplementedError()
