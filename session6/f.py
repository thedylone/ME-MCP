"""Fractals"""

import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Fractals"""

    tasklist = []

    @staticmethod
    def fractal(param_a, param_b, param_c, x_prev, y_prev, num):
        """Generate fractal coordinates"""
        x_vals = [x_prev]
        y_vals = [y_prev]
        for _ in range(num):
            if x_prev == 0:
                k = 0
            else:
                k = math.copysign(1, x_prev)
            x_next = y_prev - k * math.sqrt(abs(param_b * x_prev - param_c))
            y_next = param_a - x_prev
            x_vals.append(x_next)
            y_vals.append(y_next)
            x_prev, y_prev = x_next, y_next
        plt.scatter(x_vals, y_vals)
        plt.show()
        return {"last x": x_vals[-1], "last y": y_vals[-1]}

    @task_to_list(tasklist)
    def task1(self):
        """Write a script to plot N points, with coordinates (xi, yi),
        generated from the following iterative sequence
        (also known as Julia set)
        x_i = y_i-1 - k * sqrt(abs(b * x_i-1 - c))
        y_i = a - x_i-1
        k = {
            -1 if x_i-1 < 0
            0 if x_i-1 = 0
            +1 if x_i-1 > 0
        }
        """
        param_a = get_input(float, "Enter parameter a")
        param_b = get_input(float, "Enter parameter b")
        param_c = get_input(float, "Enter parameter c")
        x_prev = get_input(float, "Enter x0")
        y_prev = get_input(float, "Enter y0")
        num = get_input(int, "Enter number of points")
        return Task.fractal(param_a, param_b, param_c, x_prev, y_prev, num)


if __name__ == "__main__":
    task = Task("F")
    task.run_tasks()
    print(task.fractal(0.4, 1, 0, 0, 1, 199))
