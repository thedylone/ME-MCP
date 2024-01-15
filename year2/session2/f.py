"""Multiple integrals (with given nodes): volume of an aerofoil"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from year2.session2.c import Task as TaskC


class Task(TaskBase):
    """Multiple integrals (with given nodes): volume of an aerofoil
    The file Aerofoil.txt contains the nodal coordinates of an aerofoil.
    The aerofoil is defined by two surfaces Zt(x,y) and Zb(x,y), each defining
    the top surface and the bottom surface of the aerofoil, respectively. The
    domain has been discretised with a mesh of dimension (Nx = 100, Ny = 15).
    Nodes in the file are organised within Nx ∙ Ny = 1500 lines, as follows:
    x | y | Zt(x,y) | Zb(x,y)
    --|---|---------|---------
    x0 | y0 | Zt(x0,y0) | Zb(x0,y0)
    x1 | y0 | Zt(x1,y0) | Zb(x1,y0)
    ... | ... | ... | ...
    x(Nx-1) | y0 | Zt(x(Nx-1),y0) | Zb(x(Nx-1),y0)
    x0 | y1 | Zt(x0,y1) | Zb(x0,y1)
    x1 | y1 | Zt(x1,y1) | Zb(x1,y1)
    ... | ... | ... | ...
    x(Nx-1) | y(Ny-1) | Zt(x(Nx-1),y(Ny-1)) | Zb(x(Nx-1),y(Ny-1))"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.nx: int = 100
        self.ny: int = 15
        self.x_values: np.ndarray = np.zeros(self.nx)
        self.y_values: np.ndarray = np.zeros(self.ny)
        self.top: np.ndarray = np.ndarray((self.nx, self.ny))
        self.bottom: np.ndarray = np.ndarray((self.nx, self.ny))

    @task_to_list(tasklist)
    def task1(self):
        """Compute the volume of the aerofoil"""
        with open(
            "year2/session2/Aerofoil.txt", "r", encoding="utf-8"
        ) as file:
            lines: list[str] = file.readlines()
        g_x: np.ndarray = np.zeros(self.ny)
        for j in range(0, self.nx * self.ny, self.nx):
            x_vals: np.ndarray = np.zeros(self.nx)
            z_vals: np.ndarray = np.zeros(self.nx)
            self.y_values[j // self.nx] = float(lines[j].split(",")[1])
            for i, line in enumerate(lines[j : j + self.nx]):
                pts: list[str] = line.split(",")
                x_vals[i] = float(pts[0])
                self.x_values[i] = float(pts[0])
                self.top[i, j // self.nx] = float(pts[2])
                self.bottom[i, j // self.nx] = float(pts[3])
                z_vals[i] = float(pts[2]) - float(pts[3])
            g_x[j // self.nx] = TaskC.trapz(x_vals, z_vals)
        volume: float = TaskC.trapz(self.y_values, g_x)
        return {"volume": volume}

    @task_to_list(tasklist)
    def task2(self):
        """Plot the aerofoil."""
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        x_mesh, y_mesh = np.meshgrid(self.x_values, self.y_values)
        ax.plot_surface(
            x_mesh, y_mesh, self.top, cmap="viridis", edgecolor="none"
        )
        ax.plot_surface(
            x_mesh, y_mesh, self.bottom, cmap="viridis", edgecolor="none"
        )
        plt.show()


if __name__ == "__main__":
    task: Task = Task("F")
    task.run_tasks()
