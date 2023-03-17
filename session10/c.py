"""Forces in a pin jointed frame"""

import numpy as np
from helpers.task import TaskBase, task_to_list
from session10.a import Task as TaskA


class Task(TaskBase):
    """Forces in a pin jointed frame"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Solve numerically the frame to find the forces and the tensions.
        x: HC, VA, VC, Tab, Tad, Tcb, Tcd, Tdb"""
        matrix_a: np.ndarray = np.zeros((8, 8))
        vector_b: np.ndarray = np.zeros(8)
        force_hc: int = 10
        matrix_a[0, 0], vector_b[0] = 1, force_hc
        matrix_a[1, 1], matrix_a[1, 2], vector_b[1] = 1, 1, 60
        matrix_a[2, 1], vector_b[2] = 2, 60 - 2 * force_hc
        matrix_a[3, 1], matrix_a[3, 3] = 1, np.sin(np.pi / 4)
        matrix_a[4, 3], matrix_a[4, 4] = np.cos(np.pi / 4), 1
        matrix_a[5, 2], matrix_a[5, 5] = 1, 1
        matrix_a[6, 0], matrix_a[6, 6] = 1, 1
        matrix_a[7, 7], vector_b[7] = 1, 60
        vector_x: np.ndarray = TaskA.gauss_elim(matrix_a, vector_b)
        return {"vector_x": vector_x}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
