"""Trapezium rule for functions with non-equidistant nodes"""

import numpy as np

from helpers.task import TaskBase, task_to_list


def trapz(x: np.ndarray, y: np.ndarray) -> float:
    """Trapezium integration"""
    return sum(
        (x[i + 1] - x[i]) * (y[i + 1] + y[i]) / 2 for i in range(len(x) - 1)
    )


class Task(TaskBase):
    """Trapezium rule for functions with non-equidistant nodes"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write another Python function, trapz, receiving a set of points
        x and y, and outputting the numerical integral of y within the
        interval specified by x. The values in x might not be distanced at
        same intervals."""


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
