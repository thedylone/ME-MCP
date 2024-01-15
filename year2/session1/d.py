"""Vector plots"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Vector plots"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.x_array: np.ndarray = np.array([])
        self.y_array: np.ndarray = np.array([])
        self.matrix: list[np.ndarray] = []
        self.f_vector: np.ndarray = np.array([])
        self.g_vector: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Divergence and curl of vectors
        f = xi + yj
        g = yi - xj
        Represent with appropriate variables the two vector fields f(x,y,z) in
        the range x = y = [-5:5] with intervals dx = dy = 0.1
        """
        self.x_array: np.ndarray = np.arange(-5, 5 + 0.1, 0.1)
        self.y_array: np.ndarray = np.arange(-5, 5 + 0.1, 0.1)
        self.matrix: list[np.ndarray] = np.meshgrid(self.x_array, self.y_array)
        self.f_vector: np.ndarray = np.ndarray(
            (len(self.x_array), len(self.y_array), 2)
        )
        self.f_vector[:, :, 0] = self.matrix[0]
        self.f_vector[:, :, 1] = self.matrix[1]
        self.g_vector: np.ndarray = np.ndarray(
            (len(self.x_array), len(self.y_array), 2)
        )
        self.g_vector[:, :, 0] = self.matrix[1]
        self.g_vector[:, :, 1] = -self.matrix[0]
        return {"f_vector": self.f_vector, "g_vector": self.g_vector}

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Plot as quivers and streamlines the two vector fields f, and
        observe whether the fields are conservatives, irrotational, etc."""
        _fig, ax = plt.subplots(1, 2)
        ax[0].quiver(
            self.matrix[0],
            self.matrix[1],
            self.f_vector[:, :, 0],
            self.f_vector[:, :, 1],
        )
        ax[0].streamplot(
            self.matrix[0],
            self.matrix[1],
            self.f_vector[:, :, 0],
            self.f_vector[:, :, 1],
        )
        ax[0].set_title("f vector")
        ax[1].quiver(
            self.matrix[0],
            self.matrix[1],
            self.g_vector[:, :, 0],
            self.g_vector[:, :, 1],
        )
        ax[1].streamplot(
            self.matrix[0],
            self.matrix[1],
            self.g_vector[:, :, 0],
            self.g_vector[:, :, 1],
        )
        ax[1].set_title("g vector")
        plt.show()

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Helmholtz decomposition
        The vector u(x,y) = (4x + 14y)i + (-6x - 11y)j can be decomposed into
        an irrotational component and an incompressible component.
        Plot the two components and the overall vector u(x,y)
        within the same domain as above."""
        matrix = np.array([[4, 14], [-6, -11]])
        original_vector: np.ndarray = np.ndarray(
            (len(self.x_array), len(self.y_array), 2)
        )
        original_vector[:, :, 0] = (
            matrix[0][0] * self.matrix[0] + matrix[0][1] * self.matrix[1]
        )
        original_vector[:, :, 1] = (
            matrix[1][0] * self.matrix[0] + matrix[1][1] * self.matrix[1]
        )
        irrotational = (matrix + matrix.T) / 2
        incompressible = (matrix - matrix.T) / 2
        irr_vector: np.ndarray = np.ndarray(
            (len(self.x_array), len(self.y_array), 2)
        )
        irr_vector[:, :, 0] = (
            irrotational[0][0] * self.matrix[0]
            + irrotational[0][1] * self.matrix[1]
        )
        irr_vector[:, :, 1] = (
            irrotational[1][0] * self.matrix[0]
            + irrotational[1][1] * self.matrix[1]
        )
        inc_vector: np.ndarray = np.ndarray(
            (len(self.x_array), len(self.y_array), 2)
        )
        inc_vector[:, :, 0] = (
            incompressible[0][0] * self.matrix[0]
            + incompressible[0][1] * self.matrix[1]
        )
        inc_vector[:, :, 1] = (
            incompressible[1][0] * self.matrix[0]
            + incompressible[1][1] * self.matrix[1]
        )
        _fig, ax = plt.subplots(1, 3)
        ax[0].quiver(
            self.matrix[0],
            self.matrix[1],
            original_vector[:, :, 0],
            original_vector[:, :, 1],
        )
        ax[1].quiver(
            self.matrix[0],
            self.matrix[1],
            irr_vector[:, :, 0],
            irr_vector[:, :, 1],
        )
        ax[2].quiver(
            self.matrix[0],
            self.matrix[1],
            inc_vector[:, :, 0],
            inc_vector[:, :, 1],
        )
        plt.show()


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
