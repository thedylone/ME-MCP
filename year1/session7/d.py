"""Create objects"""

from helpers.task import TaskBase, task_to_list
from year1.session7.a import Point, Polygon, Euclidean
from year1.session7.b import Task as TaskB
from year1.session7.c import Task as TaskC


class Task(TaskBase):
    """Create objects"""

    tasklist: list = []
    task_b: TaskB = TaskB(output=False)
    task_b.run_tasks()
    task_c: TaskC = TaskC(output=False)
    task_c.run_tasks()

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.poly1: Euclidean
        self.poly2: Euclidean
        self.poly3: Euclidean
        self.poly4: Euclidean

    @staticmethod
    def create(name, nside, pts) -> Euclidean:
        """Create Euclidean objects"""
        return Euclidean(name, Polygon(nside, [Point(x, y) for x, y in pts]))

    @task_to_list(tasklist)
    def task1(self) -> dict[str, Euclidean]:
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
    task: Task = Task("D")
    task.run_tasks()
