"""Task A"""

import os
import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02345678")


class Task(TaskBase):
    """Task A"""

    tasklist: list = []

    @staticmethod
    def series(num: int) -> float:
        """Calculate the mathematical series
        S = sum_{j=-N}^{N} (1/(100 - a^2)
        sum_{k=-j, k!=0}^{j-1} (-1)^j sin(ak)/k^a)"""
        var_a = int(CID[3])
        return sum(
            1
            / (100 - var_a**2)
            * sum(
                (-1) ** j * math.sin(var_a * k) / k**var_a
                for k in range(-j, j)
                if k != 0
            )
            for j in range(-num, num + 1)
        )

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function, Series(), to calculate the mathematical series
        S = sum_{j=-N}^{N} (1/(100 - a^2)
        sum_{k=-j, k!=0}^{j-1} (-1)^j sin(ak)/k^a)
        where a is the 4th digit of your CID.
        The function receives the value of N and returns the result S.
        Compute the sum S for integer values of N in the range [1...20].
        Plot the various values of S against the number of terms N.
        """
        s_vals: list[float] = [self.series(n) for n in range(1, 21)]
        plt.plot(range(1, 21), s_vals)
        plt.xlabel("N")
        plt.ylabel("S")
        plt.title("S vs N")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    CID = "02345678"
    assert Task.series(10) == -0.009788394388041466
