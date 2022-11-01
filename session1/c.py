from helpers.task import TaskBase


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        self.a = 10
        self.b = 5
        self.a, self.b = self.b, self.a
        return {"a": self.a, "b": self.b}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        self.c = 20
        self.a, self.b, self.c = self.c, self.a, self.b
        return {"a": self.a, "b": self.b, "c": self.c}


if __name__ == "__main__":
    task = Task("C")
    task.runTasks()
