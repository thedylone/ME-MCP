"""Inverse of a matrix"""

from helpers.task import TaskBase, task_to_list
from session9.c import Task as TaskC
from session9.d import Task as TaskD
from session9.f import Task as TaskF


class Task(TaskBase):
    """Inverse of a matrix"""

    tasklist = []

    @staticmethod
    def adjoint(matrix):
        """Return the adjoint of a matrix."""
        # check square matrix
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix is not square.")
        return TaskC.transpose(
            [
                [
                    ((-1) ** (i + j))
                    * TaskF.determinant(TaskF.minor(matrix, i, j))
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
        det = TaskF.determinant(matrix)
        if det == 0:
            raise ValueError("Determinant is 0, inverse does not exist.")
        return TaskD.scalar_mult(1 / det, Task.adjoint(matrix))

    @task_to_list(tasklist)
    def task2(self):
        """Write a function Inverse, that receives a matrix A of
        dimension N x N, and returns its inverse matrix"""
        matrix_A = [[1, 2, 1], [0, 2, 1], [1, 0, 1]]
        return {"Inverse of A": self.inverse(matrix_A)}


if __name__ == "__main__":
    task = Task("G")
    task.run_tasks()
    print(
        task.inverse(
            ([[3, 1, -1, 5], [2, -2, 0, 2], [1, 2, -1, -3], [2, 5, -1, 4]])
        )[1][1]
    )
