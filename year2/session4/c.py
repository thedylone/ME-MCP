"""Smoothing derivatives with polynomial interpolation. Launch of a rocket."""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session4.b import derivative_fwd
from year2.session3.c import splines


class Task(TaskBase):
    """Smoothing derivatives with polynomial interpolation. Launch of a rocket.
    A rocket is launched into space. After reaching the top point, the rocket
    descends back, with the deployment of a parachute. The trajectory of the
    rocket is depicted in Figure C. The actual values of the altitude are
    provided in the file Rocket.txt, taken at time intervals of 100sec."""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.time: np.ndarray
        self.altitudes: np.ndarray
        self.velocities: list[float] | np.ndarray
        self.accelerations: list[float] | np.ndarray

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[float] | np.ndarray]:
        """Compute the velocity and the acceleration of the rocket at the
        given nodal points, by using the function Derivative from Task B."""
        h = 100
        with open("year2/session4/Rocket.txt", encoding="utf-8") as file:
            self.altitudes = np.array([float(line) for line in file])
        self.time = np.arange(0, h * len(self.altitudes), h)
        self.velocities = derivative_fwd(1, h, self.altitudes)
        self.accelerations = derivative_fwd(2, h, self.altitudes)
        # 3 subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
        fig.suptitle("Rocket trajectory")
        ax1.scatter(self.time, self.altitudes, label="Altitude")
        ax1.legend()
        ax2.plot(self.time[:-1], self.velocities, label="Velocity")
        ax2.legend()
        ax3.plot(self.time[:-2], self.accelerations, label="Acceleration")
        ax3.legend()
        plt.show()
        return {
            "velocities": self.velocities,
            "accelerations": self.accelerations,
        }

    @task_to_list(tasklist)
    def task2(self):
        """Interpolate, with splines, the nodal points (xn, yn), for 140
        points over the same time domain. Recompute the velocity and the
        acceleration of the rocket at the interpolated points.
        (You need to use splines to avoid the Runge's phenomenon. In fact, if
        you use Lagrangian interpolation, and you can verify this yourself,
        the interpolated trajectory will suffer of the Runge's problem)."""
        h = 100 * len(self.altitudes) / 140
        x = np.linspace(0, 1300, 140)
        y = splines(self.time, self.altitudes, x, 0, 0)
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
        fig.suptitle("Rocket trajectory")
        ax1.scatter(x, y, label="Altitude")
        ax1.legend()
        velocities = derivative_fwd(1, h, y)
        accelerations = derivative_fwd(2, h, y)
        ax2.plot(x[:-1], velocities, label="Velocity")
        ax2.legend()
        ax3.plot(x[:-2], accelerations, label="Acceleration")
        ax3.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
