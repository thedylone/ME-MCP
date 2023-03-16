"""Class definition"""

from collections.abc import Callable
from helpers.task import TaskBase


class Point:
    """Define a class Point, representing a point in 2D space,
    with attributes: x, y."""

    x_coord: float
    y_coord: float

    def __init__(self, x_coord: float, y_coord: float) -> None:
        pass


class Line:
    """Define a class Line, representing a line in 2D space,
    with attributes: Point1, Point2."""

    point1: Point
    point2: Point

    def __init__(self, point1: Point, point2: Point) -> None:
        pass


class Polygon:
    """Define a class Polygon, representing a polygon,
    with attributes: nsides, vertex."""

    nsides: int
    vertices: list[Point]
    perimeter: Callable[..., float]
    area: Callable[..., float]
    centroid: Callable[..., Point]
    plot: Callable[..., None]

    def __init__(self, nsides: int, vertices: list[Point]) -> None:
        pass


class Euclidean:
    """Define a class Euclidean, representing a geometrical shape,
    with attributes: name and shape."""

    name: str
    shape: Polygon
    shift: Callable[..., None]
    mirror: Callable[..., None]
    join: Callable[..., Line]
    duplicate: Callable

    def __init__(self, name: str, shape: Polygon) -> None:
        pass


class Task(TaskBase):
    """Class definition"""


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
