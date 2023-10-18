"""Task A"""

import os
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02345678")


def transpose(matrix: list[list]) -> list[list]:
    """Returns the transpose of the matrix"""
    return list(map(list, zip(*matrix)))


class Task(TaskBase):
    """Task A"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Write a script to compute the array c: c = (A - A.T) . b
        Matrix A has dimensions 8 x 8 and of the form below, where the two
        diagonals are made out of your College CID. A.T is the transpose of A.
        The array b has dimensions 8 x 1 and is made out of your CID."""

        mat_a: list[list[int]] = [[0] * 8 for _ in range(8)]
        for i in range(8):
            mat_a[i][i] = int(CID[i])
            mat_a[i][7 - i] = int(CID[i])
        mat_b: list[list[int]] = [[int(i)] for i in CID]
        mat_c: list[int] = [
            sum(mat_b[j][0] * (mat_a[i][j] - mat_a[j][i]) for j in range(8))
            for i in range(8)
        ]
        return {"c": mat_c}


if __name__ == "__main__":
    print("CID:", CID)
    task: Task = Task("A")
    task.run_tasks()
    CID = "01302327"
    assert task.task1()["c"] == [-49, -2, 0, -4, 0, 0, 1, 0]
