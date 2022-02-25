import time
import task

class Scheduler:
    def __init__(self, time_func):
        self.tasks = []
        self.time_func = time_func

    def register_task(self, task: task.Task):
        self.tasks.append({
            "task": task,
            "last_run_time": time.monotonic() - task.SCHEDULE["update_time"]
        })
        self.tasks.sort(key=lambda t: t["task"].SCHEDULE["priority"])

        return task

    def start(self):
        while True:
            for i, task in enumerate(self.tasks):
                current_time = time.monotonic()
                time_delta = current_time - task["last_run_time"]

                if time_delta > task["task"].SCHEDULE["update_time"]:
                    self.tasks[i]["last_run_time"] = current_time

                    task["task"].advance(time_delta)
