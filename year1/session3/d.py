"""Series expansion"""

import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Plot(int):
    """Class for plotting"""

    y_vals: list[float] = []


class Task(TaskBase):
    """Series expansion"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.plots: list[Plot] = [Plot(2), Plot(6), Plot(10), Plot(14)]
        self.x_vals: list[float] = list(map(lambda x: x / 100, range(-80, 80)))

    @task_to_list(tasklist)
    def task1(self) -> None:
        """y(x) = 1/(1-x) = sum_{i=0}^{N to inf} x^i
        Write a script to evaluate the function y(x)
        in the range x = [-0.8 0.8] with step 0.01,
        for values of N = 2, 6, 10, 14."""
        for plot in self.plots:
            plot.y_vals = [
                sum(x**i for i in range(plot + 1)) for x in self.x_vals
            ]

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Plot, on the same graph, y(x) vs x
        in the specified range x = [-0.8 0.8],
        for each value of N."""
        for plot in self.plots:
            plt.plot(self.x_vals, plot.y_vals, label=f"N={plot}")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Evaluate the analytical value of y(x) in the same range of x
        and plot it, to compare the exact function with the truncated series"""
        true_y: list[float] = [1 / (1 - x) for x in self.x_vals]
        for plot in self.plots:
            plt.plot(self.x_vals, plot.y_vals, label=f"N={plot}")
        plt.plot(self.x_vals, true_y, label="True")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    print(task.plots[-1].y_vals[10])
