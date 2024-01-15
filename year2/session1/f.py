"""Slicing with conditions"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Slicing with conditions"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.x_array: np.ndarray = np.array([])
        self.ym_array: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Compute, with vectorised operations, the value:
        ym(x) = |y(x)| = |sin(x)|
        in the range x = [-5:5] with dx = 0.1"""
        self.x_array = np.arange(-5, 5 + 0.1, 0.1)
        y_array: np.ndarray = np.sin(self.x_array)
        self.ym_array = np.abs(y_array)
        plt.plot(self.x_array, y_array)
        plt.plot(self.x_array, self.ym_array)
        return {"x": self.x_array, "y": y_array, "ym": self.ym_array}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Compute the array ymsat such that:
        ymsat = 0 for -5 ≤ x ≤ 0
        ymsat = ym for x > 0 and ym ≤ 0.5
        ymsat = 0.5 for x > 0 and ym > 0.5
        """
        ymsat: np.ndarray = np.zeros(len(self.ym_array))
        ymsat[self.ym_array > 0.5] = 0.5
        ymsat[self.ym_array <= 0.5] = self.ym_array[self.ym_array <= 0.5]
        ymsat[self.x_array <= 0] = 0
        plt.plot(self.x_array, ymsat)
        plt.show()
        return {"ymsat": ymsat}


if __name__ == "__main__":
    task: Task = Task("F")
    task.run_tasks()
