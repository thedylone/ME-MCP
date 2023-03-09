"""System of linear equations"""

from helpers.task import TaskBase, task_to_list
from session9.c import Task as TaskC
from session9.e import Task as TaskE
from session9.f import Task as TaskF
from session9.g import Task as TaskG


class Task(TaskBase):
    """System of linear equations"""

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.matrix_A = []
        self.matrix_b = []

    @task_to_list(tasklist)
    def get_matrices(self):
        """Get the matrices A and b"""
        self.matrix_A = [[1, -3, -3], [2, 3, -2], [-2, 0, 2]]
        self.matrix_b = [[-14], [2], [4]]
        # check dimensions
        if len(self.matrix_A[0]) != len(self.matrix_b):
            raise ValueError("Dimensions do not match.")
        return {"A": self.matrix_A, "b": self.matrix_b}

    @task_to_list(tasklist)
    def task1(self):
        """Determine the solution x, by inverting the matrix A"""
        return {"x": TaskE.matmat(TaskG.inverse(self.matrix_A), self.matrix_b)}

    @task_to_list(tasklist)
    def task2(self):
        """Determine the solution x, by applying Cramer's rule"""
        return {
            "x": [
                [
                    TaskF.determinant(
                        TaskC.transpose(self.matrix_A)[:i]
                        + [[b for row in self.matrix_b for b in row]]
                        + TaskC.transpose(self.matrix_A)[i + 1 :]
                    )
                    / TaskF.determinant(self.matrix_A)
                ]
                for i in range(len(self.matrix_A))
            ]
        }


if __name__ == "__main__":
    task = Task("H")
    task.run_tasks()
    task.matrix_A = [
        [1, -2, 1, 5],
        [1, -5, 2, 1],
        [-1, 2, 7, 2],
        [2, -1, 3, 8],
    ]
    task.matrix_b = [[2], [-7], [-1], [5]]
    task.log(task.task2())
