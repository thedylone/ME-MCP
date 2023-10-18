"""Use of methods"""

import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from year1.session7.d import Task as TaskD
from year1.session7.a import Point, Line, Euclidean


class Task(TaskBase):
    """Use of methods"""

    tasklist: list = []
    task_d: TaskD = TaskD(output=False)
    task_d.run_tasks()
    poly1: Euclidean = task_d.poly1
    poly2: Euclidean = task_d.poly2
    poly3: Euclidean = task_d.poly3
    poly4: Euclidean = task_d.poly4
    poly5: Euclidean
    shapes: list[Euclidean] = [poly1, poly2, poly3, poly4]

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.plot_all()

    def plot_all(self) -> None:
        """Plot all shapes"""
        for poly in self.shapes:
            plt.fill(
                [p.x_coord for p in poly.shape.vertices],
                [p.y_coord for p in poly.shape.vertices],
                linewidth=2,
            )
        plt.show()

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Move Pol1 over Pol2 (overlapping the centroid of the two shapes)"""
        self.poly1.shift(self.poly2.shape.centroid())
        self.plot_all()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Mirror Pol4 around the y axis."""
        self.poly4.mirror("y")
        self.plot_all()

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Join the centroid of the mirrored Pol4 with that of Pol3."""
        line: Line = self.poly4.join(self.poly3)
        pts: list[tuple[float, float]] = [
            (line.point1.x_coord, line.point1.y_coord),
            (line.point1.x_coord, line.point1.y_coord + 0.1),
            (line.point2.x_coord, line.point2.y_coord + 0.1),
            (line.point2.x_coord, line.point2.y_coord),
        ]
        self.shapes.append(TaskD.create("line", 2, pts))
        self.plot_all()

    @task_to_list(tasklist)
    def task4(self) -> dict[str, float]:
        """Determine perimeters of all shapes."""
        return {poly.name: poly.shape.perimeter() for poly in self.shapes}

    @task_to_list(tasklist)
    def task5(self) -> None:
        """Duplicate Pol3, positioning the new shape across
        the new centroid (-4,-5)."""
        self.poly5 = self.poly3.duplicate()
        self.poly5.shift(Point(-4, -5))
        self.shapes.append(self.poly5)
        self.plot_all()


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
