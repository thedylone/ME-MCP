"""Constructor"""

from helpers.task import TaskBase, task_to_list
from session7.a import Euclidean, Point, Line, Polygon


def init_euclidean(self, name, shape):
    """Initialise Euclidean attributes"""
    self.name = name
    self.shape = shape


def init_point(self, x_coord, y_coord):
    """Initialise Point attributes"""
    self.x = x_coord
    self.y = y_coord


def repr_point(self):
    """Return a string representation of Point"""
    return f"Point({self.x}, {self.y})"


def init_line(self, point1, point2):
    """Initialise Line attributes"""
    self.point1 = point1
    self.point2 = point2


def init_polygon(self, nsides, vertices):
    """Initialise Polygon attributes"""
    self.nsides = nsides
    self.vertices = vertices


class Task(TaskBase):
    """Constructor"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """For each of the classes define
        the initialising constructor __init__."""
        Euclidean.__init__ = init_euclidean
        Point.__init__ = init_point
        Point.__repr__ = repr_point
        Line.__init__ = init_line
        Polygon.__init__ = init_polygon


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
