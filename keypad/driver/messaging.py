import json
import config

from task import Task


class MessageType:
    KEY_PRESSED = 1
    KEY_RELEASED = 2
    ENCODER_CHANGED = 3
    ERROR = 4
    COMMAND = 5

    def to_string(message_type: int):
        if message_type == MessageType.KEY_PRESSED:
            return "KEY_PRESSED"
        elif message_type == MessageType.KEY_RELEASED:
            return "KEY_RELEASED"
        elif message_type == MessageType.ENCODER_CHANGED:
            return "ENCODER_CHANGED"
        elif message_type == MessageType.ERROR:
            return "ERROR"
        elif message_type == MessageType.COMMAND:
            return "COMMAND"

class CommandType:
    SEND_KEYCODE = 1
    BRIGHTNESS_SET = 2
    BRIGHTNESS_UP = 3
    BRIGHTNESS_DOWN = 4
    HUE_SET = 5
    STATUS_BLINK = 6
    LIGHTING_PROGRAM_NEXT = 7,
    LIGHTING_PROGRAM_LAST = 8

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


class Message:
    def __init__(self, id: int, message_type: MessageType, metadata: dict, command: CommandType = None):
        self.id: int = id
        self.type: MessageType = message_type
        self.metadata: dict = metadata
        self.command: dict = command

    def __str__(self) -> str:
        return "#{} type={} command={} metadata={}".format(self.id, MessageType.to_string(self.type), CommandType.to_string(self.command), json.dumps(self.metadata))

class MessageReader:
    def __init__(self, message_bus):
        self.message_bus = message_bus

        if len(self.message_bus.messages) > 0:
            self.read_head = min(self.message_bus.messages)
        else:
            self.read_head = 0

    def __iter__(self):
        return self

    def __next__(self) -> Message:
        if self.read_head <= self.message_bus.last_id:
            message = self.message_bus.messages[self.read_head]
            self.read_head += 1

            return message
        else:
            raise StopIteration

    def unsubscribe(self):
        self.message_bus.readers.remove(self)

class MessageBus(Task):
    UPDATE_TIME = 1

    def __init__(self):
        self.messages = {}
        self.readers = []
        self.mediator = MessageCommandMediator(self)

        self.last_id = -1

    def push(self, message_type: MessageType, command=None, **metadata: dict):
        self.last_id += 1
        message = Message(self.last_id, message_type, metadata, command)

        self.messages[message.id] = message

        self.mediator.handle_message(message)

    def subscribe(self) -> MessageReader:
        # Subcribe to the bus. The caller commits to consume all events as soon as posible

        reader = MessageReader(self)
        self.readers.append(reader)

        return reader

    def _cleanup(self):
        oldest_read_message = min(self.readers, key=lambda r: r.read_head).read_head
        newest_message = self.last_id

        # max will remove newer messages if buffer size is reached or if every reader consumed them
        # this means some messages meight be lost when buffer size is reached but not every reader consumed them
        newest_allowed_message = max(oldest_read_message, newest_message - config.MESSAGE_BUS["BUFFER_SIZE"])

        for id, message in list(self.messages.items()):
            if message.id < newest_allowed_message:
                del self.messages[id]

    async def advance(self):
        self._cleanup()


class MessageCommandMediator:
    def __init__(self, message_bus: MessageBus):
        self.message_bus = message_bus

    def handle_message(self, message: Message):
        if message.type == MessageType.COMMAND:
            return

        elif message.type == MessageType.KEY_PRESSED:
            if message.metadata["row"] == 0 and message.metadata["column"] == 4:
                # upper rotary encoder
                self.message_bus.push(MessageType.COMMAND, command=CommandType.LIGHTING_PROGRAM_LAST)
            elif message.metadata["row"] == 1 and message.metadata["column"] == 4:
                # lower rotary encoder
                self.message_bus.push(MessageType.COMMAND, command=CommandType.LIGHTING_PROGRAM_NEXT)
            else:
                keycode = config.KEYBOARD["KEYMAP"][message.metadata["row"]][message.metadata["column"]]
                self.message_bus.push(MessageType.COMMAND, command=CommandType.SEND_KEYCODE, press=True, release=False, keycode=keycode)

        elif message.type == MessageType.KEY_RELEASED:
            if message.metadata["row"] == 0 and message.metadata["column"] == 4:
                # upper rotary encoder
                return
            elif message.metadata["row"] == 1 and message.metadata["column"] == 4:
                # lower rotary encoder
                return
            else:
                keycode = config.KEYBOARD["KEYMAP"][message.metadata["row"]][message.metadata["column"]]
                self.message_bus.push(MessageType.COMMAND, command=CommandType.SEND_KEYCODE, press=False, release=True, keycode=keycode)

        elif message.type == MessageType.ENCODER_CHANGED:
            if message.metadata["id"] == 0:
                hue = ((config.RGB_LIGHTS["DEFAULT_HUE"] + message.metadata["position"]) % 64) / 64
                self.message_bus.push(MessageType.COMMAND, command=CommandType.HUE_SET, hue=hue)

            elif message.metadata["id"] == 1:
                if message.metadata["delta"] > 0:
                    self.message_bus.push(MessageType.COMMAND, command=CommandType.BRIGHTNESS_UP)
                else:
                    self.message_bus.push(MessageType.COMMAND, command=CommandType.BRIGHTNESS_DOWN)

        elif message.type == MessageType.ERROR:
            self.message_bus.push(MessageType.COMMAND, command=CommandType.STATUS_BLINK, count=3)
