"""PDE with multiple spatial dimensions: baking a potato in the oven"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def heat_conduction_2d_potato(
    alpha_air: float,
    alpha_potato: float,
    potato_xlen: float,
    potato_ylen: float,
    xa: float,
    xb: float,
    ya: float,
    yb: float,
    Txa: float,
    Txb: float,
    Tya: float,
    Tyb: float,
    T0: float,
    dt: float,
    dx: float,
    dy: float,
    t_end: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x_range = np.arange(xa, xb + dx, dx)
    y_range = np.arange(ya, yb + dy, dy)
    t_range = np.arange(0, t_end + dt, dt)
    alpha = np.zeros((len(x_range), len(y_range)))
    alpha[:, :] = alpha_air
    xap = int((xa + xb - potato_xlen) / 2 / dx)
    xbp = int((xa + xb + potato_xlen) / 2 / dx)
    yap = int((ya + yb - potato_ylen) / 2 / dy)
    ybp = int((ya + yb + potato_ylen) / 2 / dy)
    alpha[xap:xbp, yap:ybp] = alpha_potato
    T = np.zeros((len(x_range), len(y_range), len(t_range)))
    T[:, :, 0] = T0
    T[0, :, :] = Txa
    T[-1, :, :] = Txb
    T[:, 0, :] = Tya
    T[:, -1, :] = Tyb
    T[xap:xbp, yap:ybp, 0] = -15
    for i in range(1, len(t_range)):
        for j in range(1, len(x_range) - 1):
            for k in range(1, len(y_range) - 1):
                T[j, k, i] = (
                    alpha[j, k]
                    * dt
                    / dx**2
                    * (T[j + 1, k, i - 1] + T[j - 1, k, i - 1])
                    + alpha[j, k]
                    * dt
                    / dy**2
                    * (T[j, k + 1, i - 1] + T[j, k - 1, i - 1])
                    + (
                        1
                        - 2 * alpha[j, k] * dt / dx**2
                        - 2 * alpha[j, k] * dt / dy**2
                    )
                    * T[j, k, i - 1]
                )
    return x_range, y_range, t_range, T


class Task(TaskBase):
    """PDE with multiple spatial dimensions: baking a potato in the oven
    A (two dimensional) traditional oven can be represented with the
    discretisation grid
    The heat equation within the oven is described by the PDE:
    dT/dt = alpha * (d^2T/dx^2 + d^2T/dy^2)
    The oven, inside, is initially at room temperature T0 = 25°C. A frozen
    potato, with an initial temperature T0 = -15°C, is positioned centrally in
    the middle of the oven. The walls of the oven are heated at a constant
    temperature of T0 = 180°C."""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a script to solve numerically the heat conduction equation.
        The thermal diffusivity of air in the oven is alpha = 1.9 * 10^-5 m^2/s
        The thermal diffusivity of the potato is alpha = 1.3 * 10^-7 m^2/s."""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Compute T(x,y,u) with dx = dy = 0.01m, dt = 1."""

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Plot the 2-D temperature profile at various time steps, to observe
        how the potato is baking."""
        x_range, y_range, t_range, T = heat_conduction_2d_potato(
            alpha_air=1.9 * 10**-5,
            alpha_potato=1.3 * 10**-7,
            potato_xlen=0.06,
            potato_ylen=0.06,
            xa=0,
            xb=0.4,
            ya=0,
            yb=0.4,
            Txa=180,
            Txb=180,
            Tya=180,
            Tyb=180,
            T0=25,
            dt=1,
            dx=0.01,
            dy=0.01,
            t_end=7200,
        )
        # 2d heat map
        # t = 0s
        plt.imshow(T[:, :, 0], vmin=-15, vmax=180)
        plt.colorbar()
        plt.title("t = 0s")
        plt.show()
        # t = 600s
        plt.imshow(T[:, :, 600], vmin=-15, vmax=180)
        plt.colorbar()
        plt.title("t = 600s")
        plt.show()
        # t = 1800s
        plt.imshow(T[:, :, 1800], vmin=-15, vmax=180)
        plt.colorbar()
        plt.title("t = 1800s")
        plt.show()
        # t = 3600s
        plt.imshow(T[:, :, 3600], vmin=-15, vmax=180)
        plt.colorbar()
        plt.title("t = 3600s")
        plt.show()
        # t = 7200s
        plt.imshow(T[:, :, -1], vmin=-15, vmax=180)
        plt.colorbar()
        plt.title("t = 7200s")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
