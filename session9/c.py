"""Transpose of a matrix"""

import numpy as np
import random
from helpers.task import TaskBase, task_to_list


class TaskOld(TaskBase):
    """Transpose of a matrix"""

    tasklist = []
    matrix_R = []

    @task_to_list(tasklist)
    def task1(self):
        """Create a matrix R of random integer numbers
        between 1 and 100, with dimensions 10 x 5."""
        for _ in range(10):
            self.matrix_R.append([random.randint(1, 100) for _ in range(5)])
        return {"R": self.matrix_R}

    @staticmethod
    def transpose(matrix):
        """Transpose a matrix."""
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    @task_to_list(tasklist)
    def task2(self):
        """Write a function Transpose, that receives a matrix R
        and returns its transpose."""
        return {"Transposed R": self.transpose(self.matrix_R)}


class Task(TaskBase):
    """Transpose of a matrix"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Create a matrix R of random integer numbers
        between 1 and 100, with dimensions 10 x 5."""
        self.matrix_R = np.random.randint(1, 100, (10, 5))
        return {"R": self.matrix_R}

    @staticmethod
    def transpose(matrix):
        """Transpose a matrix."""
        # already an inbuilt function in numpy
        return matrix.T

    @task_to_list(tasklist)
    def task2(self):
        """Write a function Transpose, that receives a matrix R
        and returns its transpose."""
        self.matrix_R = Task.transpose(self.matrix_R)
        return {"Transposed R": self.matrix_R}


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
