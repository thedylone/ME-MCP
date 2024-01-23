"""Simpson Integration and Adaptive Simpson Integration"""

import numpy as np

from helpers.task import TaskBase, task_to_list


def simpson(h: float, yn: list[float] | np.ndarray) -> float:
    """Simpson integration"""
    return sum(
        h / 3 * (yn[i] + 4 * yn[i + 1] + yn[i + 2])
        for i in range(0, len(yn) - 2, 2)
    )


class Task(TaskBase):
    """Simpson Integration and Adaptive Simpson Integration"""

    tasklist: list = []

    def f(self, x: np.ndarray) -> np.ndarray:
        """Function to integrate"""
        return 1 / (1 + x**2)

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function, Simpson, to integrate over a uniformly
        distributed set of nodal point.
        Compute the integral:
        int_0^1 1/(1+x^2) dx
        with steps dx = 0.01 and dx and 0.001"""
        steps = [0.01, 0.001]
        for h in steps:
            x = np.arange(0, 1 + h, h)
            y = self.f(x)
            integral = simpson(h, y)
            print(f"Integral for h = {h} is {integral}")

    @task_to_list(tasklist)
    def task2(self):
        """Write an adaptive script to integrate numerically a given function
        f(x), over a prescribed domain, until a desired tolerance is achieved.
        Compute the above integral, with tolerances 𝜀 = 10^-2 and 𝜀 = 10^-6.
        Note the analytical solution:
        int 1/(1+x^2) dx = arctan(x) + C"""
        tolerances = [1e-2, 1e-6]
        for tolerance in tolerances:
            nodes = 1
            integral = 0
            error = float("inf")
            while error > tolerance:
                nodes *= 2
                x = np.linspace(0, 1, nodes + 1)
                y = self.f(x)
                new = simpson(1 / nodes, y)
                # error = abs(integral - np.arctan(1))
                error = 1 / 15 * (abs(integral - new))
                integral = new
            print(f"𝜀 = {tolerance}: {integral} with {nodes+1} nodes")


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
