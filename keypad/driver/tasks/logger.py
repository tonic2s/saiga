import time
import config

from task import Task
from messaging import CommandBus, InputType


class FileLogger(Task):
    UPDATE_TIME = 1

    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_reader = command_bus.subscribe()

        # Setup log file
        try:
            self.error_log = open(config.LOGGER["LOG_FILE_PATH"], "a")
            print("creted error log file", config.LOGGER["LOG_FILE_PATH"])
        except OSError as e:
            self.error_log = None
            command_bus.trigger(InputType.ERROR, source="FileLogger", message=str(e))
            print("error creating error log file", config.LOGGER["LOG_FILE_PATH"])

    async def advance(self):
        for command in self.command_reader:
            if command.type == InputType.ERROR and self.error_log:
                print("got error writing to file")
                self.error_log.write("ERROR {}: {}".format(time.monotonic(), command))


class ConsoleLogger(Task):
    def __init__(self, command_bus: CommandBus):
        # Setup command handing
        self.command_reader = command_bus.subscribe()

    async def advance(self):
        for command in self.command_reader:
            print(str(command))
