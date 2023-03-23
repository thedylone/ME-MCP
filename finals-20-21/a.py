"""Task A"""

import os
from helpers.task import TaskBase, task_to_list

CID: list[int] = list(map(int, list(os.environ.get("CID", "02345678"))))


def matmult(matrix_a, matrix_b):
    """Multiply two matrices. Return 0 if the sizes are incompatible."""
    if len(matrix_a[0]) != len(matrix_b):
        return [[0]]
    zip_b = list(zip(*matrix_b))
    return [
        [
            sum(val_a * val_b for val_a, val_b in zip(row_a, col_b))
            for col_b in zip_b
        ]
        for row_a in matrix_a
    ]


class Task(TaskBase):
    """Task A"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[int]]]:
        """Write a script to compute the array D
        D = (A + B) . (A - B)
        Matrix A and B have dimensions 8 x 8 and of the form below,
        with values made out of your College CID.
        First column of A is CID, last column is CID reversed.
        First row of B is CID, last row is CID reversed."""
        mat_a: list[list[int]] = [[0] * 8 for _ in range(8)]
        mat_b: list[list[int]] = [[0] * 8 for _ in range(8)]
        mat_d: list[list[int]] = [[0] * 8 for _ in range(8)]

        mat_b[0] = CID
        mat_b[-1] = CID[::-1]
        for i in range(8):
            mat_a[i][0] = CID[i]
            mat_a[i][-1] = CID[-i - 1]

        mat_d = matmult(
            [[mat_a[i][j] + mat_b[i][j] for j in range(8)] for i in range(8)],
            [[mat_a[i][j] - mat_b[i][j] for j in range(8)] for i in range(8)],
        )

        return {"D": mat_d}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    CID = [0, 1, 8, 5, 6, 6, 6, 6]
    assert task.task1()["D"] == [
        [198, -72, -72, -72, -60, -96, -12, 168],
        [0, -37, -44, -41, -36, -54, -12, 0],
        [0, -44, -100, -76, -78, -96, -54, 0],
        [0, -41, -76, -61, -60, -78, -36, 0],
        [0, -36, -78, -60, -61, -76, -41, 0],
        [0, -54, -96, -78, -76, -100, -44, 0],
        [0, -12, -54, -36, -41, -44, -37, 0],
        [168, -12, -96, -60, -72, -72, -72, 198],
    ]
