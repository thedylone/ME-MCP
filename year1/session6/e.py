"""Experimental analysis"""

import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Experimental analysis"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[float] | float]:
        """The performance of a boiling system has been monitored with daily
        measurements of its water temperature. Measurements were performed
        throughout ten different days. Each day, measurements were taken at
        every hour, for a total of 24 data per day. The data measured are
        stored sequentially, one per line, in the file Temperatures.txt.
        Compute the average temperature, Tav, of the water for each day,
        and plot the result in a graph with Tav vs day.
        Compute also the maximum and minimum temperatures overall."""
        averages: list[float] = []
        maximum: float = float("-inf")
        minimum: float = float("inf")
        with open(
            "year1/session6/Temperatures.txt", "r", encoding="utf-8"
        ) as file:
            i: int = 0
            running: float = 0
            for line in file:
                i += 1
                running += float(line)
                if i % 24 == 0:
                    averages.append(running / 24)
                    running = 0
                maximum = max(maximum, float(line))
                minimum = min(minimum, float(line))

        plt.plot(averages)
        plt.show()
        return {"average": averages, "maximum": maximum, "minimum": minimum}


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
