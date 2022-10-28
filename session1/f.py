from helpers.task import TaskBase
import e


class Task(TaskBase):
    def __init__(self, name="") -> None:
        super().__init__(name)
        TaskE = e.Task()
        TaskE.runTasks()
        self.A = TaskE.A
        self.B = TaskE.B

    def task1(self):
        self.C = self.A[:6]
        print(f"task1: C: {self.C}")

    def task2(self):
        self.D = self.B[-6:]
        print(f"task2: D: {self.D}")

    def task3(self):
        self.E = self.C + self.D
        print(f"task3: E: {self.E}")

    def task4(self):
        i = self.E.index(13)
        j = self.E.index(26)
        self.F = self.E[i : j + 1]
        print(f"task4: F: {self.F}")

    def task5(self):
        self.G = self.F + self.C
        print(f"task5: G: {self.G}")

    def task6(self):
        self.C[1] = self.F[4] + self.C[4]
        print(f"task6: C: {self.C}")

    def task7(self):
        self.C[-1] = self.F[-1] + self.C[0]
        print(f"task7: C: {self.C}")


if __name__ == "__main__":
    task = Task("F")
    task.runTasks()
    print(task.C[2])
