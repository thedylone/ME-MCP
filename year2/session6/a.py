"""Direct methods"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def ode_bc(
    ode: Callable, a: float, b: float, y_a: float, y_b: float, N: int
) -> tuple:
    """Solve a boundary value problem for a second-order ODE."""
    x: np.ndarray
    x, _h = np.linspace(a, b, N + 1, retstep=True)
    h = float(_h)
    A = np.zeros((N + 1, N + 1))
    B = np.zeros(N + 1)
    A[0, 0] = 1
    A[N, N] = 1
    B[0] = y_a
    B[N] = y_b
    for i in range(1, N):
        f, g, p = ode(x[i])
        A[i, i - 1] = 1 / h**2 - f / (2 * h)
        A[i, i] = -2 / h**2 + g
        A[i, i + 1] = 1 / h**2 + f / (2 * h)
        B[i] = p
    y = np.linalg.solve(A, B)
    return x, y


class Task(TaskBase):
    """Direct methods

    d^2y/dx^2 + f(x) dy/dx + g(x) y = p(x)
    """

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function, myodebc, that receives the boundaries of the
        domain a and b, the value of the solutions at these points, y(a) = y_a
        and y(b) = y_b, and the number N of desired intervals. myodebc returns
        the grid points x_i and the solution y_i(x_i) at the grid points.
        The ODE is defined through an external function, myfunc, that receives
        the value of x and returns the values of f(x), g(x) and p(x)."""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Solve the ODE d^2y/dx^2 + 2x dy/dx + 2y - cos(3x) = 0, in the domain
        [0, 𝜋], with boundary conditions y(0) = 1.5 and y(𝜋) = 0. Discretise
        the domain with 10 intervals. Plot y(x)."""

        def ode(x: float) -> tuple:
            return 2 * x, 2, np.cos(3 * x)

        x, y = ode_bc(ode, 0, np.pi, 1.5, 0, 10)
        plt.plot(x, y)
        plt.show()
        # print value at x = 2.8274
        print(x[9], y[9])

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Repeat the analysis with 100 intervals and compare it with the
        previous results."""

        def ode(x: float) -> tuple:
            return 2 * x, 2, np.cos(3 * x)

        x, y = ode_bc(ode, 0, np.pi, 1.5, 0, 100)
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
