"""Solutions of a linear system"""

import numpy as np
from helpers.task import TaskBase, task_to_list
from session10.a import Task as TaskA


class Task(TaskBase):
    """Solutions of a linear system"""

    tasklist: list = []

    @staticmethod
    def lin_sys(matrix_a: np.ndarray, vector_p: np.ndarray) -> np.ndarray:
        """Solve a linear system"""
        determinant: float = np.linalg.det(matrix_a)
        homogeneous: bool = np.allclose(vector_p, np.zeros(len(vector_p)))
        if determinant == 0:
            if homogeneous:
                print("The system has infinitely many solutions")
            else:
                print("The system has no solutions")
        else:
            print("The system has a unique solution")
            if homogeneous:
                print("The system has a trivial solution")
        # return np.linalg.solve(matrix_a, vector_p)
        return TaskA.gauss_elim(matrix_a, vector_p)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, np.ndarray]:
        """Write a function LinSystems, that receives a set of n linear
        equations, in the form of a matrix A and a vector p: A . x = p,
        and prints out one of the possible results, as
        learned in Maths lecture
        If the system has a solution, the function should also return the
        values of the array x (make use of the function GaussElimination,
        to determine the solution, and previous functions form Session 9 to
        compute the determinant)."""
        print("test det = 0, p != 0")
        matrix_a: np.ndarray = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        vector_p: np.ndarray = np.array([1, 2, 3])
        vector_x: np.ndarray = self.lin_sys(matrix_a, vector_p)
        print("vector_x:", vector_x)
        print("test det = 0, p = 0")
        vector_p: np.ndarray = np.array([0, 0, 0])
        vector_x: np.ndarray = self.lin_sys(matrix_a, vector_p)
        print("vector_x:", vector_x)
        print("test det != 0, p = 0")
        matrix_a: np.ndarray = np.array([[1, 2, 3], [0, 3, 4], [3, 4, 5]])
        vector_x: np.ndarray = self.lin_sys(matrix_a, vector_p)
        print("vector_x:", vector_x)
        print("test det != 0, p != 0")
        vector_p: np.ndarray = np.array([1, 2, 3])
        vector_x: np.ndarray = self.lin_sys(matrix_a, vector_p)
        return {"vector_x": vector_x}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
