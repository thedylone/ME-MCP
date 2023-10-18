"""Task D"""

import os
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


class Task(TaskBase):
    """Task D"""

    tasklist: list = []

    @staticmethod
    def sequence(num: int) -> float:
        """Write a RECURSIVE function, Sequence(), to calculate the sequence:
        y1 = 0
        y2 = 1
        yn = yn-1 - (n+1) * yn-2"""
        if num == 1:
            return 0
        if num == 2:
            return 1
        return sequence(num - 1) - (num + 1) * sequence(num - 2)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[float]]:
        """Print the first 20 values of the sequence."""
        # starting from n = 1 to n = 20
        return {"sequence": [sequence(n) for n in range(1, 21)]}


def sequence(num: int) -> float:
    """Write a RECURSIVE function, Sequence(), to calculate the sequence:
    y1 = 0
    y2 = 1
    yn = yn-1 - (n+1) * yn-2"""
    if num == 1:
        return 0
    if num == 2:
        return 1
    return sequence(num - 1) - (num + 1) * sequence(num - 2)


def main() -> None:
    """Print the first 20 values of the sequence."""
    # starting from n = 1 to n = 20
    print(*[sequence(n) for n in range(1, 21)])


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    assert Task.sequence(20) == 4515086720
