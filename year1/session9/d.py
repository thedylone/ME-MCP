"""Sum of two matrices"""

import numpy as np
from helpers.task import TaskBase, task_to_list
from year1.session9.c import TaskOld as TaskCOld


class TaskOld(TaskBase):
    """Sum of two matrices"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_a: list[list[float | int]]
        self.matrix_b: list[list[float | int]]
        self.matrix_c: list[list[float | int]]

    def import_matrix(
        self, path: str, rows: int, cols: int
    ) -> list[list[float | int]]:
        """Import a matrix from a file."""
        with open(path, "r", encoding="utf-8") as file:
            matrix: list[list[float | int]] = [
                [int(file.readline()) for _ in range(cols)]
                for _ in range(rows)
            ]
        return matrix

    @task_to_list(tasklist)
    def task1(self) -> None:
        """The files MatA.txt and MatB.txt contain the values of two matrices,
        A and B, of size 60x60. Entries of the matrices are stored in the file
        one value per line, sequentially as they appear in the matrix. Read in
        the numerical values from the two files and form the two matrices
        A and B accordingly."""
        self.matrix_a = self.import_matrix("year1/session9/MatA.txt", 60, 60)
        self.matrix_b = self.import_matrix("year1/session9/MatB.txt", 60, 60)

    @staticmethod
    def matsum(
        matrix_a: list[list[float | int]], matrix_b: list[list[float | int]]
    ) -> list[list[float | int]]:
        """Sum of two matrices."""
        if len(matrix_a) != len(matrix_b):
            raise ValueError("Matrices must have the same number of rows")
        if len(matrix_a[0]) != len(matrix_b[0]):
            raise ValueError("Matrices must have the same number of columns")
        return [
            [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
            for i in range(len(matrix_a))
        ]

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[list[float | int]]]:
        """Write a function MatSum, that receives two matrices, A and B,
        and returns the sum of them"""
        self.matrix_c = self.matsum(self.matrix_a, self.matrix_b)
        return {"A + B": self.matrix_c}

    @staticmethod
    def scalar_mult(
        scalar: float | int, matrix: list[list[float | int]]
    ) -> list[list[float]]:
        """Multiply a matrix by a scalar."""
        return [[scalar * val for val in row] for row in matrix]

    @task_to_list(tasklist)
    def task3(self) -> dict[str, bool]:
        """Compute the matrix D = 0.5(A + A^T) + 0.5(A - A^T)
        and verify that D is the same as A"""
        matrix_d: list[list[float | int]] = self.matsum(
            self.scalar_mult(
                0.5,
                self.matsum(self.matrix_a, TaskCOld.transpose(self.matrix_a)),
            ),
            self.scalar_mult(
                0.5,
                self.matsum(
                    self.matrix_a,
                    self.scalar_mult(-1, TaskCOld.transpose(self.matrix_a)),
                ),
            ),
        )
        return {"D == A": matrix_d == self.matrix_a}


class Task(TaskBase):
    """Sum of two matrices"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_a: np.ndarray
        self.matrix_b: np.ndarray
        self.matrix_c: np.ndarray

    @staticmethod
    def import_matrix(path, rows, cols) -> np.ndarray:
        """Import a matrix from a file."""
        with open(path, "r", encoding="utf-8") as file:
            matrix: list[list[int]] = [
                [int(file.readline()) for _ in range(cols)]
                for _ in range(rows)
            ]
        return np.array(matrix)

    @task_to_list(tasklist)
    def task1(self) -> None:
        """The files MatA.txt and MatB.txt contain the values of two matrices,
        A and B, of size 60x60. Entries of the matrices are stored in the file
        one value per line, sequentially as they appear in the matrix. Read in
        the numerical values from the two files and form the two matrices
        A and B accordingly."""
        self.matrix_a = self.import_matrix("year1/session9/MatA.txt", 60, 60)
        self.matrix_b = self.import_matrix("year1/session9/MatB.txt", 60, 60)

    @staticmethod
    def matsum(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
        """Sum of two matrices."""
        if len(matrix_a) != len(matrix_b):
            raise ValueError("Matrices must have the same number of rows")
        if len(matrix_a[0]) != len(matrix_b[0]):
            raise ValueError("Matrices must have the same number of columns")
        # already an inbuilt operation in numpy
        return matrix_a + matrix_b

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Write a function MatSum, that receives two matrices, A and B,
        and returns the sum of them"""
        self.matrix_c = self.matsum(self.matrix_a, self.matrix_b)
        return {"A + B": self.matrix_c}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, bool]:
        """Compute the matrix D = 0.5(A + A^T) + 0.5(A - A^T)
        and verify that D is the same as A"""
        matrix_d: np.ndarray = 0.5 * (
            self.matrix_a + self.matrix_a.T
        ) + 0.5 * (self.matrix_a - self.matrix_a.T)
        return {"D == A": np.array_equal(matrix_d, self.matrix_a)}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    print(task.matrix_a[3][4])
    print(task.matrix_c[10][34])
