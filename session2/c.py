from helpers.task import TaskBase


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.x = []
        self.y = []

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        self.x = list(range(1, 101, 5))
        return {"x": self.x}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        import math

        self.y = list(map(lambda x: math.log(x, 10), self.x))
        return {"y": self.y}

    @TaskBase.task_to_list(tasklist)
    def task3(self):
        import matplotlib.pyplot as plt

        plt.scatter(self.x, self.y)
        plt.show()


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
