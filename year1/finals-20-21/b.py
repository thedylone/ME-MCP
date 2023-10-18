"""Task B"""

import os
import random
import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

CID: list[int] = list(map(int, list(os.environ.get("CID", "02345678"))))


class Task(TaskBase):
    """Task B"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Given the bell function:
        f(x) = e^(-(x-0.5)^2/sigma^2))
        Write a code to determine the ratio between the two shadowed areas
        (underneath and outside the bell) in the picture below. Set the
        value sigma = 0.1 + a/20, where a is the 6th digit of your CID."""
        inside_x: list[float] = []
        inside_y: list[float] = []
        outside_x: list[float] = []
        outside_y: list[float] = []
        sigma: float = 0.1 + CID[5] / 20
        limit = 10000
        for _ in range(limit):
            x_pos: float = random.random()
            y_pos: float = random.random()
            if y_pos <= math.exp(-((x_pos - 0.5) ** 2) / sigma**2):
                inside_x.append(x_pos)
                inside_y.append(y_pos)
            else:
                outside_x.append(x_pos)
                outside_y.append(y_pos)

        plt.scatter(inside_x, inside_y, color="red", s=1)
        plt.scatter(outside_x, outside_y, color="blue", s=1)
        plt.gca().set_aspect("equal")
        plt.show()
        return {"ratio": len(inside_x) / len(outside_x)}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
