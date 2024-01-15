"""K-th order derivative"""

import numpy as np

from helpers.task import TaskBase, task_to_list


def factorial(n: int) -> int:
    """Factorial"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


def choose(n: int, k: int) -> int:
    """Binomial"""
    return factorial(n) // (factorial(k) * factorial(n - k))


class Task(TaskBase):
    """K-th order derivative"""

    tasklist: list = []

    @staticmethod
    def derivative_fwd(
        k: int, h: float, yn: list[float] | np.ndarray
    ) -> list[float] | np.ndarray:
        """k-th order derivative using forward method"""
        nodes = len(yn) - k
        dx = np.ndarray(nodes)
        for n in range(nodes):
            dx[n] = sum(
                (-1) ** i * choose(k, i) * yn[n + k - i] for i in range(k + 1)
            )
        return dx / h**k

    @staticmethod
    def derivative_bwd(k: int, h: float, yn: list[float] | np.ndarray):
        """k-th order derivate using backward method"""
        nodes = len(yn) - k
        dx = np.ndarray(nodes)
        for n in range(k, len(yn)):
            dx[n] = sum(
                (-1) ** i * choose(k, 1) * yn[n - i] for i in range(k + 1)
            )
        return dx / h**k

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[float] | np.ndarray]:
        """Write a function, Derivative, to compute the k-th order derivative
        for a given set of uniformly distributed nodal points (choose yourself
        to apply either the forward or backward scheme)."""
        # test with f(x) = sin(x)
        h = 0.01
        x = np.arange(0, 1 + h, h)
        y = np.sin(x)
        k = 2
        dy = self.derivative_fwd(k, h, y)
        return {"dy": dy, "real": -y[:-k]}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
