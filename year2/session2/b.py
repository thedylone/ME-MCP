"""Numerical integration of diverging improper integrals"""

import numpy as np

from helpers.task import task_to_list
from year2.session2.a import Task as TaskA


class Task(TaskA):
    """Numerical integration of diverging improper integrals"""

    tasklist: list = []

    @staticmethod
    def func(x: np.ndarray) -> np.ndarray:
        """Function to integrate"""
        return 1 / (x**1.10 + 2023) ** 0.5

    @staticmethod
    def integrate(b: float, n: int) -> float:
        """Integrate with custom number of nodes"""
        x: np.ndarray = np.linspace(0, b, n)
        return Task.trapzeqd(x, Task.func(x))

    @task_to_list(tasklist)
    def task4(self) -> None:
        """Recompute the numerical integrations as in Task A2 and A3, but with
        the integrand function:
        I = int_0^b 1/sqrt(x^1.10 + 2023) dx"""
        print(self.task2())
        print(self.task3())


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
