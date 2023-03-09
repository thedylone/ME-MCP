"""Sum of two matrices"""

from helpers.task import TaskBase, task_to_list
from session9.c import Task as TaskC


class Task(TaskBase):
    """Sum of two matrices"""

    tasklist = []

    def import_matrix(self, path, rows, cols):
        """Import a matrix from a file."""
        with open(path, "r") as f:
            matrix = []
            for _ in range(rows):
                matrix.append([int(f.readline()) for _ in range(cols)])
        return matrix

    @task_to_list(tasklist)
    def task1(self):
        """The files MatA.txt and MatB.txt contain the values of two matrices,
        A and B, of size 60x60. Entries of the matrices are stored in the file
        one value per line, sequentially as they appear in the matrix. Read in
        the numerical values from the two files and form the two matrices
        A and B accordingly."""
        self.matrix_A = self.import_matrix("session9/MatA.txt", 60, 60)
        self.matrix_B = self.import_matrix("session9/MatB.txt", 60, 60)

    @staticmethod
    def matsum(matrix_A, matrix_B):
        """Sum of two matrices."""
        if len(matrix_A) != len(matrix_B):
            raise ValueError("Matrices must have the same number of rows")
        if len(matrix_A[0]) != len(matrix_B[0]):
            raise ValueError("Matrices must have the same number of columns")
        return [
            [matrix_A[i][j] + matrix_B[i][j] for j in range(len(matrix_A[0]))]
            for i in range(len(matrix_A))
        ]

    @task_to_list(tasklist)
    def task2(self):
        """Write a function MatSum, that receives two matrices, A and B,
        and returns the sum of them"""
        return {"A + B": self.matsum(self.matrix_A, self.matrix_B)}

    @staticmethod
    def scalar_mult(scalar, matrix):
        """Multiply a matrix by a scalar."""
        return [
            [scalar * matrix[i][j] for j in range(len(matrix[0]))]
            for i in range(len(matrix))
        ]

    @task_to_list(tasklist)
    def task3(self):
        """Compute the matrix D = 0.5(A + A^T) + 0.5(A - A^T)
        and verify that D is the same as A"""
        matrix_D = self.matsum(
            self.scalar_mult(
                0.5,
                self.matsum(self.matrix_A, TaskC.transpose(self.matrix_A)),
            ),
            self.scalar_mult(
                0.5,
                self.matsum(
                    self.matrix_A,
                    self.scalar_mult(-1, TaskC.transpose(self.matrix_A)),
                ),
            ),
        )
        return {"D == A": matrix_D == self.matrix_A}


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()
