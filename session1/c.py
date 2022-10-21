class Task:
    def __init__(self) -> None:
        print("################")
        print("running Task C...")
        print("################")

    def task1(self):
        self.a = 10
        self.b = 5
        self.a, self.b = self.b, self.a
        print(f"task1: a is {self.a} and b is {self.b}")

    def task2(self):
        self.c = 20
        self.a, self.b, self.c = self.c, self.a, self.b
        print(f"task2: a, b, c is {self.a, self.b, self.c}")

    def runTasks(self):
        self.task1()
        self.task2()


if __name__ == "__main__":
    task = Task()
    task.runTasks()
