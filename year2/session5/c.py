"""System of ODEs, with explicit methods"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def fwd_euler_n(
    funcs: list[Callable],
    t0: float,
    y0: np.ndarray,
    t_end: float,
    h: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Forward Euler method for a system of ODEs."""
    t: np.ndarray = np.arange(t0, t_end + h, h)
    y: np.ndarray = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        for j, func in enumerate(funcs):
            y[i, j] = y[i - 1, j] + h * func(t[i - 1], *y[i - 1])
    return t, y


class Task(TaskBase):
    """System of ODEs, with explicit methods.
    Modify the function FwEuler(), into a new function FwEulerN(), to solve a
    set of Nv given ODEs:
    dy1/dt = f1(t, y1, y2, ..., yNv)
    dy2/dt = f2(t, y1, y2, ..., yNv)
    dyNv/dt = fNv(t, y1, y2, ..., yNv)
    with initial conditions:
        y1(t0) = y1_0
        y2(t0) = y2_0
        yNv(t0) = yNv_0
    The function FwEulerN() receives as input: the initial and final
    computational time, t0 and t_end, and the time step h (all these input
    arguments are scalars); the vector Y0 with the initial values of the
    solution at t = t0 (Y0 has dimensions 1 x Nv), where Nv is the number of
    equations of the system (i.e., the number of variables solved).
    The function FwEulerN() outputs an array t of dimensions 1 x Nv and an
    array Y = [y1(t), y2(t), ..., yNv(t)] of dimensions Nv x Nt, with the
    solutions. Nt is the number of temporal nodes computed."""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """The spread of the virus can be modelled considering three classes
        of population:
        i) The number of susceptible individuals, S. These can be infected when
        exposed to the virus.
        ii) The number of infected individuals, I, growing with a rate a.
        iii) The number of recovered individuals, R. These have been infected
        and therefore become immune. The recovery rate is b.

        The dynamics of the three classes are described by the set of ODEs:
        dS/dt = -aSI
        dI/dt = aSI - bI
        dR/dt = bI

        Apply the function FwEulerN() to predict the number of S, I and R,
        with conditions"""

    @staticmethod
    def ds(a: float) -> Callable[[float, float, float, float], float]:
        """dS/dt = -aSI"""

        def f(_t, s: float, i: float, _r) -> float:
            return -a * s * i

        return f

    @staticmethod
    def di(
        a: float, b: float
    ) -> Callable[[float, float, float, float], float]:
        """dI/dt = aSI - bI"""

        def f(_t, s: float, i: float, _r) -> float:
            return a * s * i - b * i

        return f

    @staticmethod
    def dr(b: float) -> Callable[[float, float, float, float], float]:
        """dR/dt = bI"""

        def f(_t, _s, i: float, _r) -> float:
            return b * i

        return f

    @task_to_list(tasklist)
    def task1a(self) -> None:
        """a) Low infection rate: a = 0.001, b = 0.05, S(0) = 500, I(0) = 10,
        R(0) = 0, within the time window t0 = 0 to t_end = 100 with h= 0.05."""
        a = 0.001
        b = 0.05
        t0 = 0
        t_end = 100
        h = 0.05
        y0: np.ndarray = np.array([500, 10, 0])
        funcs = [self.ds(a), self.di(a, b), self.dr(b)]
        t, y = fwd_euler_n(funcs, t0, y0, t_end, h)
        plt.plot(t, y[:, 0], label="S")
        plt.plot(t, y[:, 1], label="I")
        plt.plot(t, y[:, 2], label="R")
        plt.legend()
        plt.title("Low infection rate")
        plt.show()

    @task_to_list(tasklist)
    def task1b(self) -> None:
        """b) High infection rate: a = 0.01, b = 0.05, S(0) = 500, I(0) = 10,
        R(0) = 0, within the time window t0 = 0 to t_end = 100 with h= 0.05."""
        a = 0.01
        b = 0.05
        t0 = 0
        t_end = 100
        h = 0.05
        y0: np.ndarray = np.array([500, 10, 0])
        funcs = [self.ds(a), self.di(a, b), self.dr(b)]
        t, y = fwd_euler_n(funcs, t0, y0, t_end, h)
        plt.plot(t, y[:, 0], label="S")
        plt.plot(t, y[:, 1], label="I")
        plt.plot(t, y[:, 2], label="R")
        plt.legend()
        plt.title("High infection rate")
        plt.show()

    @task_to_list(tasklist)
    def task1c(self) -> None:
        """c) Large time step: a = 0.01, b = 0.05, S(0) = 500, I(0) = 10,
        R(0) = 0, within the time window t0 = 0 to t_end = 100 with h= 0.5."""
        a = 0.01
        b = 0.05
        t0 = 0
        t_end = 100
        h = 0.5
        y0: np.ndarray = np.array([500, 10, 0])
        funcs = [self.ds(a), self.di(a, b), self.dr(b)]
        t, y = fwd_euler_n(funcs, t0, y0, t_end, h)
        plt.plot(t, y[:, 0], label="S")
        plt.plot(t, y[:, 1], label="I")
        plt.plot(t, y[:, 2], label="R")
        plt.legend()
        plt.title("Large time step")
        plt.show()

    @task_to_list(tasklist)
    def task1d(self) -> None:
        """d) Zero infection rate: a = 0, b = 0.05, S(0) = 500, I(0) = 10,
        R(0) = 0, within the time window t0 = 0 to t_end = 100 with h= 0.05."""
        a = 0
        b = 0.05
        t0 = 0
        t_end = 100
        h = 0.05
        y0: np.ndarray = np.array([500, 10, 0])
        funcs = [self.ds(a), self.di(a, b), self.dr(b)]
        t, y = fwd_euler_n(funcs, t0, y0, t_end, h)
        plt.plot(t, y[:, 0], label="S")
        plt.plot(t, y[:, 1], label="I")
        plt.plot(t, y[:, 2], label="R")
        plt.legend()
        plt.title("Zero infection rate")
        plt.show()

    @task_to_list(tasklist)
    def task2(self):
        """Financial model of the house market in London (Lotka-Volterra)
        The house market exhibits a periodic trend, where the number of houses
        sold, N, is interdependent with the average house prices, £.

        The set of ODEs describing the cycle is:
        d£/dt = 0.3£N - 0.8£
        dN/dt = 1.1N - N£
        where £(t) is the average house price (in 100k pounds) and N(t) is the
        number of houses sold (in thousands).

        Apply the function  FwEulerN() to predict the trend of £(t) and N(t),
        with initial conditions:
        £(0) = 0.8
        N(0) = 7
        over a period of 40 months, with a weekly step (i.e., h = 0.005).

        Plot, on the same graph, £(t) and N(t) vs time. Plot also, in a
        different figure, £(t) vs N(t)."""
        t0 = 0
        t_end = 40
        h = 0.005
        y0: np.ndarray = np.array([0.8, 7])
        funcs = [self.dp, self.dn]
        t, y = fwd_euler_n(funcs, t0, y0, t_end, h)
        plt.plot(t, y[:, 0], label="£")
        plt.plot(t, y[:, 1], label="N")
        plt.legend()
        plt.title("House market in London")
        plt.show()
        plt.plot(y[:, 0], y[:, 1])
        plt.xlabel("£")
        plt.ylabel("N")
        plt.title("House market in London")
        plt.show()

    @staticmethod
    def dp(_t, p: float, n: float) -> float:
        """d£/dt = 0.3£N - 0.8£"""
        return 0.3 * p * n - 0.8 * p

    @staticmethod
    def dn(_t, p: float, n: float) -> float:
        """dN/dt = 1.1N - N£"""
        return 1.1 * n - n * p


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
