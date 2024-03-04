"""Fourier Series"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Fourier Series"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Evaluate the Fourier series, representing a saw function, by using
        different numbers of terms, i.e., N = [2,6,50]:
        y(t) = 1/2 - 1/𝜋 * sum_{n=1}^{N} sin(2n𝜋/T * t)/n
        Plot the results in the range t = [0:2T], where T is the chosen period
        for the saw wave."""
        T = 5
        t = np.linspace(0, 2 * T, 1000)
        limits = [2, 6, 50]
        for N in limits:
            y = 1 / 2 - 1 / np.pi * np.sum(
                [np.sin(2 * n * np.pi / T * t) / n for n in range(1, N + 1)],
                axis=0,
            )
            plt.plot(t, y, label=f"N = {N}")
        plt.title("Fourier Series of Saw Function")
        plt.xlabel("t")
        plt.ylabel("y(t)")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Evaluate the Fourier series, representing a square function, by
        using different numbers of terms, i.e., N = [2,6,50]:
        y(t) = 4/𝜋 * sum_{n=1,3,5...}^{N} sin(2n𝜋/T * t)/n
        Plot the results in the range t = [0:2T], where T is the chosen period
        for the square wave."""
        T = 5
        t = np.linspace(0, 2 * T, 1000)
        limits = [2, 6, 50]
        for N in limits:
            y = (
                4
                / np.pi
                * np.sum(
                    [
                        np.sin(2 * n * np.pi / T * t) / n
                        for n in range(1, N + 1, 2)
                    ],
                    axis=0,
                )
            )
            plt.plot(t, y, label=f"N = {N}")
        plt.title("Fourier Series of Square Function")
        plt.xlabel("t")
        plt.ylabel("y(t)")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
