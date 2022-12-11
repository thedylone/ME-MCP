"""Counted loops and conditional flow: Ant movement tracing"""

import matplotlib.pyplot as plt
import math
import random

from helpers.task import TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Counted loops and conditional flow: Ant movement tracing"""

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        radius = random.random()
        angle = random.random() * 2 * math.pi
        self.x_pos = radius * math.cos(angle)
        self.y_pos = radius * math.sin(angle)

    @task_to_list(tasklist)
    def initial_plot(self):
        """Write a script to simulate and visualise the random motion of
        an ant within a closed circular domain. Initially generate a
        random point within the circular domain A and plot it."""
        plt.scatter(self.x_pos, self.y_pos)
        fig = plt.gcf()
        ax = fig.gca()
        ax.add_patch(plt.Circle((0, 0), 1, fill=False))
        ax.set_aspect("equal", adjustable="box")
        plt.show()

    @task_to_list(tasklist)
    def exercise2(self):
        """Then move the point N times: at every step the ant must jump to
        a new position by a distance (dx,dy). The sizes dx, dy of the move
        must be independent random values between -0.2 and 0.2.
        If the ant, after moving, leaves the domain, it must bounce back to
        the current position. Plot the trace of the ant's moves."""
        plt.scatter(self.x_pos, self.y_pos)
        times = get_input(int, "number of times")
        x_vals = [self.x_pos]
        y_vals = [self.y_pos]
        for _ in range(times):
            new_x = self.x_pos + random.random() * 0.4 - 0.2
            new_y = self.y_pos + random.random() * 0.4 - 0.2

            if new_x**2 + new_y**2 > 1:
                x_vals.append(new_x)
                y_vals.append(new_y)
            else:
                self.x_pos = new_x
                self.y_pos = new_y
            x_vals.append(self.x_pos)
            y_vals.append(self.y_pos)
        fig = plt.gcf()
        ax = fig.gca()
        ax.add_patch(plt.Circle((0, 0), 1, fill=False))
        ax.set_aspect("equal", adjustable="box")
        plt.plot(x_vals, y_vals, color="r")
        plt.show()


if __name__ == "__main__":
    task = Task("Exercise 2")
    task.run_tasks()
