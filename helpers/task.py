class TaskBase:
    def __init__(self, name) -> None:
        self.name = name
        print("################")
        print(f"running Task {self.name}...")
        print("################")

    def runTasks(self, start=1):
        i = start
        while i > 0:
            try:
                eval(f"self.task{i}()")
                i += 1
            except Exception:
                break
        print("done")
        print("################")
