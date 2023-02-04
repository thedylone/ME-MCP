"""Create objects"""

from helpers.task import TaskBase, task_to_list
from session7.a import Point, Polygon, Euclidean
from session7.b import Task as TaskB
from session7.c import Task as TaskC


class Task(TaskBase):
    """Create objects"""

    tasklist = []
    taskB = TaskB(output=False)
    taskB.run_tasks()
    taskC = TaskC(output=False)
    taskC.run_tasks()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poly1 = None
        self.poly2 = None
        self.poly3 = None
        self.poly4 = None

    @staticmethod
    def create(name, nside, pts):
        """Create Euclidean objects"""
        return Euclidean(name, Polygon(nside, [Point(x, y) for x, y in pts]))

    @task_to_list(tasklist)
    def task1(self):
        """Create, and initialise, instances of the above classes,
        to represent the shapes as in the figure below"""
        self.poly1 = self.create("Pol1", 4, [(2, 8), (2, 10), (8, 10), (8, 8)])
        self.poly2 = self.create("Pol2", 3, [(10, 6), (13, 10), (14, 6)])
        self.poly3 = self.create(
            "Pol3", 5, [(6, 1), (2, 3), (1, 3), (6, 4), (8, 3)]
        )
        self.poly4 = self.create("Pol4", 4, [(13, 1), (9, 3), (9, 5), (13, 5)])
        return {
            "Pol1": self.poly1,
            "Pol2": self.poly2,
            "Pol3": self.poly3,
            "Pol4": self.poly4,
        }


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()
