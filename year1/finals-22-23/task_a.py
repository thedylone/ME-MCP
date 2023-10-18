"""Task A"""

import os
import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


class Task(TaskBase):
    """Task A"""

    tasklist: list = []

    @staticmethod
    def series(limit: int) -> float:
        """Calculate the sries
        S = sum_{j=-N}^{N+2} ( 1/j! sum_{k=2, k even}^{10j} (-1)^j j^k/k!)"""
        return sum(
            (
                1
                / math.factorial(j)
                * sum(
                    (-1) ** j * j**k / math.factorial(k)
                    for k in range(2, 10 * j + 1, 2)
                )
                for j in range(0, limit + 3)
            )
        )

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Compute the sum S eight times, taking N as each digit of your CID.
        Plot the various values of S against the number of terms N."""
        cid = list(map(int, list(CID)))  # convert CID to list of ints
        s_vals: list[float] = [series(digit) for digit in cid]
        # plot S vs N
        # use a bar chart since CID values are discrete
        plt.bar(cid, s_vals)
        plt.xlabel("N")
        plt.ylabel("S")
        plt.title("S vs N")
        plt.show()


def series(limit: int) -> float:
    """Calculate the sries
    S = sum_{j=-N}^{N+2} ( 1/j! sum_{k=2, k even}^{10j} (-1)^j j^k/k!)"""
    return sum(
        (
            1
            / math.factorial(j)
            * sum(
                (-1) ** j * j**k / math.factorial(k)
                for k in range(2, 10 * j + 1, 2)
            )
            for j in range(0, limit + 3)
        )
    )
    # # equivalent to:
    # outer = 0
    # for j in range(0, limit + 2):
    # # note j starts from 0 (negative factorials)
    #     inner = 0
    #     for k in range(2, 10 * j + 1, 2):
    #     # sum up inner terms, use step 2 to only sum even numbers
    #         inner += (-1) ** j * j**k / math.factorial(k)
    #     outer += 1 / math.factorial(j) * inner
    # return outer


def main() -> None:
    """Compute the sum S eight times, taking N as each digit of your CID.
    Plot the various values of S against the number of terms N."""
    s_vals: list[float] = []
    cid = list(map(int, list(CID)))  # convert CID to list of ints
    for digit in cid:
        s_vals.append(series(digit))  # compute S for each digit

    # plot S vs N
    # use a bar chart since CID values are discrete
    plt.bar(cid, s_vals)
    plt.xlabel("N")
    plt.ylabel("S")
    plt.title("S vs N")
    plt.show()


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
