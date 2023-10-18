"""Further skills"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from year1.session10.a import Task as TaskA


class Task(TaskBase):
    """Further skills"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """For this set of linear equations:
        4x + 3y = 2
        8x + 6y = 1
        Plot the two equations, each as a line y vs x, on the same graph.
        Solve them numerically: what does it happen?"""
        x_vals: np.ndarray = np.linspace(-1, 1, 100)
        y1_vals: np.ndarray = (2 - 4 * x_vals) / 3
        y2_vals: np.ndarray = (1 - 8 * x_vals) / 6
        plt.plot(x_vals, y1_vals, x_vals, y2_vals)
        plt.show()
        matrix_a: np.ndarray = np.array([[4, 3], [8, 6]])
        vector_b: np.ndarray = np.array([2, 1])
        vector_x: np.ndarray = TaskA.gauss_elim(matrix_a, vector_b)
        return {"vector_x": vector_x}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """There are cases, when the solution exists, where numerical methods
        can provide completely inaccurate results. These cases are said to be
        ill conditioned.
        Consider these two sets of linear equations:
        400x - 201y = 200
        -800x + 401y = -200

        and

        401x - 201y = 200
        -800x + 401y = -200

        Solve the two sets of equations separately. How do the numerical
        solutions differ from each other?
        """
        # first set
        matrix_a1: np.ndarray = np.array([[400, -201], [-800, 401]])
        vector_b1: np.ndarray = np.array([200, -200])
        vector_x1: np.ndarray = TaskA.gauss_elim(matrix_a1, vector_b1)
        # second set
        matrix_a2: np.ndarray = np.array([[401, -201], [-800, 401]])
        vector_b2: np.ndarray = np.array([200, -200])
        vector_x2: np.ndarray = TaskA.gauss_elim(matrix_a2, vector_b2)
        return {"vector_x1": vector_x1, "vector_x2": vector_x2}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
