"""Task D"""

import os
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02345678")


class Task(TaskBase):
    """Task D"""

    tasklist: list = []

    @staticmethod
    def exp_seq(num: int) -> int:
        """Recursive function to calculate the sequence:
        y_n = (10 - a) ^ n
        for any n > 0, where a is the 4th digit of your CID."""
        if num == 0:
            return 1
        return (10 - int(CID[3])) * Task.exp_seq(num - 1)

    @task_to_list(tasklist)
    def task1(self) -> dict:
        """Write a RECURSIVE function, ExpSeq(), to calculate the sequence:
        y_n = (10 - a) ^ n
        for any n > 0, where a is the 4th digit of your CID.
        The function receives the value of n only
        and returns the value of y_n only.
        Print the first 10 values of the sequence."""
        return {"first 10 values": [self.exp_seq(i) for i in range(1, 11)]}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    CID = "02345678"
    assert Task.exp_seq(10) == 60466176
