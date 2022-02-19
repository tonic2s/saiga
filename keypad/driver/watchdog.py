from task import Task
from watchdog import WatchDogMode
from microcontroller import watchdog


class Watchdog(Task):
    def __init__(self, timeout: int):
        # Setup watchdog with given timeout
        # Resets the system if not updated before timeout runs out

        watchdog.timeout = timeout
        watchdog.mode = WatchDogMode.RESET
        watchdog.feed()

    def advance(self, time_delta):
        watchdog.feed()
