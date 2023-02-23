"""Use of methods"""

import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from session7.d import Task as TaskD
from session7.a import Point


class Task(TaskBase):
    """Use of methods"""

    tasklist = []
    taskD = TaskD(output=False)
    taskD.run_tasks()
    poly1 = taskD.poly1
    poly2 = taskD.poly2
    poly3 = taskD.poly3
    poly4 = taskD.poly4
    poly5 = None
    shapes = [poly1, poly2, poly3, poly4]

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.plot_all()

    def plot_all(self):
        """Plot all shapes"""
        for poly in self.shapes:
            plt.fill(
                [p.x for p in poly.shape.vertices],
                [p.y for p in poly.shape.vertices],
                linewidth=2,
            )
        plt.show()

    @task_to_list(tasklist)
    def task1(self):
        """Move Pol1 over Pol2 (overlapping the centroid of the two shapes)"""
        self.poly1.shift(self.poly2.shape.centroid())
        self.plot_all()

    @task_to_list(tasklist)
    def task2(self):
        """Mirror Pol4 around the y axis."""
        self.poly4.mirror("y")
        self.plot_all()

    @task_to_list(tasklist)
    def task3(self):
        """Join the centroid of the mirrored Pol4 with that of Pol3."""
        line = self.poly4.join(self.poly3)
        pts = [
            (line.point1.x, line.point1.y),
            (line.point1.x, line.point1.y + 0.1),
            (line.point2.x, line.point2.y + 0.1),
            (line.point2.x, line.point2.y),
        ]
        self.shapes.append(TaskD.create("line", 2, pts))
        self.plot_all()

    @task_to_list(tasklist)
    def task4(self):
        """Determine perimeters of all shapes."""
        return {poly.name: poly.shape.perimeter() for poly in self.shapes}

    @task_to_list(tasklist)
    def task5(self):
        """Duplicate Pol3, positioning the new shape across
        the new centroid (-4,-5)."""
        self.poly5 = self.poly3.duplicate()
        self.poly5.shift(Point(-4, -5))
        self.shapes.append(self.poly5)
        self.plot_all()


if __name__ == "__main__":
    task = Task("E")
    task.run_tasks()
