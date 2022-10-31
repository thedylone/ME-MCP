class TaskBase:
    def __init__(self, name, output=True) -> None:
        self.name = name
        self.output = output
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log("################")

    def task_to_list(list):
        def subtask(func):
            list.append(func)
            return func

        return subtask

    def runTasks(self):
        for task in self.tasklist:
            task(self)
        self.log("done")
        self.log("################")

    def log(self, msg, **vars):
        if not self.output:
            return
        if not vars:
            print(msg)
            return
        var_list = []
        msg += ":"
        for key, value in vars.items():
            var_list.append(f"{key} = {value}")
        var_str = "; ".join(var_list)
        print(msg, var_str)
