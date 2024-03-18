"""Interpolation over a triangle: inverse distance method"""

import numpy as np

from helpers.task import TaskBase, task_to_list


def trNN(
    r1: tuple[float, float],
    r2: tuple[float, float],
    r3: tuple[float, float],
    vals: tuple[float, float, float],
    rp: tuple[float, float],
) -> float:
    """Interpolate the value of a function at a point inside a triangle using
    the inverse distance method.

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
    # inverse distance method
    w1: float = 1 / np.sqrt((rp[0] - r1[0]) ** 2 + (rp[1] - r1[1]) ** 2)
    w2: float = 1 / np.sqrt((rp[0] - r2[0]) ** 2 + (rp[1] - r2[1]) ** 2)
    w3: float = 1 / np.sqrt((rp[0] - r3[0]) ** 2 + (rp[1] - r3[1]) ** 2)
    return (w1 * vals[0] + w2 * vals[1] + w3 * vals[2]) / (w1 + w2 + w3)


class Task(TaskBase):
    """Interpolation over a triangle: inverse distance method"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Write a function TrNN, to interpolate three points with the inverse
        distance method. The function receives the coordinates of three points
        (r1, r2, r3) and the values of the mathematical function at these
        three points (f1, f2, f3), and the coordinates of a fourth point
        rp , coplanar with the first three ones, and returns the interpolated
        value f(rp)."""
        return {"quiz": trNN((-1, 0), (1, 2), (2, 0.5), (1, 1.5, 3), (1, 0.5))}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
