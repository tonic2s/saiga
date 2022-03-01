import time
import asyncio
import traceback


class Task:
    UPDATE_TIME = 0

    async def advance(self):
        # abstract advance method has to be overwritten
        raise NotImplementedError()

    async def _advance(self):
        try:
            while True:
                await self.advance()
                await asyncio.sleep(self.UPDATE_TIME)

        except Exception as e:
            print("TASK EXCEPTION", self, ":", traceback.format_exception(BaseException, e, e.__traceback__))

class TimedTask:
    UPDATE_TIME = 0

    def __init__(self) -> None:
        self.last_excution = time.monotonic()

    async def advance(self, time_delta):
        # abstract advance method has to be overwritten
        raise NotImplementedError()

    async def _advance(self):
        try:
            while True:
                current_time = time.monotonic()
                time_delta = current_time - self.last_excution
                self.last_excution = current_time

                await self.advance(time_delta)
                await asyncio.sleep(self.UPDATE_TIME)

        except Exception as e:
            print("TASK EXCEPTION", self, ":", traceback.format_exception(BaseException, e, e.__traceback__))
