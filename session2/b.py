from helpers.task import TaskBase
import session2.a


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        TaskA = session2.a.Task(output=False)
        TaskA.runTasks()
        self.A = TaskA.A
        self.D = []

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        self.A = [0 if i % 3 == 0 else v for i, v in enumerate(self.A)]
        return {"A": self.A}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        self.D = self.A[::-1]
        return {"D": self.D}


if __name__ == "__main__":
    task = Task("B")
    task.runTasks()
    print(task.D[69])
