import json
import config

from task import Task

class MessageType:
    KEY_PRESSED = 1
    KEY_RELEASED = 2
    ENCODER_CHANGED = 3
    ERROR = 4

    def to_string(message_type: int):
        if message_type == MessageType.KEY_PRESSED:
            return "KEY_PRESSED"
        elif message_type == MessageType.KEY_RELEASED:
            return "KEY_RELEASED"
        elif message_type == MessageType.ENCODER_CHANGED:
            return "ENCODER_CHANGED"
        elif message_type == MessageType.ERROR:
            return "ERROR"

class Message:
    def __init__(self, id: int, message_type: MessageType, metadata: dict):
        self.id: int = id
        self.type: MessageType = message_type
        self.metadata: dict = metadata

    def __str__(self) -> str:
        return "#{} type={} metadata={}".format(self.id, MessageType.to_string(self.type), json.dumps(self.metadata))

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

class MessageBus(Task):
    SCHEDULE = { "update_time": 1, "priority": 50 }

    def __init__(self):
        self.messages = {}
        self.readers = []
        self.last_id = -1

    def push(self, message_type: MessageType, **metadata: dict):
        self.last_id += 1
        message = Message(self.last_id, message_type, metadata)

        self.messages[message.id] = message

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

    def advance(self, time_delta):
        self._cleanup()
