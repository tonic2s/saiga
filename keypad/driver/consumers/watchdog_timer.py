import config

from task import Task
from watchdog import WatchDogMode
from microcontroller import watchdog as RP2040Watchdog


class Watchdog(Task):
    SCHEDULE = { "update_time": 1, "priority": 100 }

    def __init__(self):
        # Setup watchdog with given timeout
        # Resets the system if not updated before timeout runs out

        RP2040Watchdog.timeout = config.WATCHDOG["TIMEOUT"]
        RP2040Watchdog.mode = WatchDogMode.RESET
        RP2040Watchdog.feed()

    async def advance(self):
        RP2040Watchdog.feed()
