"""Heat conduction in a bar"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def heat_conduction(
    alpha: float,
    a: float,
    b: float,
    Ta: float,
    Tb: float,
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
    T[0, :] = Ta
    T[-1, :] = Tb
    for i in range(1, len(t_range)):
        for j in range(1, len(x_range) - 1):
            T[j, i] = (
                alpha * dt / dx**2 * (T[j + 1, i - 1] + T[j - 1, i - 1])
                + (1 - 2 * alpha * dt / dx**2) * T[j, i - 1]
            )
    return x_range, t_range, T


class Task(TaskBase):
    """Heat conduction in a bar
    A steel bar (alpha = 1.172 * 10^-5 m^2/s) of length 0.5m is initially at a
    uniform temperature of T = 10°C. The two extremes are suddenly brought to
    a temperature of T = 50°C and kept at this temperature. Determine the
    temperature distribution within the bar after one hour."""

    tasklist: list = []
    alpha: float = 1.172 * 10**-5
    length: float = 0.5
    t_0: float = 10

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a script to solve numerically the heat conduction equation.
        Input data for the problem are: the endpoints of the domain a and b,
        the values of the solution at these points, T(a) and T(b), the initial
        uniform temperature T0 for all spatial points, the time and spatial
        steps dt and dx, respectively, and the desired computational time span
        t_end. Output data for the problem are: the grid points x, the grid
        time t and the solution T(x,t) at every grid points for anytime
        between 0 and t_end."""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Compute the temperature distribution with dt = 1s and dx = 0.01m.
        Plot T(x,t_end)."""
        x_range, t_range, T = heat_conduction(
            alpha=self.alpha,
            a=0,
            b=self.length,
            Ta=50,
            Tb=50,
            T0=self.t_0,
            dt=1,
            dx=0.01,
            t_end=3600,
        )
        plt.plot(x_range, T[:, -1])
        plt.xlabel("x")
        plt.ylabel("T")
        plt.show()

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Repeat the calculation with T(a) = 50 and T(b) = 70."""
        x_range, t_range, T = heat_conduction(
            alpha=self.alpha,
            a=0,
            b=self.length,
            Ta=50,
            Tb=70,
            T0=self.t_0,
            dt=1,
            dx=0.01,
            t_end=3600,
        )
        plt.plot(x_range, T[:, -1])
        plt.xlabel("x")
        plt.ylabel("T")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
