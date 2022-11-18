"""Consolidating Counted Loops"""

import random

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Consolidating Counted Loops"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Write a script to find out the sum: S = sum_{n=1}^{N} n^2"""
        upper = TaskBase.int_input("upper bound")
        total = sum(num * num for num in range(1, upper + 1))
        return {"total": total}

    @task_to_list(tasklist)
    def task2(self):
        """Write a script to throw N times a dice
        and compute the overall score."""
        times = TaskBase.int_input("number of times")
        total = sum(random.randint(1, 6) for _ in range(times))
        return {"total": total}

    @task_to_list(tasklist)
    def task3(self):
        """Write a script to compute the factorial of an integer number."""
        number = TaskBase.int_input("number")
        if number < 0:
            raise ValueError("Number must be positive.")
        total = 1
        for num in range(2, number + 1):
            total *= num
        return {"total": total}


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
