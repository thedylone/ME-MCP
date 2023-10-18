"""Task D"""

import os
import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

CID: list[int] = list(map(int, list(os.environ.get("CID", "02345678"))))


class Task(TaskBase):
    """Task D"""

    tasklist: list = []

    @staticmethod
    def series(num: int) -> float:
        """Calculate the sum:
        P = sum_{i=1}^N (1/(i-1)! sum_{k=1}^i (a+10)^(k-3))
        where a = 4th digit of your CID."""
        return sum(
            1
            / math.factorial(i - 1)
            * sum((CID[3] + 10) ** (k - 3) for k in range(1, i + 1))
            for i in range(1, num + 1)
        )

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function Series(N) to calculate the sum:
        P = sum_{i=1}^N (1/(i-1)! sum_{k=1}^i (a+10)^(k-3))
        where a = 4th digit of your CID.
        Call the function for all the values N = 1,2, ... . .50
        and plot a graph of P vs N."""
        p_vals: list[float] = [self.series(i) for i in range(1, 51)]
        plt.plot(p_vals)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    CID = [0, 1, 8, 5, 6, 6, 6, 6]
    assert Task.series(10) == 1087.3935673255928
