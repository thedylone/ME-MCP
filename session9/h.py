"""System of linear equations"""

import numpy as np
from helpers.task import TaskBase, task_to_list
from session9.c import TaskOld as TaskCOld
from session9.e import TaskOld as TaskEOld
from session9.f import TaskOld as TaskFOld
from session9.g import TaskOld as TaskGOld


class TaskOld(TaskBase):
    """System of linear equations"""

    tasklist: list = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.matrix_a: list[list[float | int]] = []
        self.matrix_b: list[list[float | int]] = []

    @task_to_list(tasklist)
    def get_matrices(self) -> dict[str, list[list[float | int]]]:
        """Get the matrices A and b"""
        self.matrix_a = [[1, -3, -3], [2, 3, -2], [-2, 0, 2]]
        self.matrix_b = [[-14], [2], [4]]
        # check dimensions
        if len(self.matrix_a[0]) != len(self.matrix_b):
            raise ValueError("Dimensions do not match.")
        return {"A": self.matrix_a, "b": self.matrix_b}

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[float | int]]]:
        """Determine the solution x, by inverting the matrix A"""
        return {
            "x": TaskEOld.matmat(
                TaskGOld.inverse(self.matrix_a), self.matrix_b
            )
        }

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[list[float | int]]]:
        """Determine the solution x, by applying Cramer's rule"""
        return {
            "x": [
                [
                    TaskFOld.determinant(
                        TaskCOld.transpose(self.matrix_a)[:i]
                        + [[b for row in self.matrix_b for b in row]]
                        + TaskCOld.transpose(self.matrix_a)[i + 1 :]
                    )
                    / TaskFOld.determinant(self.matrix_a)
                ]
                for i in range(len(self.matrix_a))
            ]
        }


class Task(TaskBase):
    """System of linear equations"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.matrix_a: np.ndarray
        self.matrix_b: np.ndarray

    @task_to_list(tasklist)
    def get_matrices(self) -> dict[str, np.ndarray]:
        """Get the matrices A and b"""
        self.matrix_a = np.array([[1, -3, -3], [2, 3, -2], [-2, 0, 2]])
        self.matrix_b = np.array([[-14], [2], [4]])
        # check dimensions
        if len(self.matrix_a[0]) != len(self.matrix_b):
            raise ValueError("Dimensions do not match.")
        return {"A": self.matrix_a, "b": self.matrix_b}

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Determine the solution x, by inverting the matrix A"""
        return {"x": np.linalg.inv(self.matrix_a) @ self.matrix_b}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, np.ndarray]:
        """Determine the solution x, by applying Cramer's rule"""
        return {
            "x": np.array(
                [
                    [
                        np.linalg.det(
                            np.concatenate(
                                (
                                    self.matrix_a.T[:i],
                                    [np.ndarray.flatten(self.matrix_b)],
                                    self.matrix_a.T[i + 1 :],
                                ),
                                axis=0,
                            )
                        )
                        / np.linalg.det(self.matrix_a)
                    ]
                    for i in range(len(self.matrix_a))
                ]
            )
        }


if __name__ == "__main__":
    task: Task = Task("H")
    task.run_tasks()
    task.matrix_a = np.array(
        [
            [1, -2, 1, 5],
            [1, -5, 2, 1],
            [-1, 2, 7, 2],
            [2, -1, 3, 8],
        ]
    )
    task.matrix_b = np.array([[2], [-7], [-1], [5]])
    task.log("task 2", **task.task2())
