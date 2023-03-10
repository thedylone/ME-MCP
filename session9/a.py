"""Use of numpy"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Use of numpy"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Create a range of values x between -2.0 and 5.8
        with step dx = 0.1."""
        self.x_vals = np.arange(-2.0, 5.8, 0.1)
        return {"x_vals head": self.x_vals[:5]}

    @task_to_list(tasklist)
    def task2(self):
        """Calculate the values y = sin x for the above range of x."""
        self.y_vals = np.sin(self.x_vals)
        return {"y_vals head": self.y_vals[:5]}

    @task_to_list(tasklist)
    def task3(self):
        """Plot y vs x."""
        plt.plot(self.x_vals, self.y_vals)
        plt.show()

    @task_to_list(tasklist)
    def task4(self):
        """Create a range of 100 values x between -2.0 and 5.8."""
        self.x_vals = np.linspace(-2.0, 5.8, 100)
        return {"x_vals head": self.x_vals[:5]}

    @task_to_list(tasklist)
    def task5(self):
        """Calculate the values y = (e^x - e^(-x))/2
        for the above range of x."""
        self.y_vals = (np.exp(self.x_vals) - np.exp(-self.x_vals)) / 2
        return {"y_vals head": self.y_vals[:5]}

    @task_to_list(tasklist)
    def task6(self):
        """Plot y vs x."""
        plt.plot(self.x_vals, self.y_vals)
        plt.show()

    @task_to_list(tasklist)
    def task7(self):
        """Generate an array x of numbers in the range [-5 : 5]
        with the following steps:
            dx = 0.5 in -5 <= x <= -2,
            dx = 0.05 in -2 < x < 3,
            dx = 0.5 in 3 <= x <= 5"""
        self.x_vals = np.concatenate(
            (
                np.arange(-5, -1.5, 0.5),
                np.arange(-2.05, 3, 0.05),
                np.arange(3, 5.5, 0.5),
            )
        )
        return {"x_vals head": self.x_vals[:5]}

    @task_to_list(tasklist)
    def task8(self):
        """Compute the function: y = e^(-x^2 / 4) in the above range."""
        self.y_vals = np.exp(-self.x_vals**2 / 4)
        return {"y_vals head": self.y_vals[:5]}

    @task_to_list(tasklist)
    def task9(self):
        """Plot y vs x."""
        plt.plot(self.x_vals, self.y_vals)
        plt.show()


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
    print(task.x_vals[14])
