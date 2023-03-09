"""Matrix-matrix multiplication"""

from helpers.task import TaskBase, task_to_list
from session9.d import Task as TaskD


class Task(TaskBase):
    """Matrix-matrix multiplication"""

    tasklist = []

    @staticmethod
    def matmat(matrix_A, matrix_B):
        """Multiply two matrices. Return 0 if the sizes are incompatible."""
        if len(matrix_A[0]) != len(matrix_B):
            return 0
        return [
            [
                sum(a * b for a, b in zip(row_A, col_B))
                for col_B in zip(*matrix_B)
            ]
            for row_A in matrix_A
        ]

    @task_to_list(tasklist)
    def task1(self):
        """Write a function, MatMat, that receives two matrices, A and B,
        and returns the product of the two matrices, P = AB. The function
        should return the value 0 if the sizes of the two matrices are
        incompatible for the multiplication.
        Verify that A * B != B * A"""
        taskD = TaskD("D", False)
        taskD.task1()
        matrix_A = taskD.matrix_A
        matrix_B = taskD.matrix_B
        return {
            "A * B == B * A": self.matmat(matrix_A, matrix_B)
            == self.matmat(matrix_B, matrix_A)
        }


if __name__ == "__main__":
    task = Task("E")
    task.run_tasks()
