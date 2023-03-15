"""Matrix-matrix multiplication"""

import numpy as np
from helpers.task import TaskBase, task_to_list
from session9.d import Task as TaskD, TaskOld as TaskDOld


class TaskOld(TaskBase):
    """Matrix-matrix multiplication"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_p: list[list[float | int]]

    @staticmethod
    def matmat(
        matrix_1: list[list[float | int]], matrix_2: list[list[float | int]]
    ) -> list[list[float | int]]:
        """Multiply two matrices. Return 0 if the sizes are incompatible."""
        if len(matrix_1[0]) != len(matrix_2):
            return [[0]]
        return [
            [
                sum(a * b for a, b in zip(row_A, col_B))
                for col_B in zip(*matrix_2)
            ]
            for row_A in matrix_1
        ]

    @task_to_list(tasklist)
    def task1(self) -> dict[str, bool]:
        """Write a function, MatMat, that receives two matrices, A and B,
        and returns the product of the two matrices, P = AB. The function
        should return the value 0 if the sizes of the two matrices are
        incompatible for the multiplication.
        Verify that A * B != B * A"""
        task_d: TaskDOld = TaskDOld("D", False)
        task_d.task1()
        matrix_a: list[list[float | int]] = task_d.matrix_a
        matrix_b: list[list[float | int]] = task_d.matrix_b
        self.matrix_p = self.matmat(matrix_a, matrix_b)
        return {
            "A * B == B * A": self.matmat(matrix_a, matrix_b)
            == self.matmat(matrix_b, matrix_a)
        }


class Task(TaskBase):
    """Matrix-matrix multiplication"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_p: np.ndarray

    @staticmethod
    def matmat(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
        """Multiply two matrices. Return 0 if the sizes are incompatible."""
        if len(matrix_a[0]) != len(matrix_b):
            return np.zeros((1, 1))
        # already an inbuilt operator in python and numpy
        return matrix_a @ matrix_b

    @task_to_list(tasklist)
    def task1(self) -> dict[str, bool]:
        """Write a function, MatMat, that receives two matrices, A and B,
        and returns the product of the two matrices, P = AB. The function
        should return the value 0 if the sizes of the two matrices are
        incompatible for the multiplication.
        Verify that A * B != B * A"""
        task_d: TaskD = TaskD("D", False)
        task_d.task1()
        matrix_a: np.ndarray = task_d.matrix_a
        matrix_b: np.ndarray = task_d.matrix_b
        self.matrix_p = self.matmat(matrix_a, matrix_b)
        return {
            "A * B == B * A": np.array_equal(
                matrix_a @ matrix_b, matrix_b @ matrix_a
            )
        }


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
    print(task.matrix_p[22][22])
