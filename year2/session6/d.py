"""The shooting method: Blasius's boundary layer equation"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

from year2.session2.c import trapz
from year2.session3.a import lagr_interp
from year2.session5.c import fwd_euler_n


class Task(TaskBase):
    """The shooting method: Blasius's boundary layer equation
    The Blasius' equation, as given in ME2 Fluid Dynamics (boundary layer on a
    flat plate parallel to a uniform flow) is:
    d^3f(𝜂) / d𝜂^3 + 1/2 f(𝜂) d^2f(𝜂) / d𝜂^2 = 0
    with boundary conditions f(0) = 0, f'(0) = 0, f'(∞) = 1"""

    tasklist: list = []

    tol = 1.0e-5
    maxiter = 1000

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.t: np.ndarray = np.array([])
        self.y: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Solve numerically the ODE, plot the results for f(𝜂)
        and u(𝜂) = df/d𝜂"""

        def df(_t, _f, g, _h) -> float:
            """Blasius equation df/d𝜂"""
            return g

        def dg(_t, _f, _g, h) -> float:
            """Blasius equation d^2f/d𝜂^2"""
            return h

        def dh(_t, f, _g, h) -> float:
            """Blasius equation d^3f/d𝜂^3"""
            return -1 / 2 * f * h

        y0 = np.array([0, 0, 1.0])

        g_end = 1
        start = 0
        end = 10
        step = 0.01

        error = 100
        iterations = 0
        g_prev = 0
        h_prev = 0
        t: np.ndarray = np.array([])
        y: np.ndarray = np.array([])
        while error > self.tol and iterations < self.maxiter:
            iterations += 1
            t, y = fwd_euler_n([df, dg, dh], start, y0, end, step)
            g = [g_prev, y[-1, 1]]
            h = [h_prev, y0[2]]
            interp = lagr_interp(g, h, [g_end])
            error = abs(g[-1] - g_end)
            g_prev = g[-1]
            h_prev = h[-1]
            y0[2] = interp[0]

        print(f"iterations: {iterations}")
        print(f"error: {error}")
        self.t = t
        self.y = y
        plt.plot(t, y[:, 0], label="f(t)")
        plt.plot(t, y[:, 1], label="u(t)")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> dict[str, float]:
        """Determine the displacement thickness
        int_0^inf (1 - u(𝜂)) d𝜂
        and the momentum thickness
        int_0^inf (1 - u(𝜂)) u(𝜂) d𝜂
        (these two quantities will make physical sense after you are taught
        boundary layers in FMX2)."""
        displacement: float = trapz(self.t, 1 - self.y[:, 1])
        momentum: float = trapz(self.t, (1 - self.y[:, 1]) * self.y[:, 1])
        return {"displacement": displacement, "momentum": momentum}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
