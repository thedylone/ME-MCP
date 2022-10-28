from helpers.task import TaskBase


class Task(TaskBase):
    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)

    def task1(self):
        var = 3.14
        varcopy = var
        var *= 2
        self.log(f"task1: var is {var} and varcopy is {varcopy}")

    def task2(self):
        MyPints = 3
        drink2more = 2
        MyPints += drink2more
        MyPints += drink2more
        self.log(f"task2: MyPints is {MyPints}")

    def task3(self):
        Num = 3
        Den = 4
        Res = Num / Den
        self.log(f"task3: Res is {Res}")


if __name__ == "__main__":
    task = Task("B")
    task.runTasks()
