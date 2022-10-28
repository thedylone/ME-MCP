from helpers.task import TaskBase


class Task(TaskBase):
    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)

    def task1(self):
        a = 2
        b = 4
        c = a + b
        a += 1
        b = a
        c = a + b
        self.log("task1", c=c)

    def task2(self):
        x = 11
        y = -3
        z = 3 * x + y * y
        self.log("task2", z=z)


if __name__ == "__main__":
    task = Task("A")
    task.runTasks()
