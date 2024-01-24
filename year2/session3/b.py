"""Newton interpolation"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session3.a import Task as LagrTask


def newt_div_diff(
    xn: list[float] | np.ndarray, yn: list[float] | np.ndarray
) -> float:
    """Write a recursive function, NewtDivDiff, to compute the value of
    the Newton's Divided Difference f[x0, x1, x2, ..., xn], as defined in
    slide 124. The function receives the two lists of nodal points xn and
    yn and returns the corresponding scalar value."""
    if len(xn) == 1:
        return yn[0]
    left: float = newt_div_diff(xn[:-1], yn[:-1])
    right: float = newt_div_diff(xn[1:], yn[1:])
    return (left - right) / (xn[0] - xn[-1])


def newton_interp(
    xn: list[float] | np.ndarray,
    yn: list[float] | np.ndarray,
    x: list[float] | np.ndarray,
) -> list[float]:
    """Write a function, NewtonInterp, that receives the sets of know
    values, xn and yn, the points to be interpolated x, and returns the
    interpolated values y, by using Newton's Divided Difference."""
    out: list[float] = []
    n: int = len(xn)
    for xp in x:
        y: float = yn[0]
        for i in range(1, n):
            prod = 1
            for j in range(i):
                prod *= xp - xn[j]
            y += newt_div_diff(xn[: i + 1], yn[: i + 1]) * prod
        out.append(y)
    return out


class Task(TaskBase):
    """Newton interpolation"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.lagr_task = LagrTask("A", False)
        self.lagr_task.calculate_polynomials()

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a recursive function, NewtDivDiff, to compute the value of
        the Newton's Divided Difference f[x0, x1, x2, ..., xn], as defined in
        slide 124. The function receives the two lists of nodal points xn and
        yn and returns the corresponding scalar value."""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Write a function, NewtonInterp, that receives the sets of know
        values, xn and yn, the points to be interpolated x, and returns the
        interpolated values y, by using Newton's Divided Difference."""

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Test the two functions above with f(x) = sin (x) over the range
        [0, 3] with step 0.05, given the nodal values at:
        a) xn = [1:2] with 2 nodes: linear interpolation p1(x)
        b) xn = [1:3] with 3 nodes: quadratic interpolation p2(x)
        c) xn = [1:4] with 4 nodes: cubic interpolation p3(x)

        Compare/plot the interpolating polynomials, p1(x) p2(x) p3(x)
        with/against those calculated with Lagrangian inerpolation."""
        x = np.linspace(0, 3, 61)

        # p1(x)
        xn = np.linspace(1, 2, 2)
        yn = np.sin(xn)
        p1 = newton_interp(xn, yn, x)
        plt.plot(x, p1, label="newton")
        plt.plot(x, self.lagr_task.p1, label="lagrangian")
        plt.title("p1(x)")
        plt.legend()
        plt.show()

        # p2(x)
        xn = np.linspace(1, 2, 3)
        yn = np.sin(xn)
        p2 = newton_interp(xn, yn, x)
        plt.plot(x, p2, label="newton")
        plt.plot(x, self.lagr_task.p2, label="lagrangian")
        plt.title("p2(x)")
        plt.legend()
        plt.show()

        # p3(x)
        xn = np.linspace(1, 2, 4)
        yn = np.sin(xn)
        p3 = newton_interp(xn, yn, x)
        plt.plot(x, p3, label="newton")
        plt.plot(x, self.lagr_task.p3, label="lagrangian")
        plt.title("p3(x)")
        plt.legend()
        plt.show()

        plt.plot(x, p1, label="p1(x)")
        plt.plot(x, p2, label="p2(x)")
        plt.plot(x, p3, label="p3(x)")
        plt.plot(x, np.sin(x), label="sin(x)")
        plt.title("p1(x), p2(x), p3(x)")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task4(self) -> None:
        """Interpolate the function (slide 138):
        f(x) = 1 / (1 + 25 * x**2)
        in the range -1 <= x <= 1, with Newton's interpolation of order
        n = 1, 2, 3, 4, 5 ... 14 and plot the interpolating polynomials.
        (Runge's phenomenon)"""
        x = np.linspace(-1, 1, 41)
        for n in range(1, 14):
            xn = np.linspace(-1, 1, n + 1)
            yn = 1 / (1 + 25 * xn**2)
            p = newton_interp(xn, yn, x)
            plt.plot(x, p, label=f"p{n}(x)")
        plt.plot(x, 1 / (1 + 25 * x**2), label="f(x)")
        plt.title("Runge's phenomenon")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
    # task 4 interpolated value at x = 0.8 with n = 9
    quiz_xn = np.linspace(-1, 1, 10)
    quiz_yn = 1 / (1 + 25 * quiz_xn**2)
    quiz_p = newton_interp(quiz_xn, quiz_yn, [0.8])
    print(quiz_p)
