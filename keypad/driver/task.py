import time
import asyncio


class Task:
    UPDATE_TIME = None

    def advance(self):
        # abstract advance method has to be overwritten
        raise NotImplementedError()

    async def _advance(self):
        if self.UPDATE_TIME is None:
            raise ValueError("self.UPDATE_TIME", self.UPDATE_TIME)

        while True:
            await self.advance()
            await asyncio.sleep(self.UPDATE_TIME)


class TimedTask:
    UPDATE_TIME = None

    def __init__(self) -> None:
        self.last_excution = time.monotonic()

    def advance(self, time_delta):
        # abstract advance method has to be overwritten
        raise NotImplementedError()

    async def _advance(self):
        if self.UPDATE_TIME is None:
            raise ValueError("self.UPDATE_TIME", self.UPDATE_TIME)

        while True:
            current_time = time.monotonic()
            time_delta = self.last_excution - current_time
            self.last_excution = current_time

            await self.advance(time_delta)
            await asyncio.sleep(self.UPDATE_TIME)


