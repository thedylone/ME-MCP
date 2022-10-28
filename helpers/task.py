class TaskBase:
    def __init__(self, name, output=True) -> None:
        self.name = name
        self.output = output
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log("################")

    def runTasks(self, start=1):
        i = start
        while i > 0:
            try:
                eval(f"self.task{i}()")
                i += 1
            except Exception:
                break
        self.log("done")
        self.log("################")

    def log(self, msg):
        if self.output:
            print(msg)
