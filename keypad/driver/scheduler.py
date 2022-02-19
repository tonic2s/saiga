import time

class Scheduler:
    def __init__(self, time_func):
        self.tasks = []
        self.time_func = time_func

    def register_task(self, task: task.Task, refresh_time: int, priority: int):
        self.tasks.append({
            "task": task,
            "refresh_time": refresh_time,
            "priority": priority,
            "last_run_time": None
        })
        self.tasks.sort(key=lambda t: t["priority"])

    def start(self):
        for i, task in enumerate(self.tasks):
            current_time = time.monotonic()
            time_delta = current_time - task["last_run_time"]

            if time_delta > task["refresh_time"]:
                self.tasks[i]["last_run_time"] = current_time

                task["task"](time_delta)
