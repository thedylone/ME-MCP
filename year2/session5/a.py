"""Explicit methods: Forward Euler and RK4"""

from typing import Callable
import numpy as np

from helpers.task import TaskBase, task_to_list


def ode(t: float, y: float) -> float:
    """ODE to solve"""
    return -2 * y * t - 2 * t**3


def fwd_euler(
    func: Callable, t0: float, y0: float, t_end: float, h: float
) -> tuple[np.ndarray, np.ndarray]:
    """Forward Euler method"""
    t: np.ndarray = np.arange(t0, t_end + h, h)
    y: np.ndarray = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * func(t[i - 1], y[i - 1])
    return t, y


def ode_rk4(
    func: Callable, t0: float, y0: float, t_end: float, h: float
) -> tuple[np.ndarray, np.ndarray]:
    """Runge-Kutta 4th order method"""
    t: np.ndarray = np.arange(t0, t_end + h, h)
    y: np.ndarray = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        k1 = h * func(t[i - 1], y[i - 1])
        k2 = h * func(t[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * func(t[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * func(t[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return t, y


class Task(TaskBase):
    """Explicit methods: Forward Euler and RK4"""

    tasklist: list = []

    t0: float = 0
    y0: float = -10
    t_end: float = 100
    h = 0.01

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Write a function, FwEuler(), to solve a general ODE:
        dy/dt = F(y,t)
        by adopting a forward Euler numerical scheme (slide 225). The function
        receives the initial condition, t0 and y0, the time step h and the
        desired final computational time t_end (all these input arguments are
        scalars).
        The function outputs two arrays, t and y, describing the solution y(t)
        both of dimensions 1 x Nt, where Nt is the number of temporal nodes
        computed.
        Within FwEuler(), the mathematical function F(t,y) can be evaluated by
        invoking a separate Python function func().
        Explicit methods are subject to instabilities: consider this when
        choosing the value for h."""
        t, y = fwd_euler(ode, self.t0, self.y0, self.t_end, self.h)
        return {"t": t, "y": y}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Write a function ODERK4() to perform as the function at point 1, but
        implementing the Runge-Kutta method instead (slide 232)."""
        t, y = ode_rk4(ode, self.t0, self.y0, self.t_end, self.h)
        return {"t": t, "y": y}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
