"""Maths and plotting functions"""

import math

import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Maths and plotting functions"""

    tasklist = []
    x = []
    y = []

    @task_to_list(tasklist)
    def task1(self):
        """Set a list x with integer values from 1 to 100 in steps of 5."""
        self.x = list(range(1, 101, 5))
        return {"x": self.x}

    @task_to_list(tasklist)
    def task2(self):
        """Compute y = log10(x)."""
        self.y = list(map(lambda x: math.log(x, 10), self.x))
        return {"y": self.y}

    @task_to_list(tasklist)
    def task3(self):
        """Plot y vs x."""
        plt.scatter(self.x, self.y)
        plt.show()


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
