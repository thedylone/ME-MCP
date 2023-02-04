"""Method definition"""

import copy
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from session7.a import Euclidean, Point, Line, Polygon


# class Polygon
def perimeter(self):
    """Calculate the perimeter of the shape"""
    verts = self.vertices
    return sum(
        (
            (verts[i].x - verts[i - 1].x) ** 2
            + (verts[i].y - verts[i - 1].y) ** 2
        )
        ** 0.5
        for i in range(self.nsides)
    )


def area(self):
    """Calculate the area of the shape"""
    verts = self.vertices
    return (
        sum(
            verts[i - 1].x * verts[i].y - verts[i].x * verts[i - 1].y
            for i in range(self.nsides)
        )
        / 2
    )


def centroid(self):
    """Calculate the centroid of the polygon"""
    verts = self.vertices
    centroid_x = sum(
        (verts[i - 1].x + verts[i].x)
        * (verts[i - 1].x * verts[i].y - verts[i].x * verts[i - 1].y)
        for i in range(self.nsides)
    )
    centroid_y = sum(
        (verts[i - 1].y + verts[i].y)
        * (verts[i - 1].x * verts[i].y - verts[i].x * verts[i - 1].y)
        for i in range(self.nsides)
    )
    _area = self.area()
    return Point(centroid_x / (6 * _area), centroid_y / (6 * _area))


def plot(self, colour):
    """Plot the polygon"""
    x_coords = [vertex.x for vertex in self.vertices]
    y_coords = [vertex.y for vertex in self.vertices]
    plt.fill(x_coords, y_coords, colour)
    plt.show()


# class Euclidean:
def shift(self, centre):
    """Shift the shape to a new centre"""
    current_centroid = self.shape.centroid()
    shift_x = centre.x - current_centroid.x
    shift_y = centre.y - current_centroid.y
    for vertex in self.shape.vertices:
        vertex.x += shift_x
        vertex.y += shift_y


def mirror(self, axis):
    """Mirror the shape across an axis"""
    if axis == "x":
        for vertex in self.shape.vertices:
            vertex.y *= -1
    if axis == "y":
        for vertex in self.shape.vertices:
            vertex.x *= -1
    return


def join(self, other):
    """Join the centroid of two shapes with a line"""
    return Line(self.shape.centroid(), other.shape.centroid())


def duplicate(self):
    """Duplicate the shape"""
    new_shape = copy.deepcopy(self.shape)
    new_euclidean = Euclidean(self.name, new_shape)
    return new_euclidean


class Task(TaskBase):
    """Method definition"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """For the class Polygon, define the following methods:
        perimeter, area, centroid, plot"""
        Polygon.perimeter = perimeter
        Polygon.area = area
        Polygon.centroid = centroid
        Polygon.plot = plot

    @task_to_list(tasklist)
    def task2(self):
        """For the class Euclidean, define the following methods:
        shift, mirror, join, duplicate"""
        Euclidean.shift = shift
        Euclidean.mirror = mirror
        Euclidean.join = join
        Euclidean.duplicate = duplicate


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
