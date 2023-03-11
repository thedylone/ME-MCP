"""Inverse of a matrix"""

import numpy as np
from helpers.task import TaskBase, task_to_list
from session9.c import TaskOld as TaskCOld
from session9.d import TaskOld as TaskDOld
from session9.f import Task as TaskF, TaskOld as TaskFOld


class TaskOld(TaskBase):
    """Inverse of a matrix"""

    tasklist = []

    @staticmethod
    def adjoint(matrix):
        """Return the adjoint of a matrix."""
        # check square matrix
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix is not square.")
        return TaskCOld.transpose(
            [
                [
                    ((-1) ** (i + j))
                    * TaskFOld.determinant(TaskFOld.minor(matrix, i, j))
                    for j in range(len(matrix))
                ]
                for i in range(len(matrix))
            ]
        )

    @task_to_list(tasklist)
    def task1(self):
        """Write a function Adjoint, that receives a matrix A of
        dimension N x N, and returns its adjointed matrix"""
        matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return {"Adjoint of A": self.adjoint(matrix_A)}

    @staticmethod
    def inverse(matrix):
        """Return the inverse of a matrix."""
        # check determinant != 0
        det = TaskFOld.determinant(matrix)
        if det == 0:
            raise ValueError("Determinant is 0, inverse does not exist.")
        return TaskDOld.scalar_mult(1 / det, TaskOld.adjoint(matrix))

    @task_to_list(tasklist)
    def task2(self):
        """Write a function Inverse, that receives a matrix A of
        dimension N x N, and returns its inverse matrix"""
        matrix_A = [[1, 2, 1], [0, 2, 1], [1, 0, 1]]
        return {"Inverse of A": self.inverse(matrix_A)}


class Task(TaskBase):
    """Inverse of a matrix"""

    tasklist = []

    @staticmethod
    def adjoint(matrix):
        """Return the adjoint of a matrix."""
        # check square matrix
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix is not square.")
        # return matrix.H
        return np.array(
            [
                [
                    ((-1) ** (i + j))
                    * TaskF.determinant(TaskF.minor(matrix, i, j))
                    for j in range(len(matrix))
                ]
                for i in range(len(matrix))
            ]
        ).T

    @task_to_list(tasklist)
    def task1(self):
        """Write a function Adjoint, that receives a matrix A of
        dimension N x N, and returns its adjointed matrix"""
        matrix_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        return {"Adjoint of A": self.adjoint(matrix_A)}

    @staticmethod
    def inverse(matrix):
        """Return the inverse of a matrix."""
        # already an inbuily function in numpy
        # return np.linalg.inv(matrix)

        # check determinant != 0
        det = TaskF.determinant(matrix)
        if det == 0:
            raise ValueError("Determinant is 0, inverse does not exist.")
        return (1 / det) * Task.adjoint(matrix)

    @task_to_list(tasklist)
    def task2(self):
        """Write a function Inverse, that receives a matrix A of
        dimension N x N, and returns its inverse matrix"""
        matrix_A = np.array([[1, 2, 1], [0, 2, 1], [1, 0, 1]])
        return {"Inverse of A": self.inverse(matrix_A)}


if __name__ == "__main__":
    task = Task("G")
    task.run_tasks()
    print(
        task.inverse(
            np.array(
                [[3, 1, -1, 5], [2, -2, 0, 2], [1, 2, -1, -3], [2, 5, -1, 4]]
            )
        )[1][1]
    )
