"""Class definition"""

from helpers.task import TaskBase


class Euclidean:
    """Define a class Euclidean, representing a geometrical shape,
    with attributes: name and shape."""


class Point:
    """Define a class Point, representing a point in 2D space,
    with attributes: x, y."""


class Line:
    """Define a class Line, representing a line in 2D space,
    with attributes: Point1, Point2."""


class Polygon:
    """Define a class Polygon, representing a polygon,
    with attributes: nsides, vertex."""


class Task(TaskBase):
    """Class definition"""


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
