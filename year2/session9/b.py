"""Interpolation over a triangle: barycentric coordinates"""

import numpy as np

from helpers.task import TaskBase, task_to_list


def tr_baryc(
    r1: tuple[float, float],
    r2: tuple[float, float],
    r3: tuple[float, float],
    vals: tuple[float, float, float],
    rp: tuple[float, float],
) -> float:
    """Interpolate the value of a function at a point inside a triangle using
    the barycentric coordinates method.

    Args:
        r1 (tuple[float, float]): Coordinates of the first point.
        r2 (tuple[float, float]): Coordinates of the second point.
        r3 (tuple[float, float]): Coordinates of the third point.
        f1 (float): Value of the function at the first point.
        f2 (float): Value of the function at the second point.
        f3 (float): Value of the function at the third point.
        rp (tuple[float, float]): Coordinates of the point to interpolate.

    Returns:
        float: Interpolated value of the function at the point rp.
    """
    # barycentric coordinates method
    A: np.ndarray = np.array(
        [[r1[0], r2[0], r3[0]], [r1[1], r2[1], r3[1]], [1, 1, 1]]
    )
    b: np.ndarray = np.array([rp[0], rp[1], 1])
    alpha, beta, gamma = np.linalg.solve(A, b)
    return alpha * vals[0] + beta * vals[1] + gamma * vals[2]


class Task(TaskBase):
    """Interpolation over a triangle: barycentric coordinates"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Write a function TrBaryc, to interpolate three points with the
        barycentric coordinates method. The function has same input and output
        arguments as in Task A."""
        return {
            "quiz": tr_baryc((-1, -2), (1, 3), (3, 0.5), (1, 1.5, 5), (1, 0.5))
        }


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
