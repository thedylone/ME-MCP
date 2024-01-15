"""Trapezium rule for functions with equidistant nodes"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Trapezium rule for functions with equidistant nodes"""

    tasklist: list = []

    @staticmethod
    def trapzeqd(x: np.ndarray, y: np.ndarray) -> float:
        """Trapezium integration"""
        return sum(
            (x[i + 1] - x[i]) * (y[i + 1] + y[i]) / 2
            for i in range(len(x) - 1)
        )

    @staticmethod
    def func(x: np.ndarray) -> np.ndarray:
        """Function to integrate"""
        return 1 / (x**17.10 + 2023) ** 0.5

    @staticmethod
    def get_x(b: float, n: int) -> np.ndarray:
        """Get x values"""
        return np.linspace(0, b, n)

    @staticmethod
    def integrate(b: float, n: int) -> float:
        """Integrate with custom number of nodes"""
        x: np.ndarray = np.linspace(0, b, n)
        return Task.trapzeqd(x, Task.func(x))

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Write a Python function, trapzeqd, receiving a set of points
        x and y, and outputting the numerical integral of y within
        the interval specified by x. Assume that the nodes x are equidistant.
        Test the Python function by integrating:
        I = int_0^b 1/sqrt(x^17.10 + 2023) dx
        in the interval x = [0:b=2] with 5 nodes and then with 11 nodes."""
        b: float = 2
        int_5nodes: float = self.integrate(b, 5)
        int_11nodes: float = self.integrate(b, 11)
        return {"int_5nodes": int_5nodes, "int_11nodes": int_11nodes}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[float]]:
        """Increase the interval of integration with b = 10, 100, 1000, 10000
        and recompute the integral with the same number of nodes (5).
        Plot the values of I vs b."""
        limits: list[int] = [10, 100, 1000, 10000]
        integral: list[float] = []
        for b in limits:
            int_val: float = self.integrate(b, 5)
            integral.append(int_val)
            plt.scatter(b, int_val)
        plt.xlabel("b")
        plt.ylabel("I")
        plt.show()
        return {"integral": integral}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, list[float]]:
        """Repeat the numerical integration for the intervals in Part 2, but
        retaining the same interval h = 0.5, i.e. by increasing progressively
        the number of nodes.
        Replot the values of I vs b."""
        limits: list[int] = [10, 100, 1000, 10000]
        integral: list[float] = []
        for b in limits:
            int_val: float = self.integrate(b, int(b // 0.5 + 1))
            integral.append(int_val)
            plt.scatter(b, int_val)
        plt.xlabel("b")
        plt.ylabel("I")
        plt.show()
        return {"integral": integral}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    print(task.integrate(2, 10))
