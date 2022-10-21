class TaskBase:
    def __init__(self) -> None:
        pass

    def runTasks(self, start=1):
        i = start
        while i > 0:
            try:
                eval(f"self.task{i}()")
                i += 1
            except Exception:
                break
