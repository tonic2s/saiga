import time
import config

from task import Task
from messaging import MessageBus, MessageType


class FileLogger(Task):
    UPDATE_TIME = 1

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_reader = message_bus.subscribe()

        # Setup log file
        try:
            self.error_log = open(config.LOGGER["LOG_FILE_PATH"], "a")
            print("creted error log file", config.LOGGER["LOG_FILE_PATH"])
        except OSError as e:
            self.error_log = None
            message_bus.push(MessageType.ERROR, source="FileLogger", message=str(e))
            print("error creating error log file", config.LOGGER["LOG_FILE_PATH"])

    async def advance(self):
        for message in self.message_reader:
            if message.type == MessageType.ERROR and self.error_log:
                print("got error writing to file")
                self.error_log.write("ERROR {}: {}".format(time.monotonic(), message))


class ConsoleLogger(Task):
    UPDATE_TIME = 0.25

    def __init__(self, message_bus: MessageBus):
        # Setup message handing
        self.message_reader = message_bus.subscribe()

    async def advance(self):
        for message in self.message_reader:
            print(str(message))
