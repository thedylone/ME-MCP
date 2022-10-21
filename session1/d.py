class Task:
    def __init__(self) -> None:
        print("################")
        print("running Task D...")
        print("################")

    def task1(self):
        self.a = str(2)
        self.b = 2

    def task2(self):
        try:
            f = self.a + self.b
            print(f)
        except Exception as e:
            print(f"task2: {e}")

    def task3(self):
        self.c = str(3)
        self.d = 3

    def task4(self):
        g = self.a + self.c
        h = self.b + self.d
        print(f"g: {g}, h: {h}")

    def task5(self):
        self.a = int(self.a)
        self.c = int(self.c)
        m = self.a + self.c
        print(f"m: {m}, type: {type(m)}")

    def runTasks(self):
        self.task1()
        self.task2()
        self.task3()
        self.task4()
        self.task5()


if __name__ == "__main__":
    task = Task()
    task.runTasks()
