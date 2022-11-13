from helpers.task import TaskBase


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        var = 3.14
        varcopy = var
        var *= 2
        return {"var": var, "varcopy": varcopy}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        MyPints = 3
        drink2more = 2
        MyPints += drink2more
        MyPints += drink2more
        return {"MyPints": MyPints}

    @TaskBase.task_to_list(tasklist)
    def task3(self):
        Num = 3
        Den = 4
        Res = Num / Den
        return {"Res": Res}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
