"""Defining and manipulating matrices"""

import numpy as np
from helpers.task import TaskBase, task_to_list, get_input


class TaskOld(TaskBase):
    """Defining and manipulating matrices"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_h: list[list[int]] = []
        self.matrix_s: list[list[int]] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[int]]]:
        """Create a matrix H of zeros with dimensions 30 x 20"""
        self.matrix_h = [[0] * 20 for _ in range(30)]
        return {"H": self.matrix_h}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[list[int]]]:
        """Insert values 50 to 69 into the 6th row of H."""
        self.matrix_h[5] = list(range(50, 70))
        return {"H": self.matrix_h}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, list[list[int]]]:
        """Insert values 100 to 129 into the 8th column of H."""
        for i in range(30):
            self.matrix_h[i][7] = i + 100
        return {"H": self.matrix_h}

    @task_to_list(tasklist)
    def task4(self) -> dict[str, list[list[int]]]:
        """Generate a a square matrix S, of dimension N x N,
        with the following pattern:
        [
        [1 0 0 0 0 1]
        [0 1 0 0 1 0]
        [0 0 1 1 0 0]
        [0 0 1 1 0 0]
        [0 1 0 0 1 0]
        [1 0 0 0 0 1]
        ]
        """
        dimension: int = get_input(int, "dimension")
        for i in range(dimension):
            row: list[int] = [0] * dimension
            row[i] = row[-i - 1] = 1
            self.matrix_s.append(row)
        return {"S": self.matrix_s}


class Task(TaskBase):
    """Defining and manipulating matrices"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_h: np.ndarray
        self.matrix_s: np.ndarray

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Create a matrix H of zeros with dimensions 30 x 20"""
        self.matrix_h = np.zeros((30, 20))
        return {"H": self.matrix_h}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Insert values 50 to 69 into the 6th row of H."""
        self.matrix_h[5] = list(range(50, 70))
        return {"H": self.matrix_h}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, np.ndarray]:
        """Insert values 100 to 129 into the 8th column of H."""
        self.matrix_h[:, 7] = range(100, 130)
        return {"H": self.matrix_h}

    @task_to_list(tasklist)
    def task4(self) -> dict[str, np.ndarray]:
        """Generate a a square matrix S, of dimension N x N,
        with the following pattern:
        [
        [1 0 0 0 0 1]
        [0 1 0 0 1 0]
        [0 0 1 1 0 0]
        [0 0 1 1 0 0]
        [0 1 0 0 1 0]
        [1 0 0 0 0 1]
        ]
        """
        dimension: int = get_input(int, "dimension")
        self.matrix_s = np.identity(dimension)
        np.fill_diagonal(np.fliplr(self.matrix_s), 1)
        return {"S": self.matrix_s}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
