from helpers.task import TaskBase


class Task(TaskBase):
    def __init__(self, name="") -> None:
        super().__init__(name)

    def task1(self):
        self.a = 10
        self.b = 5
        self.a, self.b = self.b, self.a
        print(f"task1: a is {self.a} and b is {self.b}")

    def task2(self):
        self.c = 20
        self.a, self.b, self.c = self.c, self.a, self.b
        print(f"task2: a, b, c is {self.a, self.b, self.c}")


if __name__ == "__main__":
    task = Task("C")
    task.runTasks()
