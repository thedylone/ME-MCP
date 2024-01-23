"""Lagrangian polynomials and interpolation"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def lagrangian(j: int, xp: float, xn: list[float] | np.ndarray) -> float:
    """Write a function, Lagrangian, to compute the Lagrangian polynomial
    j at a point xp, with given nodes xn.
    The function receives the values j, xp and the array of nodes xn, and
    returns the value:
    Lj(xp) = product_{k=0, k!=j}^n (xp - xk) / (xj - xk)"""
    out = 1
    for k, xk in enumerate(xn):
        if k != j:
            out *= (xp - xk) / (xn[j] - xk)

    return out


def lagr_interp(
    xn: list[float] | np.ndarray,
    yn: list[float] | np.ndarray,
    x: list[float] | np.ndarray,
) -> list[float]:
    """Write a function, LagrInterp, that receives the sets of know values,
    xn and yn, the points to be interpolated x, and returns the
    interpolated values y, by using Lagrangian polynomials."""
    out = []
    for xp in x:
        y = 0
        for j in range(len(xn)):
            y += yn[j] * lagrangian(j, xp, xn)
        out.append(y)
    return out


class Task(TaskBase):
    """Lagrangian polynomials and interpolation"""

    tasklist: list = []

    p1: list[float] = []
    p2: list[float] = []
    p3: list[float] = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function, Lagrangian, to compute the Lagrangian polynomial
        j at a point xp, with given nodes xn.
        The function receives the values j, xp and the array of nodes xn, and
        returns the value:
        Lj(xp) = product_{k=0, k!=j}^n (xp - xk) / (xj - xk)"""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Write a function, LagrInterp, that receives the sets of know values,
        xn and yn, the points to be interpolated x, and returns the
        interpolated values y, by using Lagrangian polynomials."""

    def calculate_polynomials(self) -> None:
        """intermediate step to calculate polynomials for task 3"""
        x = np.linspace(0, 3, 61)

        # p1(x)
        xn = np.linspace(1, 2, 2)
        yn = np.sin(xn)
        self.p1 = lagr_interp(xn, yn, x)

        # p2(x)
        xn = np.linspace(1, 2, 3)
        yn = np.sin(xn)
        self.p2 = lagr_interp(xn, yn, x)

        # p3(x)
        xn = np.linspace(1, 2, 4)
        yn = np.sin(xn)
        self.p3 = lagr_interp(xn, yn, x)

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Test the two functions above with f(x) = sin (x) over the range
        x = [0:3] with step 0.05, given the nodal values at:
        a) xn = [1:2] with 2 nodes: linear interpolation p1(x)
        b) xn = [1:2] with 3 nodes: quadratic interpolation p2(x)
        c) xn = [1:2] with 4 nodes: cubic interpolation p3(x)

        Compare/plot the interpolating polynomials, p1(x) p2(x) p3(x)
        with/against those calculated manually in slides 106, 107 and 109,
        respectively. (You should end up with a plot like in slide 50)."""
        x = np.linspace(0, 3, 61)

        # p1(x)
        p1_manual = 0.0678 * x + 0.7737
        plt.plot(x, self.p1, label="p1(x)")
        plt.plot(x, p1_manual, label="p1_manual(x)")
        plt.title("p1(x)")
        plt.legend()
        plt.show()

        # p2(x)
        p2_manual = -0.4884 * x**2 + 1.533 * x - 0.2032
        plt.plot(x, self.p2, label="p2(x)")
        plt.plot(x, p2_manual, label="p2_manual(x)")
        plt.title("p2(x)")
        plt.legend()
        plt.show()

        # p3(x)
        p3_manual = -0.01163 * x**3 - 0.4350 * x**2 + 1.454 * x - 0.1661
        plt.plot(x, self.p3, label="p3(x)")
        plt.plot(x, p3_manual, label="p3_manual(x)")
        plt.title("p3(x)")
        plt.legend()
        plt.show()

        plt.plot(x, self.p1, label="p1(x)")
        plt.plot(x, self.p2, label="p2(x)")
        plt.plot(x, self.p3, label="p3(x)")
        plt.plot(x, np.sin(x), label="sin(x)")
        plt.title("p1(x), p2(x), p3(x)")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task4(self) -> dict[str, list[float]]:
        """Error analysis: compute the basic error (as defined in slide 119)
        for p1(x), p2(x), ..., p13(x), p14(x) at x = pi/2 (slide 121)."""
        prev_p: float = 0
        errors: list[float] = []
        for j in range(1, 15):
            xn = np.linspace(1, 2, j + 1)
            yn = np.sin(xn)
            p = lagr_interp(xn, yn, [np.pi / 2])[0]
            if j > 1:
                errors.append(p - prev_p)
            prev_p = p
        return {"errors": errors}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    # cubic interpolation at x = 1.1
    print(task.p3[22])
