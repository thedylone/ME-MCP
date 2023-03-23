"""Task C"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Task C"""

    tasklist: list = []

    @staticmethod
    def in_bounds(x_pos, y_pos) -> bool:
        """Check if the ant is within the bounds of the pipe"""
        # top wall
        if y_pos > x_pos + 4:
            return False
        # bottom wall
        if y_pos < x_pos + 2:
            return False
        # x-axis
        if y_pos < 0:
            return False
        # circle 1
        if (x_pos + 2) ** 2 + (y_pos - 1) ** 2 < 0.4**2:
            return False
        # circle 2
        if (x_pos + 1) ** 2 + (y_pos - 2) ** 2 < 0.4**2:
            return False
        return True

    @task_to_list(tasklist)
    def task1(self):
        """An ant is located within a pipe, with shape and dimensions
        as specified in Figure C. The pipe contains two circular obstacles
        centred at (-2,1) and (-1,2), respectively, both with radius 0.4.
        The ant is initially located at (-3,0) and moves in small steps.
        At every step the ant jumps to a new position by a small distance.
        The lengths, dx, dy of the motions are independent random values
        between -0.3 and 0.3.
        If, after a step, the ant hits one of the walls or the circular
        obstacles or goes beyond them, it is bounced back to the last position.
        Write a script to simulate the movement of the ant, until it escapes
        through the exit. If the ant does not manage to escape after
        1000 moves (including those when it hits a wall or an obstacle and
        bounces back) the script should stop and declare with a printed
        message that “The ant is exhausted”.
        Plot the trace of the ant's steps."""
        x_vals: list[float] = [-3]
        y_vals: list[float] = [0]
        x_pos = -3
        y_pos = 0
        steps = 0
        escape = False
        while steps < 1000:
            delta_x: float = np.random.uniform(-0.3, 0.3)
            delta_y: float = np.random.uniform(-0.3, 0.3)
            x_pos += delta_x
            y_pos += delta_y
            x_vals.append(x_pos)
            y_vals.append(y_pos)
            steps += 1
            if not Task.in_bounds(x_pos, y_pos):
                x_pos -= delta_x
                y_pos -= delta_y
                x_vals.append(x_pos)
                y_vals.append(y_pos)
                steps += 1
            if x_pos > 0:
                escape = True
                break
        if escape:
            print("The ant escaped!")
        else:
            print("The ant is exhausted!")
        plt.plot(x_vals, y_vals)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Ant's path")
        # plot pipe walls and obstacles
        plt.plot([-4, 0], [0, 4], "k")
        plt.plot([-2, 0], [0, 2], "k")
        plt.axhline(0, color="k")
        plt.axvline(0, color="k")
        # add circles
        circle1 = plt.Circle((-2, 1), 0.4, color="k", fill=False)
        circle2 = plt.Circle((-1, 2), 0.4, color="k", fill=False)
        plt.gca().add_patch(circle1)
        plt.gca().add_patch(circle2)
        plt.gca().set_aspect("equal")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
