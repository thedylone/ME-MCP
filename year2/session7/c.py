"""Stability of the finite difference numerical method"""

import matplotlib.pyplot as plt

from helpers.task import task_to_list
from year2.session7.a import heat_conduction, Task as TaskA


class Task(TaskA):
    """Stability of the finite difference numerical method

    Solving numerically a time marching PDE with boundary conditions can be
    easily unstable and careful attention is needed.
    Once the time step dt becomes too large the last term in Equation 1,
    (1 - 2*alpha*dt/dx^2), becomes negative. The same is true if dx is reduced.
    When this term is negative the numerical computation is unstable:
    errors are introduced and amplified at every successive time step.
    Therefore, in order for the solution to converge it must be:
    alpha * dt / dx^2 <= 0.5
    This is a stability criterion, also known as the Courant condition of
    stability, and poses a restrain between dx and dt. For a chosen dx there
    must be a maximum dt to ensure numerical stability.
    Use the script for Task A, with T(a) = 50 and T(b) = 50."""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Compute T(x, t_end) with dt = 1s and dx = 0.01m, dx = 0.05m
        and dx = 0.001m. Calculate the Courant condition for all the three
        cases and plot T(x, t_end)."""
        dt = 1
        courant: dict[str, float] = {}
        dxs: list[float] = [0.01, 0.05, 0.001]
        for dx in dxs:
            x_range, t_range, T = heat_conduction(
                alpha=self.alpha,
                a=0,
                b=self.length,
                Ta=50,
                Tb=50,
                T0=self.t_0,
                dt=dt,
                dx=dx,
                t_end=3600,
            )
            courant[str(dx)] = self.alpha * dt / dx**2
            plt.plot(x_range, T[:, -1], label=f"dx = {dx}")
        plt.xlabel("x")
        plt.ylabel("T")
        plt.legend()
        plt.show()
        return courant

    @task_to_list(tasklist)
    def task2(self):
        """Repeat the calculation with dx = 0.001m and a reduced dt = 0.04s."""
        dt = 0.04
        dx = 0.001
        x_range, t_range, T = heat_conduction(
            alpha=self.alpha,
            a=0,
            b=self.length,
            Ta=50,
            Tb=50,
            T0=self.t_0,
            dt=dt,
            dx=dx,
            t_end=3600,
        )
        plt.plot(x_range, T[:, -1])
        plt.xlabel("x")
        plt.ylabel("T")
        plt.show()
        return {f"dx = {dx} at dt = {dt}": self.alpha * dt / dx**2}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
