"""Multi-dimensional arrays and grids"""

import numpy as np

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Multi-dimensional arrays and grids"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.x_array: np.ndarray = np.array([])
        self.y_array: np.ndarray = np.array([])
        self.matrix: list[np.ndarray] = []
        self.f_values: np.ndarray = np.array([])
        self.g_values: np.ndarray = np.array([])
        self.s_values: np.ndarray = np.array([])
        self.p_values: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Represent with appropriate variables the two functions:
        f(x, y) = sin x ∙ cos y
        g(x, y) = cos x ∙ sin y
        in the range x = [-2𝜋 : 2𝜋] and y = [-𝜋 : 2𝜋] with steps
        ∆x = ∆y = 0.1."""
        self.x_array: np.ndarray = np.arange(-2 * np.pi, 2 * np.pi + 0.1, 0.1)
        self.y_array: np.ndarray = np.arange(-np.pi, 2 * np.pi + 0.1, 0.1)
        self.matrix: list[np.ndarray] = np.meshgrid(self.x_array, self.y_array)
        self.f_values = np.sin(self.matrix[0]) * np.cos(self.matrix[1])
        self.g_values = np.cos(self.matrix[0]) * np.sin(self.matrix[1])
        return {"f": self.f_values, "g": self.g_values}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Compute the two functions:
        s(x, y) = f(x, y) + g(x, y)
        p(x, y) = f(x, y) ∙ g(x, y)"""
        self.s_values: np.ndarray = self.f_values + self.g_values
        self.p_values: np.ndarray = self.f_values * self.g_values
        return {"s": self.s_values, "p": self.p_values}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
