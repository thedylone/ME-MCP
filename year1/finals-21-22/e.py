"""Task E"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Task E"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Amend the lines 3rd and 4th only, of the script below, in order
        to plot the following graph, Figure E:
        x = np.arange(-2*np.pi,2*np.pi,0.01)
        y = np.sin(x)
        xm = x[]
        ym = y[]
        pl.scatter(x,y,Linewidth=10,c='b')
        pl.scatter(xm,ym,Linewidth=1,c='r')
        pl.grid()
        pl.legend(['y','ym'])"""
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
        y = np.sin(x)
        xm = [x[i] for i in range(len(x)) if y[i] > 0]
        ym = [i for i in y if i > 0]
        plt.scatter(x, y, linewidth=10, c="b")
        plt.scatter(xm, ym, linewidth=1, c="r")
        plt.grid()
        plt.legend(["y", "ym"])
        plt.show()


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
