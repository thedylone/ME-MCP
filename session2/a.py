from helpers.task import TaskBase


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.A = []
        self.B = []
        self.C = []

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        self.A = list(range(1, 101))
        return {"A": self.A}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        self.B = list(map(lambda x: x * x, self.A))
        return {"B": self.B}

    @TaskBase.task_to_list(tasklist)
    def task3(self):
        self.C = list(map(sum, zip(self.A, self.B)))
        return {"C": self.C}


if __name__ == "__main__":
    task = Task("A")
    task.runTasks()
    print(task.C[9])
