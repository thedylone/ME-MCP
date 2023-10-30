"""Surface plots"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session1.b import Task as TaskB


class Task(TaskBase):
    """Surface plots"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.task_b: TaskB = TaskB()
        self.task_b.run_tasks()
        self.t_array: np.ndarray = np.array([])
        self.matrix_t: list[np.ndarray] = []
        self.r_values: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Plot, both with a surface plot and a contour plot separately, the
        functions s(x, y) and p(x, y) of Task B."""
        # Surface plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d", title="Surface plot")
        ax.plot_surface(
            self.task_b.matrix[0], self.task_b.matrix[1], self.task_b.s_values
        )
        ax.plot_surface(
            self.task_b.matrix[0], self.task_b.matrix[1], self.task_b.p_values
        )
        plt.show()
        # Contour plot
        fig = plt.figure()
        ax = fig.add_subplot(111, title="Contour plot")
        ax.contour(
            self.task_b.matrix[0], self.task_b.matrix[1], self.task_b.s_values
        )
        ax.contour(
            self.task_b.matrix[0], self.task_b.matrix[1], self.task_b.p_values
        )
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Consider the function:
        r(x, y, t) = f(x, y) ∙ e**(-0.5t)

        in the same range of x and y as in Task B and t = [0 : 10]
        with ∆t = 0.05.
        """
        self.t_array = np.arange(0, 10 + 0.05, 0.05)
        self.matrix_t = np.meshgrid(
            self.task_b.x_array, self.task_b.y_array, self.t_array
        )
        self.r_values = (
            np.sin(self.matrix_t[0])
            * np.cos(self.matrix_t[1])
            * np.exp(-0.5 * self.matrix_t[2])
        )
        return {"r": self.r_values}

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Plot, with a surface plot, r(x, y, t = 0) and r(x, y, t = 5)."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d", title="Surface plot")
        x_vals: np.ndarray = self.matrix_t[0][:, :, 0]
        y_vals: np.ndarray = self.matrix_t[1][:, :, 0]
        ax.plot_surface(x_vals, y_vals, self.r_values[:, :, 0])
        ax.plot_surface(
            x_vals, y_vals, self.r_values[:, :, len(self.t_array) // 2]
        )
        plt.show()

    @task_to_list(tasklist)
    def task4(self) -> None:
        """Plot the evolution along t of r(x, y, t) at x = 𝜋 and y = -𝜋/2."""
        fig = plt.figure()
        ax = fig.add_subplot(111, title="Evolution along t")
        # x = 𝜋 means index 3/4 of x_array
        # y = -𝜋/2 means index 1/6 of y_array
        ax.plot(
            self.t_array,
            self.r_values[
                3 * len(self.task_b.x_array) // 4,
                len(self.task_b.y_array) // 6,
                :,
            ],
        )
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
