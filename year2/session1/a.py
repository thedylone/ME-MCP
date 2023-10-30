"""Generate an array with a non-uniform range"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Generate an array with a non-uniform range"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.x_array: np.ndarray = np.array([])
        self.f_values: np.ndarray = np.array([])
        self.g_values: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Generate an array x of numbers in the range [-5 : 5] with the
        following steps:

        ∆x = 0.5 in -5 ≤ x ≤ -2
        ∆x = 0.05 in -2 < x < 3
        ∆x = 0.5 in 3 ≤ x ≤ 5"""
        x_array: list[float] = []
        for i in np.arange(-5, -2, 0.5):
            x_array.append(i)
        for i in np.arange(-2, 3, 0.05):
            x_array.append(i)
        for i in np.arange(3, 5, 0.5):
            x_array.append(i)
        self.x_array = np.array(x_array)
        return {"x": self.x_array}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Compute the functions: f = sin(x) and g = sin(x**2+ 𝜋)"""
        self.f_values = np.sin(self.x_array)
        self.g_values = np.sin(self.x_array**2 + np.pi)
        return {"f": self.f_values, "g": self.g_values}

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Plot, with scattered points, on the same graph, f(x) and g(x),
        with red diamond and purple circle seeds, respectively."""
        plt.scatter(
            self.x_array, self.f_values, c="r", marker=MarkerStyle("D")
        )
        plt.scatter(
            self.x_array, self.g_values, c="purple", marker=MarkerStyle("o")
        )
        plt.show()


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
