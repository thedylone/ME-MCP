"""Task B"""

import os
import random
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02345678")


class Task(TaskBase):
    """Task B"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """An ant is trying to escape out of the upper-half of a semi-circular
        doughnut (in red) into the lower-half of the doughnut (in green), as
        depicted in the figure below.
        The ant is initially located at position (0,18) and moves in steps.
        At every step the ant jumps to a new position by a distance (dx,dy).
        The lengths, dx, dy of the moves are independent random values between
        -s1 and +s2, where s1 and s2 are defined as:
        s1 = (5th digit of your CID)/10 + 0.9)
        s2 = (7th digit of your CID)/10 + 0.6)
        If, after a step, the ant hits one of the walls or goes beyond it, it
        is bounced back to the last position.
        Write a script (name the file ExB) to simulate the movement of the ant
        until it reaches the green lower-half of the doughnut.
        Plot the trace of the ant's steps."""
        x_vals: list[float] = [0]
        y_vals: list[float] = [18]
        param_s1: float = int(CID[4]) / 10 + 0.9
        param_s2: float = int(CID[6]) / 10 + 0.6
        while True:
            step_x: float = random.uniform(-param_s1, param_s2)
            step_y: float = random.uniform(-param_s1, param_s2)
            new_x: float = x_vals[-1] + step_x
            new_y: float = y_vals[-1] + step_y
            x_vals.append(new_x)
            y_vals.append(new_y)
            if not 100 < new_x**2 + new_y**2 < 400:
                # out of bounds
                x_vals.append(x_vals[-2])
                y_vals.append(y_vals[-2])
                continue
            if new_y < 0:
                # reached green
                break

        plt.plot(x_vals, y_vals)
        outer = plt.Circle((0, 0), 20, color="r", fill=False)
        inner = plt.Circle((0, 0), 10, color="b", fill=False)
        plt.gca().add_patch(outer)
        plt.gca().add_patch(inner)
        plt.gca().set_aspect("equal")
        plt.show()


if __name__ == "__main__":
    print("CID:", CID)
    task: Task = Task("B")
    task.run_tasks()
