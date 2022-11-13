from helpers.task import TaskBase


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        self.a = str(2)
        self.b = 2

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        try:
            f = self.a + self.b
            return {"f": f}
        except Exception as e:
            return {"error": e}

    @TaskBase.task_to_list(tasklist)
    def task3(self):
        self.c = str(3)
        self.d = 3

    @TaskBase.task_to_list(tasklist)
    def task4(self):
        g = self.a + self.c
        h = self.b + self.d
        return {"g": g, "h": h}

    @TaskBase.task_to_list(tasklist)
    def task5(self):
        self.a = int(self.a)
        self.c = int(self.c)
        m = self.a + self.c
        return {"m": m, "m_type": type(m)}


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()
