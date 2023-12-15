"""Implicit methods: Backward Euler"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session5.a import Task as TaskA


def ode(t: float, y: float) -> float:
    """ODE to solve"""
    return -2 * y * t - 2 * t**3


class Task(TaskBase):
    """Implicit methods: Backward Euler"""

    tasklist: list = []

    t0: float = 0
    y0: float = -10
    t_end: float = 100
    h = 0.01

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        explicit_task: TaskA = TaskA("A", False)
        self.fwd_euler = explicit_task.task1()
        self.rk4 = explicit_task.task2()
        self.bwd_euler_t: np.ndarray
        self.bwd_euler_y: np.ndarray

    @staticmethod
    def bwd_euler(
        t0: float, y0: float, t_end: float, h: float
    ) -> tuple[np.ndarray, np.ndarray]:
        """Backward Euler method"""
        t: np.ndarray = np.arange(t0, t_end + h, h)
        y: np.ndarray = np.zeros(len(t))
        y[0] = y0
        for i in range(1, len(t)):
            y[i] = (y[i - 1] + h * -2 * t[i] ** 3) / (1 + 2 * h * t[i])
        return t, y

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Write a function, BwEuler(), to solve the above ODE by adopting a
        backward Euler numerical scheme (slide 225). The function receives the
        initial condition, t0 and y0, the time step h and the desired final
        computational time t_end (all these input arguments are scalars).
        The function outputs two arrays, t and y, describing the solution y(t)
        both of dimensions 1 x Nt, where Nt is the number of temporal nodes
        computed."""
        t, y = self.bwd_euler(self.t0, self.y0, self.t_end, self.h)
        self.bwd_euler_t = t
        self.bwd_euler_y = y
        return {"t": t, "y": y}

    @task_to_list(tasklist)
    def task2(self):
        """Plot, on the same graph, the solutions obtained from Task A1,
        Task A2, Task B1 and the analytical solution, vs time."""
        t = np.arange(self.t0, self.t_end + self.h, self.h)
        c = (self.y0 + self.t0**2 - 1) / np.exp(-self.t0**2)
        analytical = 1 - t**2 + c * np.exp(-(t**2))
        plt.plot(t, self.fwd_euler["y"], label="Fwd Euler")
        plt.plot(t, self.rk4["y"], label="RK4")
        plt.plot(t, self.bwd_euler_y, label="Bwd Euler")
        plt.plot(t, analytical, label="Analytical")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
