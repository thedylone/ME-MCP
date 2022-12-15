"""Counted loops: Series expansion"""

import matplotlib.pyplot as plt
import numpy as np

from helpers.task import TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Counted loops: Series expansion"""

    tasklist = []

    @task_to_list(tasklist)
    def exercise1(self):
        """The function sin(x) can be evaluated with the Taylor expansion:
        sin(x) = sum_{i=1}^{N} (-1)^int(i/2) x^i / i!, where i is odd
        Write a script to compute and plot sin(x) vs x
        in the range x = [0 : 2pi] with step 0.01, for a given N."""
        x_vals = np.arange(0, 2 * np.pi, 0.01)
        y_vals = []
        upper = get_input(int, "upper bound")
        for x in x_vals:
            running = 0
            for i in range(1, upper + 1, 2):
                running += (-1) ** (i // 2) * x**i / np.math.factorial(i)
            y_vals.append(running)
        plt.plot(x_vals, y_vals)
        plt.show()


if __name__ == "__main__":
    task = Task("Exercise 1")
    task.run_tasks()
