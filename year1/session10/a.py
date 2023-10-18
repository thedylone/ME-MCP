"""Gaussian elimination"""

import numpy as np
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Gaussian elimination"""

    tasklist: list = []

    @staticmethod
    def gauss_elim(matrix_a: np.ndarray, vector_b: np.ndarray) -> np.ndarray:
        """Gaussian elimination"""
        for i in range(len(matrix_a) - 1):
            for j in range(i + 1, len(matrix_a)):
                ratio: float = matrix_a[j, i] / matrix_a[i, i]
                matrix_a[j] = matrix_a[j] - ratio * matrix_a[i]
                vector_b[j] = vector_b[j] - ratio * vector_b[i]
        matrix_x: np.ndarray = np.zeros(len(matrix_a))
        matrix_x[-1] = vector_b[-1] / matrix_a[-1, -1]
        for i in range(len(matrix_a) - 2, -1, -1):
            matrix_x[i] = (
                vector_b[i] - np.dot(matrix_a[i, i + 1 :], matrix_x[i + 1 :])
            ) / matrix_a[i, i]
        return matrix_x

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Write a function, GaussElimination, that receives a set
        of n linear equations, in the form of a matrix A and a vector b,
        and outputs the vector solution x.
        """
        matrix_a: np.ndarray = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        vector_b: np.ndarray = np.array([1, 2, 3])
        vector_x: np.ndarray = self.gauss_elim(matrix_a, vector_b)
        return {"vector_x": vector_x}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Test the function to solve the set of equations.
        Solution: [1.3232 1.5657 -0.6061 0.7172]"""
        matrix_a: np.ndarray = np.array(
            [[8, -2, 1, 3], [1, -5, 2, 1], [-1, 2, 7, 2], [2, -1, 3, 8]],
            dtype=float,
        )
        vector_b: np.ndarray = np.array([9, -7, -1, 5], dtype=float)
        vector_x: np.ndarray = self.gauss_elim(matrix_a, vector_b)
        assert np.allclose(
            np.dot(matrix_a, vector_x), vector_b
        ), "Gauss elimination failed"
        return {"vector_x": vector_x}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
