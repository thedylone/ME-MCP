from helpers.task import TaskBase
import session1.e


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        TaskE = session1.e.Task(output=False)
        TaskE.runTasks()
        self.A = TaskE.A
        self.B = TaskE.B

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        self.C = self.A[:6]
        return {"C": self.C}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        self.D = self.B[-6:]
        return {"D": self.D}

    @TaskBase.task_to_list(tasklist)
    def task3(self):
        self.E = self.C + self.D
        return {"E": self.E}

    @TaskBase.task_to_list(tasklist)
    def task4(self):
        i = self.E.index(13)
        j = self.E.index(26)
        self.F = self.E[i : j + 1]
        return {"F": self.F}

    @TaskBase.task_to_list(tasklist)
    def task5(self):
        self.G = self.F + self.C
        return {"G": self.G}

    @TaskBase.task_to_list(tasklist)
    def task6(self):
        self.C[1] = self.F[4] + self.C[4]
        return {"C": self.C}

    @TaskBase.task_to_list(tasklist)
    def task7(self):
        self.C[-1] = self.F[-1] + self.C[0]
        return {"C": self.C}


if __name__ == "__main__":
    task = Task("F")
    task.runTasks()
    print(task.C[2])
