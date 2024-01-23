"""Splines"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def splines(
    xn: list[float] | np.ndarray,
    yn: list[float] | np.ndarray,
    x: list[float] | np.ndarray,
    grad_a: float,
    grad_b: float,
) -> list[float]:
    """Write a function, Splines, that receives the sets of know values,
    xn and yn, the points to be interpolated x, the clamped boundary
    conditions y'(a), y'(b), and returns the interpolated values y,
    by using cubic splines"""
    n = len(xn)
    h = np.diff(xn)
    # create matrix for gradients
    a = np.zeros((n, n))
    d = np.zeros(n)
    a[0, 0] = 1
    a[-1, -1] = 1
    d[0] = grad_a
    d[-1] = grad_b
    for j in range(1, n - 1):
        a[j, j - 1] = 1 / h[j - 1]
        a[j, j] = 2 * (1 / h[j - 1] + 1 / h[j])
        a[j, j + 1] = 1 / h[j]
        left = (yn[j] - yn[j - 1]) / (h[j - 1] ** 2)
        right = (yn[j + 1] - yn[j]) / (h[j] ** 2)
        d[j] = 3 * (left + right)
    # solve system
    v = np.linalg.solve(a, d)
    # create matrix for coefficients
    c = np.zeros((n - 1, 4))
    for j in range(n - 1):
        dy = yn[j + 1] - yn[j]
        c[j, 0] = yn[j]
        c[j, 1] = v[j]
        c[j, 2] = 3 * dy / h[j] ** 2 - (v[j + 1] + 2 * v[j]) / h[j]
        c[j, 3] = -2 * dy / h[j] ** 3 + (v[j + 1] + v[j]) / h[j] ** 2

    # interpolate
    out = []
    for xp in x:
        for j in range(n - 1):
            if xn[j] <= xp <= xn[j + 1]:
                dx = xp - xn[j]
                out.append(
                    c[j, 0]
                    + c[j, 1] * dx
                    + c[j, 2] * dx**2
                    + c[j, 3] * dx**3
                )
                break
    return out


class Task(TaskBase):
    """Splines"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function, Splines, that receives the sets of know values,
        xn and yn, the points to be interpolated x, the clamped boundary
        conditions y'(a), y'(b), and returns the interpolated values y,
        by using cubic splines"""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Test the function above with:
        f(x) = 1 / (1 + 25 * x**2)
        with a = -1, b = 1, y'(a) = 0.074, y'(b) = -0.074, by using 3, 5 and
        11 nodes"""
        nodes = [3, 5, 11]
        grad_a = 0.074
        grad_b = -0.074
        x = np.linspace(-1, 1, 201)
        for n in nodes:
            xn = np.linspace(-1, 1, n)
            yn = 1 / (1 + 25 * xn**2)
            y = splines(xn, yn, x, grad_a, grad_b)
            plt.plot(x, y, label=f"{n} nodes")
        plt.plot(x, 1 / (1 + 25 * x**2), label="f(x)")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
    # interpolated x = 0.8 with nodes = 7
    quiz_xn = np.linspace(-1, 1, 7)
    quiz_yn = 1 / (1 + 25 * quiz_xn**2)
    print(splines(quiz_xn, quiz_yn, [0.8], 0.074, -0.074))
