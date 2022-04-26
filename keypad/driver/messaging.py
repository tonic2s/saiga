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
    SEND_KEYCODE = 1
    BRIGHTNESS_SET = 2
    BRIGHTNESS_CHANGE = 3
    HUE_CHANGE = 4
    SATURATION_CHANGE = 5
    STATUS_BLINK = 6
    LIGHTING_PROGRAM_NEXT = 7
    LIGHTING_PROGRAM_LAST = 8
    FLAG_SET = 9
    LOG = 10
    SEND_CONSUMER_CONTROL = 11
    MOUSE_MOVE = 12
    SEND_MOUSE_BUTTON = 13
    MIDI_PLAY_NOTE = 14
    MIDI_CHANGE_OCTAVE = 15
    MIDI_CHANGE_TRANSPOSITION = 16
    MIDI_CHANGE_VELOCITY = 17
    MIDI_CHANGE_CHANNEL = 18
    MIDI_CONTROLLER = 19
    MIDI_MODULATION = 20

    def to_string(command_type: int):
        if command_type == CommandType.SEND_KEYCODE:
            return "SEND_KEYCODE"
        elif command_type == CommandType.BRIGHTNESS_SET:
            return "BRIGHTNESS_SET"
        elif command_type == CommandType.BRIGHTNESS_CHANGE:
            return "BRIGHTNESS_CHANGE"
        elif command_type == CommandType.HUE_CHANGE:
            return "HUE_CHANGE"
        elif command_type == CommandType.SATURATION_CHANGE:
            return "SATURATION_CHANGE"
        elif command_type == CommandType.STATUS_BLINK:
            return "STATUS_BLINK"
        elif command_type == CommandType.LIGHTING_PROGRAM_NEXT:
            return "LIGHTING_PROGRAM_NEXT"
        elif command_type == CommandType.LIGHTING_PROGRAM_LAST:
            return "LIGHTING_PROGRAM_LAST"
        elif command_type == CommandType.FLAG_SET:
            return "FLAG_SET"
        elif command_type == CommandType.LOG:
            return "LOG"
        elif command_type == CommandType.SEND_CONSUMER_CONTROL:
            return "SEND_CONSUMER_CONTROL"
        elif command_type == CommandType.MOUSE_MOVE:
            return "MOUSE_MOVE"
        elif command_type == CommandType.SEND_MOUSE_BUTTON:
            return "SEND_MOUSE_BUTTON"
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
