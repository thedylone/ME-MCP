"""Heat conduction in a bar with a heat source"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import task_to_list
from year2.session7.a import Task as TaskA


def heat_conduction(
    alpha: float,
    k: float,
    h: float,
    a: float,
    b: float,
    Tw: float,
    T0: float,
    dt: float,
    dx: float,
    t_end: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Write a script to solve numerically the heat conduction equation.
    Input data for the problem are: the endpoints of the domain a and b,
    the values of the solution at these points, T(a) and T(b), the initial
    uniform temperature T0 for all spatial points, the time and spatial
    steps dt and dx, respectively, and the desired computational time span
    t_end. Output data for the problem are: the grid points x, the grid
    time t and the solution T(x,t) at every grid points for anytime
    between 0 and t_end."""
    x_range = np.arange(a, b + dx, dx)
    t_range = np.arange(0, t_end + dt, dt)
    T = np.zeros((len(x_range), len(t_range)))
    T[:, 0] = T0
    for i in range(1, len(t_range)):
        for j in range(len(x_range)):
            if j == 0:
                T[j, i] = (h * Tw + k / dx * T[j + 1, i - 1]) / (h + k / dx)
                continue
            if j == len(x_range) - 1:
                T[j, i] = (h * Tw + k / dx * T[j - 1, i - 1]) / (h + k / dx)
                continue
            if j == len(x_range) // 2:
                T[j, i] = 100
                continue
            T[j, i] = (
                alpha * dt / dx**2 * (T[j + 1, i - 1] + T[j - 1, i - 1])
                + (1 - 2 * alpha * dt / dx**2) * T[j, i - 1]
            )
    return x_range, t_range, T


class Task(TaskA):
    """Heat conduction in a bar with a heat source

    Consider the same bar as in Task A, with an initial uniform temperature of
    T = 10°C. The temperature of the middle point is suddenly increased to
    T = 100°C through a source and kept constant at this value. The bar is
    immersed in a large pool of water with constant temperature Tw = 5°C and
    is subject to convective heat exchange with the water, i.e.
    k dT/dx|a = h(Ta - Tw) and k dT/dx|b = h(Tb - Tw).
    The thermal conductivity for steel is k = 40 W/mK,
    and the heat transfer coefficient h = 500 W/m^2K."""

    tasklist: list = []
    k = 40
    h = 500
    Tw = 5

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Amend the script of Task A, to incorporate the mixed boundary
        conditions."""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Compute the temperature distribution with dt = 1s and dx = 0.01m.
        Plot the spatial distribution of the temperature within the bar at
        t = 0, t = 500s and t_end = 1200s."""
        x_range, t_range, T = heat_conduction(
            alpha=self.alpha,
            k=self.k,
            h=self.h,
            a=0,
            b=self.length,
            Tw=self.Tw,
            T0=self.t_0,
            dt=1,
            dx=0.01,
            t_end=1200,
        )
        plt.plot(x_range, T[:, 0], label="t = 0")
        plt.plot(x_range, T[:, 500], label="t = 500")
        plt.plot(x_range, T[:, 700], label="t = 700")
        plt.plot(x_range, T[:, 1000], label="t = 1000")
        plt.plot(x_range, T[:, -1], label="t = 1200")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
