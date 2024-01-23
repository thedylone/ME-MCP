"""The river Thames basin in London"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session2.c import trapz


class Task(TaskBase):
    """The river Thames basin in London
    The file Thames.txt contains N = 72 spatial coordinates (xi,yi) of the
    north and south banks of the river Thames (units in meters), within the
    Central London region (between Chiswick and Woolwich).
    The nodal points are organised in the file within N = 72 lines,
    as follows:
    x North Bank | y North Bank | x South Bank | y South Bank
    ------------ | ------------ | ------------ | ------------
    xn0 | yn0 | xs0 | ys0
    xn1 | yn1 | xs1 | ys1
    ... | ... | ... | ...
    xn(N-1) | yn(N-1) | xs(N-1) | ys(N-1)"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.north_bank: np.ndarray = np.ndarray((0, 2))
        self.south_bank: np.ndarray = np.ndarray((0, 2))

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Read in the data from the files and plot the two banks of the river
        together, to visualise the shape of the basin."""
        with open("year2/session2/Thames.txt", "r", encoding="utf-8") as file:
            for line in file:
                pts: list[str] = line.split(",")
                self.north_bank = np.append(
                    self.north_bank,
                    np.array([[float(pts[0]), float(pts[1])]]),
                    axis=0,
                )
                self.south_bank = np.append(
                    self.south_bank,
                    np.array([[float(pts[2]), float(pts[3])]]),
                    axis=0,
                )
        plt.plot(self.north_bank[:, 0], self.north_bank[:, 1])
        plt.plot(self.south_bank[:, 0], self.south_bank[:, 1])
        plt.axis("equal")
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> dict[str, float]:
        """Compute the surface occupied by the basin in km^2."""
        north_area: float = trapz(self.north_bank[:, 0], self.north_bank[:, 1])
        south_area: float = trapz(self.south_bank[:, 0], self.south_bank[:, 1])
        area: float = (north_area - south_area) / 1e6
        return {"area": area}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
