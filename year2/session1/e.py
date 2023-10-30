"""Advanced plotting"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Advanced plotting"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """The two files Maths.txt and Computing.txt contain ME1 marks for the
        Maths and the Computing components, respectively. Read the two sets of
        data and round them to the nearest integer value.
        Plot in two subplots:
        a) the distribution of Maths marks AND the distribution of Computing
        marks as bar plot,
        b) the scattered correlation marks, i.e. Maths vs Computing marks."""
        with open("year2/session1/Maths.txt", "r", encoding="utf-8") as file:
            maths: list[int] = [
                round(float(line)) for line in file.readlines()
            ]
        with open(
            "year2/session1/Computing.txt", "r", encoding="utf-8"
        ) as file:
            computing: list[int] = [
                round(float(line)) for line in file.readlines()
            ]
        _fig, ax = plt.subplots(1, 2)
        ax[0].hist(maths, bins=10, color="blue", alpha=0.5)
        ax[0].hist(computing, bins=10, color="red", alpha=0.5)
        ax[1].scatter(maths, computing)
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Create a volumetric domain, with boundaries x = [-2:2], y = [-3:3],
        z = [-𝜋:2𝜋] and modal distances dx = dy = dz = 0.1.
        Evaluate the scalar function f(x,y,z) = x^2 + y^2 + z^2 - 5 sin^2(z)
        Plot the function f(x,y,z) with iso-surfaces"""
        x_array: np.ndarray = np.arange(-2, 2 + 0.1, 0.1)
        y_array: np.ndarray = np.arange(-3, 3 + 0.1, 0.1)
        z_array: np.ndarray = np.arange(-np.pi, 2 * np.pi + 0.1, 0.1)
        matrix: list[np.ndarray] = np.meshgrid(x_array, y_array, z_array)
        scalar_func = (
            matrix[0] ** 2
            + matrix[1] ** 2
            + matrix[2] ** 2
            - 5 * np.sin(matrix[2]) ** 2
        )
        fig = go.Figure(
            data=go.Isosurface(
                x=matrix[0].flatten(),
                y=matrix[1].flatten(),
                z=matrix[2].flatten(),
                value=scalar_func.flatten(),
                isomin=0,
                isomax=100,
                surface_count=3,
            )
        )
        fig.show()


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
