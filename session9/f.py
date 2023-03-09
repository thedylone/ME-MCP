"""Determinant of a matrix"""

import numpy as np
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Determinant of a matrix"""

    tasklist = []

    @staticmethod
    def minor(matrix, i, j):
        """Returns the minor of a matrix, after removing row i and column j."""
        return [
            row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])
        ]

    @task_to_list(tasklist)
    def task1(self):
        """Write a function Minor, that receives a matrix A of dimension N x N
        and two indices i and j.
        The function returns a matrix, of dimension (N-1) x (N-1),
        obtained by matrix A, after removing row i and column j."""
        matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return {"Minor of A": self.minor(matrix_A, 1, 1)}

    @staticmethod
    def determinant(matrix):
        """Returns the determinant of a matrix."""
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
    def task2(self):
        """Write a recursive function Determinant, that receives a matrix A and
        returns the value of its determinant"""
        matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return {"Determinant of A": self.determinant(matrix_A)}


if __name__ == "__main__":
    task = Task("F")
    task.run_tasks()
    print(
        task.determinant(
            [[6, 1, 1, 4], [4, -2, 5, 2], [2, 8, 7, 1], [2, 1, 5, 3]]
        )
    )
