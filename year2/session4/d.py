"""Gauss integration"""

from helpers.task import TaskBase, task_to_list
from year2.session4.Gauss import tg, wg


class Task(TaskBase):
    """Gauss integration. The Gauss-Legendre Quadrature nodes and weights are
    coded in file Gauss.py, into the two array variables tg and wg, for
    nodes n = 1, 2, 3, 4, 5.
    """

    tasklist: list = []

    @staticmethod
    def f(x: float) -> float:
        """Function to integrate"""
        return 1 / (1 + x**2)

    @task_to_list(tasklist)
    def task1(self):
        """Write a script to integrate a function f(x) with Gauss quadrature.
        Compute the integral:
        int_0^1 1/(1+x^2) dx"""
        n = 5
        a = 0
        b = 1

        return {
            "integral": (
                (b - a)
                / 2
                * sum(
                    wg[n - 1][j]
                    * self.f(
                        (a * (1 - tg[n - 1][j]) + b * (1 + tg[n - 1][j])) / 2
                    )
                    for j in range(n)
                )
            )
        }


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
