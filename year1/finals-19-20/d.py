"""Task D"""

import os
import math
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02345678")


class Task(TaskBase):
    """Task D"""

    tasklist: list = []

    @staticmethod
    def recursive(num) -> float:
        """Write a recursive function to calculate the sum S
        S = sum_{i=1}^{n} i^a / (i - 1)!
        where a = 6th digit of your CID
        Test the function by invoking it for N = 15"""
        if num == 1:
            return 1
        fact: int = math.factorial(num - 1)
        return num ** int(CID[5]) / fact + Task.recursive(num - 1)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Write a recursive function to calculate the sum S
        S = sum_{i=1}^{n} i^a / (i - 1)!
        where a = 6th digit of your CID
        Test the function by invoking it for N = 15"""
        return {"S": Task.recursive(15)}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    CID = "01302327"
    assert Task.recursive(15) == 40.774227423501046
