"""Constructor"""

from helpers.task import TaskBase, task_to_list
from year1.session7.a import Euclidean, Point, Line, Polygon


def init_euclidean(self: Euclidean, name: str, shape: Polygon) -> None:
    """Initialise Euclidean attributes"""
    self.name = name
    self.shape = shape


def init_point(self: Point, x_coord: float, y_coord: float) -> None:
    """Initialise Point attributes"""
    self.x_coord = x_coord
    self.y_coord = y_coord


def repr_point(self: Point) -> str:
    """Return a string representation of Point"""
    return f"Point({self.x_coord}, {self.y_coord})"


def init_line(self: Line, point1: Point, point2: Point) -> None:
    """Initialise Line attributes"""
    self.point1 = point1
    self.point2 = point2


def init_polygon(self: Polygon, nsides: int, vertices: list[Point]) -> None:
    """Initialise Polygon attributes"""
    self.nsides = nsides
    self.vertices = vertices


class Task(TaskBase):
    """Constructor"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """For each of the classes define
        the initialising constructor __init__."""
        Euclidean.__init__ = init_euclidean
        Point.__init__ = init_point
        Point.__repr__ = repr_point
        Line.__init__ = init_line
        Polygon.__init__ = init_polygon


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
