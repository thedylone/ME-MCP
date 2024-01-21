"""Heat transfer in a nuclear fuel rod"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

from year2.session6.b import ode_bc


class Task(TaskBase):
    """Heat transfer in a nuclear fuel rod
    The fuel rod of a nuclear reactor is a cylindrical structure with the fuel
    contained within a metal cladding. The heat is generated by the nuclear
    reaction in the fuel region and conducted, through the thickness of the
    cladding, to the outer surface of the cladding. Outside the cladding,
    cooling occurs with flowing water at temperature Tw = 473 K through
    convective heat transfer (heat transfer coefficient h = 6 * 10^4).
    The temperature distribution within the cladding is determined by the ODE:

    1/r d/dr (rk dT/dr) = - 10^8 (e^(-r/R)) / r

    in the region of the cladding R < r < R + w, with boundary conditions:

    dT/dr (R) = - 6.32 * 10^5 / k and dT/dr (R + w) = - h/k (T(R + w) - Tw)

    The thermal conductivity of the metal is k = 16.75. The dimensions of the
    rod are R = 15 mm and w = 3 mm."""

    tasklist: list = []

    Tw = 473
    h = 6e4
    k = 16.75
    R = 15e-3
    w = 3e-3

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Compute the temperature distribution within the metal cladding,
        with N = 50."""

        def ode(r: float) -> tuple:
            return 1 / r, 0, -1e8 * np.exp(-r / self.R) / (r * self.k)

        x, y = ode_bc(
            ode,
            self.R,
            self.R + self.w,
            -6.32e5 / self.k,
            self.h / self.k * self.Tw,
            50,
            np.array([1, 0, 1, self.h / self.k]),
        )
        plt.plot(x, y)
        plt.show()
        # print value at r = 15.6e-3
        print(x[10], y[10])


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
