"""Method definition"""

import copy
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from year1.session7.a import Euclidean, Point, Line, Polygon


# class Polygon
def perimeter(self: Polygon) -> float:
    """Calculate the perimeter of the shape"""
    verts: list[Point] = self.vertices
    return sum(
        (
            (verts[i].x_coord - verts[i - 1].x_coord) ** 2
            + (verts[i].y_coord - verts[i - 1].y_coord) ** 2
        )
        ** 0.5
        for i in range(self.nsides)
    )


def area(self: Polygon) -> float:
    """Calculate the area of the shape"""
    verts: list[Point] = self.vertices
    return (
        sum(
            verts[i - 1].x_coord * verts[i].y_coord
            - verts[i].x_coord * verts[i - 1].y_coord
            for i in range(self.nsides)
        )
        / 2
    )


def centroid(self: Polygon) -> Point:
    """Calculate the centroid of the polygon"""
    verts: list[Point] = self.vertices
    centroid_x: float = sum(
        (verts[i - 1].x_coord + verts[i].x_coord)
        * (
            verts[i - 1].x_coord * verts[i].y_coord
            - verts[i].x_coord * verts[i - 1].y_coord
        )
        for i in range(self.nsides)
    )
    centroid_y: float = sum(
        (verts[i - 1].y_coord + verts[i].y_coord)
        * (
            verts[i - 1].x_coord * verts[i].y_coord
            - verts[i].x_coord * verts[i - 1].y_coord
        )
        for i in range(self.nsides)
    )
    _area: float = self.area()
    return Point(centroid_x / (6 * _area), centroid_y / (6 * _area))


def plot(self: Polygon, colour) -> None:
    """Plot the polygon"""
    x_coords: list[float] = [vertex.x_coord for vertex in self.vertices]
    y_coords: list[float] = [vertex.y_coord for vertex in self.vertices]
    plt.fill(x_coords, y_coords, colour)
    plt.show()


# class Euclidean:
def shift(self: Euclidean, centre: Point) -> None:
    """Shift the shape to a new centre"""
    current_centroid: Point = self.shape.centroid()
    shift_x: float = centre.x_coord - current_centroid.x_coord
    shift_y: float = centre.y_coord - current_centroid.y_coord
    for vertex in self.shape.vertices:
        vertex.x_coord += shift_x
        vertex.y_coord += shift_y


def mirror(self: Euclidean, axis) -> None:
    """Mirror the shape across an axis"""
    if axis == "x":
        for vertex in self.shape.vertices:
            vertex.y_coord *= -1
    if axis == "y":
        for vertex in self.shape.vertices:
            vertex.x_coord *= -1


def join(self: Euclidean, other: Euclidean) -> Line:
    """Join the centroid of two shapes with a line"""
    return Line(self.shape.centroid(), other.shape.centroid())


def duplicate(self: Euclidean) -> Euclidean:
    """Duplicate the shape"""
    new_shape: Polygon = copy.deepcopy(self.shape)
    new_euclidean: Euclidean = Euclidean(self.name, new_shape)
    return new_euclidean


class Task(TaskBase):
    """Method definition"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """For the class Polygon, define the following methods:
        perimeter, area, centroid, plot"""
        Polygon.perimeter = perimeter
        Polygon.area = area
        Polygon.centroid = centroid
        Polygon.plot = plot

    @task_to_list(tasklist)
    def task2(self) -> None:
        """For the class Euclidean, define the following methods:
        shift, mirror, join, duplicate"""
        Euclidean.shift = shift
        Euclidean.mirror = mirror
        Euclidean.join = join
        Euclidean.duplicate = duplicate


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
