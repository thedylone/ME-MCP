"""Task B"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Task B"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_a: np.ndarray
        self.matrix_avg: np.ndarray = np.zeros((60, 60))
        self.matrix_det: np.ndarray = np.zeros((60, 60))

    @task_to_list(tasklist)
    def task1(self):
        """The file Matrix.txt contains 360,000 numerical values. Read in the
        content and organise the values into a mathematical matrix A,
        with dimensions 600 x 600. Consider the matrix A as if subdivided into
        many (60 x 60) smaller sub-matrices of dimension 10 x 10 each,
        as depicted in Figure A."""
        self.matrix_a = np.loadtxt(
            "finals-21-22/Matrix.txt", dtype=float
        ).reshape(600, 600)
        plt.imshow(self.matrix_a)
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Write a script to implement the following operations:
        1) For every sub-matrix, determine the average of all elements, and
        store the results into a matrix AV, of dimension 60 x 60.
        2) For every sub-matrix, compute the determinant, and store the
        results into a matrix Det, of dimension 60 x 60.
        3) For every sub-matrix with a non-zero determinant compute its
        transpose and substitute the original sub-matrix in A
        with the transpose.
        For the three operations, try to use the minimum
        overall amount of loops.
        """
        for i in range(60):
            for j in range(60):
                sub_matrix: np.ndarray = self.matrix_a[
                    i * 10 : (i + 1) * 10, j * 10 : (j + 1) * 10
                ]
                self.matrix_avg[i, j] = np.mean(sub_matrix)
                self.matrix_det[i, j] = np.linalg.det(sub_matrix)
                if self.matrix_det[i, j] != 0:
                    self.matrix_a[
                        i * 10 : (i + 1) * 10, j * 10 : (j + 1) * 10
                    ] = sub_matrix.T

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Save the matrix AV into a file named Averages.txt, one element of
        the matrix per line of file, and the matrix Det into a file named
        Determinants.txt, one element of the matrix per line of file.
        Plot the final matrix A as an image."""
        np.savetxt(
            "finals-21-22/Averages.txt", self.matrix_avg.reshape(3600, 1)
        )
        np.savetxt(
            "finals-21-22/Determinants.txt", self.matrix_det.reshape(3600, 1)
        )
        plt.imshow(self.matrix_a)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
