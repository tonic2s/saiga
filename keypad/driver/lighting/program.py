class LightingProgram:
    def advance(self):
        raise NotImplementedError()

    def deinit(self):
        pass


class TimedLightingProgram:
    def advance(self, time_delta):
        raise NotImplementedError()

    def deinit(self):
        pass
