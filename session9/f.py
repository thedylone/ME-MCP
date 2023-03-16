"""Determinant of a matrix"""

import numpy as np
from helpers.task import TaskBase, task_to_list


class TaskOld(TaskBase):
    """Determinant of a matrix"""

    tasklist: list = []

    @staticmethod
    def minor(
        matrix: list[list[float | int]], i: int, j: int
    ) -> list[list[float | int]]:
        """Returns the minor of a matrix, after removing row i and column j."""
        return [
            row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])
        ]

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[float | int]]]:
        """Write a function Minor, that receives a matrix A of dimension N x N
        and two indices i and j.
        The function returns a matrix, of dimension (N-1) x (N-1),
        obtained by matrix A, after removing row i and column j."""
        matrix_a: list[list[float | int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return {"Minor of A": self.minor(matrix_a, 1, 1)}

    @staticmethod
    def determinant(matrix: list[list[float | int]]) -> float | int:
        """Returns the determinant of a matrix."""
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return sum(
            (-1) ** j
            * matrix[0][j]
            * TaskOld.determinant(TaskOld.minor(matrix, 0, j))
            for j in range(len(matrix))
        )

    @task_to_list(tasklist)
    def task2(self) -> dict[str, float | int]:
        """Write a recursive function Determinant, that receives a matrix A and
        returns the value of its determinant"""
        matrix_a: list[list[float | int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return {"Determinant of A": self.determinant(matrix_a)}


class Task(TaskBase):
    """Determinant of a matrix"""

    tasklist: list = []

    @staticmethod
    def minor(matrix: np.ndarray, i: int, j: int) -> np.ndarray:
        """Returns the minor of a matrix, after removing row i and column j."""
        return np.delete(np.delete(matrix, i, 0), j, 1)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Write a function Minor, that receives a matrix A of dimension N x N
        and two indices i and j.
        The function returns a matrix, of dimension (N-1) x (N-1),
        obtained by matrix A, after removing row i and column j."""
        matrix_a: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        return {"Minor of A": self.minor(matrix_a, 1, 1)}

    @staticmethod
    def determinant(matrix: np.ndarray) -> float | int:
        """Returns the determinant of a matrix."""
        # already an inbuilt function in numpy
        # return np.linalg.det(matrix)
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return sum(
            (-1) ** j
            * matrix[0][j]
            * Task.determinant(Task.minor(matrix, 0, j))
            for j in range(len(matrix))
        )

    @task_to_list(tasklist)
    def task2(self) -> dict[str, float | int]:
        """Write a recursive function Determinant, that receives a matrix A and
        returns the value of its determinant"""
        matrix_a: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        return {"Determinant of A": self.determinant(matrix_a)}


if __name__ == "__main__":
    task: Task = Task("F")
    task.run_tasks()
    print(
        task.determinant(
            np.array([[6, 1, 1, 4], [4, -2, 5, 2], [2, 8, 7, 1], [2, 1, 5, 3]])
        )
    )
