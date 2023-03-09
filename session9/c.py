"""Transpose of a matrix"""

import random
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Transpose of a matrix"""

    tasklist = []
    matrix_R = []

    @task_to_list(tasklist)
    def task1(self):
        """Create  a  matrix  R  of  random  integer  numbers
        between  1  and  100,  with dimensions 10 x 5."""
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


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
