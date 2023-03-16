"""Consolidating Counted Loops"""

import random
from helpers.task import RangeValidator, TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Consolidating Counted Loops"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, int]:
        """Write a script to find out the sum: S = sum_{n=1}^{N} n^2"""
        upper: int = get_input(int, "upper bound")
        total: int = sum(num * num for num in range(1, upper + 1))
        return {"total": total}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int]:
        """Write a script to throw N times a dice
        and compute the overall score."""
        times: int = get_input(int, "number of times")
        total: int = sum(random.randint(1, 6) for _ in range(times))
        return {"total": total}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, int]:
        """Write a script to compute the factorial of an integer number."""
        number: int = get_input(int, "number", RangeValidator(0))
        total: int = 1
        for num in range(2, number + 1):
            total *= num
        return {"total": total}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
