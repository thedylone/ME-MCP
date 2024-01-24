"""Types of boundary conditions"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def ode_bc(
    ode: Callable,
    a: float,
    b: float,
    y_a: float,
    y_b: float,
    N: int,
    R: np.ndarray,
) -> tuple:
    """Modify the function, myodebc, to accommodate all the various types
    of boundary conditions. myodebc still receives the boundaries of the
    domain a and b, the boundary conditions at these points BC_a and BC_b,
    and the number N of desired intervals. In addition, it receives an
    array R of length 4, with the values of r0, r1, r2, r3, specifying
    the type of boundary conditions."""
    x: np.ndarray
    x, _h = np.linspace(a, b, N + 1, retstep=True)
    h = float(_h)
    A = np.zeros((N + 1, N + 1))
    B = np.zeros(N + 1)
    # r0 dy/dx (a) + r1 y(a) = y_a
    # r2 dy/dx (b) + r3 y(b) = y_b
    A[0, 0] = -R[0] / h + R[1]
    A[0, 1] = R[0] / h
    A[N, N - 1] = -R[2] / h
    A[N, N] = R[2] / h + R[3]
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
    """Types of boundary conditions
    The boundary conditions, specified at the two boundaries a and b, can be
    of different types
    """

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Modify the function, myodebc, to accommodate all the various types
        of boundary conditions. myodebc still receives the boundaries of the
        domain a and b, the boundary conditions at these points BC_a and BC_b,
        and the number N of desired intervals. In addition, it receives an
        array R of length 4, with the values of r0, r1, r2, r3, specifying
        the type of boundary conditions."""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Solve the ODE d^2y/dx^2 + x dy/dx + y = 5x, in the domain [0, 2],
        with boundary conditions dy/dx (0) = 0 and y(2) = 5. Discretise the
        domain with 50 intervals. Plot y(x)."""

        def ode(x: float) -> tuple:
            return x, 1, 5 * x

        x, y = ode_bc(ode, 0, 2, 0, 5, 50, np.array([1, 0, 0, 1]))
        plt.plot(x, y)
        plt.show()
        # print value at x = 0.64
        print(x[16], y[16])

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Repeat the calculation with the boundary conditions y(0) = 5 and
        dy/dx (2) = 0."""

        def ode(x: float) -> tuple:
            return x, 1, 5 * x

        x, y = ode_bc(ode, 0, 2, 5, 0, 50, np.array([0, 1, 1, 0]))
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
