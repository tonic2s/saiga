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
    BRIGHTNESS_UP = 3
    BRIGHTNESS_DOWN = 4
    HUE_SET = 5
    STATUS_BLINK = 6
    LIGHTING_PROGRAM_NEXT = 7
    LIGHTING_PROGRAM_LAST = 8
    FLAG_SET = 9
    LOG = 10

    def to_string(command_type: int):
        if command_type == CommandType.SEND_KEYCODE:
            return "SEND_KEYCODE"
        elif command_type == CommandType.BRIGHTNESS_SET:
            return "BRIGHTNESS_SET"
        elif command_type == CommandType.BRIGHTNESS_UP:
            return "BRIGHTNESS_UP"
        elif command_type == CommandType.BRIGHTNESS_DOWN:
            return "BRIGHTNESS_DOWN"
        elif command_type == CommandType.HUE_SET:
            return "HUE_SET"
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


class Command:
    def __init__(self, id: int, command_type: CommandType, metadata: dict):
        self.id: int = id
        self.type: dict = command_type
        self.metadata: dict = metadata

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
        self.command_generator = CommandGenerator(self)

        self.last_id = -1

    def trigger(self, input_type: InputType, **metadata: dict):
        self.command_generator.handle_message(input_type, metadata)

    def push(self, command_type: CommandType, **metadata: dict):
        self.last_id += 1
        command = Command(self.last_id, command_type, metadata)

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


class CommandGenerator:
    def __init__(self, command_bus: CommandBus):
        self.command_bus = command_bus

    def handle_message(self, message_type: InputType, metadata: dict):
        if message_type == InputType.KEY_PRESSED:
            if metadata["row"] == 0 and metadata["column"] == 4:
                # upper rotary encoder
                self.command_bus.push(CommandType.LIGHTING_PROGRAM_LAST)
            elif metadata["row"] == 1 and metadata["column"] == 4:
                # lower rotary encoder
                self.command_bus.push(CommandType.LIGHTING_PROGRAM_NEXT)
            else:
                keycode = config.KEYBOARD["KEYMAP"][metadata["row"]][metadata["column"]]
                self.command_bus.push(CommandType.SEND_KEYCODE, press=True, release=False, keycode=keycode)

        elif message_type == InputType.KEY_RELEASED:
            if metadata["row"] == 0 and metadata["column"] == 4:
                # upper rotary encoder
                return
            elif metadata["row"] == 1 and metadata["column"] == 4:
                # lower rotary encoder
                return
            else:
                keycode = config.KEYBOARD["KEYMAP"][metadata["row"]][metadata["column"]]
                self.command_bus.push(CommandType.SEND_KEYCODE, press=False, release=True, keycode=keycode)

        elif message_type == InputType.ENCODER_CHANGED:
            if metadata["id"] == 0:
                hue = ((config.RGB_LIGHTS["DEFAULT_HUE"] + metadata["position"]) % 64) / 64
                self.command_bus.push(CommandType.HUE_SET, hue=hue)
                self.command_bus.push(CommandType.FLAG_SET)

            elif metadata["id"] == 1:
                if metadata["delta"] > 0:
                    self.command_bus.push(CommandType.BRIGHTNESS_UP, value=0.05)
                else:
                    self.command_bus.push(CommandType.BRIGHTNESS_DOWN, value=0.05)


        elif message_type == InputType.ERROR:
            self.command_bus.push(CommandType.STATUS_BLINK, count=3)
            self.command_bus.push(CommandType.LOG, level="ERROR", **metadata)
