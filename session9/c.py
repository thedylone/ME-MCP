"""Transpose of a matrix"""

import random
import numpy as np
from helpers.task import TaskBase, task_to_list


class TaskOld(TaskBase):
    """Transpose of a matrix"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_r: list[list[float | int]] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[float | int]]]:
        """Create a matrix R of random integer numbers
        between 1 and 100, with dimensions 10 x 5."""
        for _ in range(10):
            self.matrix_r.append([random.randint(1, 100) for _ in range(5)])
        return {"R": self.matrix_r}

    @staticmethod
    def transpose(matrix: list[list[float | int]]) -> list[list[float | int]]:
        """Transpose a matrix."""
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[list[float | int]]]:
        """Write a function Transpose, that receives a matrix R
        and returns its transpose."""
        return {"Transposed R": self.transpose(self.matrix_r)}


class Task(TaskBase):
    """Transpose of a matrix"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_r: np.ndarray

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Create a matrix R of random integer numbers
        between 1 and 100, with dimensions 10 x 5."""
        self.matrix_r = np.random.randint(1, 100, (10, 5))
        return {"R": self.matrix_r}

    @staticmethod
    def transpose(matrix: np.ndarray) -> np.ndarray:
        """Transpose a matrix."""
        # already an inbuilt function in numpy
        return matrix.T

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Write a function Transpose, that receives a matrix R
        and returns its transpose."""
        self.matrix_r = Task.transpose(self.matrix_r)
        return {"Transposed R": self.matrix_r}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
