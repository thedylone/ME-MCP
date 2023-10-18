"""Maths and plotting functions"""

import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Maths and plotting functions"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.list_x: list[int] = []
        self.list_y: list[float] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Set a list x with integer values from 1 to 100 in steps of 5."""
        self.list_x = list(range(1, 101, 5))
        return {"x": self.list_x}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[float]]:
        """Compute y = log10(x)."""
        self.list_y = list(map(lambda x: math.log(x, 10), self.list_x))
        return {"y": self.list_y}

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Plot y vs x."""
        plt.scatter(self.list_x, self.list_y)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
