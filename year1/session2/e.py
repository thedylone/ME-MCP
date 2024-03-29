"""Finding Pi"""

import random
import matplotlib.pyplot as plt
from helpers.task import RangeValidator, TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Finding Pi"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.inside: int = 0
        self.inside_pts: list[tuple[float, float]] = []
        self.outside_pts: list[tuple[float, float]] = []

    @task_to_list(tasklist)
    def task1(self, pts=False) -> dict[str, float | int]:
        """The value of p can be determined numerically by using
        a technique based on random numbers. The area of the square
        can be represented with a set of N random spatial points
        generated within the enveloping square.
        Some of these points, Nc, will reside into the circle too,
        and would therefore represent the area of the circle.
        Write a script to estimate the value of p with a number N of points."""
        limit: int = get_input(int, "N", RangeValidator(1))
        for _ in range(limit):
            x_coord: float = random.random()
            y_coord: float = random.random()
            if x_coord * x_coord + y_coord * y_coord <= 1:
                self.inside += 1
                if pts:
                    self.inside_pts.append((x_coord, y_coord))
            elif pts:
                self.outside_pts.append((x_coord, y_coord))
        if limit:
            calc_pi: float = 4 * self.inside / limit
        else:
            calc_pi = 0
        return {"pi": calc_pi}

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Amend the above script to plot all the random points generated.
        Plot in red the points laying within the circle
        and in blue the ones laying outside the circle.
        Repeat the runs for the various N = 100, 1000, 10k.
        The plot will make more explicit the concept beyond the method."""
        self.task1(pts=True)

        scale: float = min(max(5000 / self.inside, 1), 50)

        plt.scatter(*zip(*self.inside_pts), color="red", s=scale)
        plt.scatter(*zip(*self.outside_pts), color="blue", s=scale)
        plt.gca().set_aspect("equal", adjustable="box")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
    rand: list[float] = [random.random() * 6 - 3 for _ in range(50)]
    print(min(rand), max(rand))
