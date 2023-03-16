"""Series expansion"""

import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from session5.a import Task as TaskA


class Task(TaskBase):
    """Series expansion"""

    tasklist: list = []

    @staticmethod
    def exp_series(x_values, N) -> list[float]:
        """Approximate e^x by the series expansion sum_{i=0}^{N} x^i/i!
        in the range x = [a:b]"""
        y_values: list[float] = [
            sum(x**i / TaskA.factorial(i) for i in range(N + 1))
            for x in x_values
        ]
        return y_values

    @task_to_list(tasklist)
    def task1(self) -> None:
        """write a script to plot y(x) in the range x = [-4:2] with points
        at intervals of 0.01, with N = 2, 6, 10, 14."""
        x_values: list[float] = [x / 100 for x in range(-400, 201)]
        n_values: list[int] = [2, 6, 10, 14]
        y_values: list[list[float]] = [
            self.exp_series(x_values, N) for N in n_values
        ]
        for y in y_values:
            plt.plot(x_values, y)
        plt.legend([f"N = {N}" for N in n_values])
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
    print(Task.exp_series([2.5], 18))
