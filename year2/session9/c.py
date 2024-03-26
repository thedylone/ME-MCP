"""Interpolation over a triangulated mesh"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Interpolation over a triangulated mesh

    An electrical circular cooking hob, with radius r = 50mm, laying in the
    x y plane, is represented with an unstructured mesh grid of triangular
    elements. The spatial temperature distribution across the hob is provided
    for each node of the mesh, in the file Hob.Temperature.txt."""

    tasklist: list = []
    hob_elements: np.ndarray = np.zeros((0, 3), dtype=int)
    """list of hob triangle elements, of three node indices"""
    hob_nodes: np.ndarray = np.zeros((0, 3), dtype=float)
    """list of hob nodes, of x, y, z coordinates"""
    hob_temps: np.ndarray = np.zeros((0, 1), dtype=float)
    """list of hob nodal temperatures"""
    teapot_elements: np.ndarray = np.zeros((0, 3), dtype=int)
    """list of teapot triangle elements, of three node indices"""
    teapot_nodes: np.ndarray = np.zeros((0, 3), dtype=float)
    """list of teapot nodes, of x, y, z coordinates"""

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str]:
        """Read in the triangled mesh grid, from the two files
        Hob.Elements.txt and Hob.Nodes.txt, containing the triangle elements
        and the discrete nodes of the circular hob, respectively."""
        self.hob_elements = np.loadtxt(
            "year2/session9/Hob.Elements.txt", delimiter=",", dtype=int
        )
        self.hob_nodes = np.loadtxt(
            "year2/session9/Hob.Nodes.txt", delimiter=","
        )
        return {"quiz": "Triangles read successfully"}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, str]:
        """Read in the file Hob.Temperatures.txt, containing the nodal
        temperature distribution."""
        self.hob_temps = np.loadtxt("year2/session9/Hob.Temperatures.txt")
        return {"quiz": "Temperatures read successfully"}

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Plot the mesh grid: both the elements and the nodes."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_trisurf(
            self.hob_nodes[:, 0],
            self.hob_nodes[:, 1],
            self.hob_nodes[:, 2],
            triangles=self.hob_elements,
            cmap="viridis",
            edgecolor="none",
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.scatter(
            self.hob_nodes[:, 0],
            self.hob_nodes[:, 1],
            self.hob_nodes[:, 2],
            c=self.hob_temps,
            cmap="viridis",
        )

        plt.show()

    @task_to_list(tasklist)
    def task4(self) -> None:
        """A tea pot is positioned on top of the hob. The tea pot is also
        represented with a set of unstructured triangular meshes, stored in
        files TeaPot.Elements.txt and TeaPot.Nodes.txt.
        The discrete nodes at the base of the teapot (z = 0) do not correspond
        necessarily to the nodes of the discrete hob.

        For each nodal point at the base of the teapot (z = 0):
        Determine the corresponding triangular element of the hob mesh,
        containing the nodal point of the teapot.
        By making use of the hob temperatures at the three nodal points of the
        embedding element determined in 1), interpolate the temperature of the
        teapot at the nodal point under consideration."""
        self.teapot_elements = (
            np.loadtxt(
                "year2/session9/TeaPot.Elements.txt", delimiter=",", dtype=int
            )
            - 1
        )
        self.teapot_nodes = np.loadtxt(
            "year2/session9/TeaPot.Nodes.txt", delimiter=","
        )
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_trisurf(
            self.teapot_nodes[:, 0],
            self.teapot_nodes[:, 1],
            self.teapot_nodes[:, 2],
            triangles=self.teapot_elements,
            cmap="viridis",
            edgecolor="none",
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()

    @task_to_list(tasklist)
    def task5(self) -> None:
        """For each nodal point at the base of the teapot (z = 0):
        Determine the corresponding triangular element of the hob mesh,
        containing the nodal point of the teapot.
        By making use of the hob temperatures at the three nodal points of the
        embedding element determined in 1), interpolate the temperature of the
        teapot at the nodal point under consideration."""
        teapot_temps: np.ndarray = np.zeros((len(self.teapot_nodes), 1))
        count = 0
        for i, node in enumerate(self.teapot_nodes):
            if node[2] != 0:
                continue
            for element in self.hob_elements:
                A = self.hob_nodes[element][:, :2]
                alpha, beta, gamma = np.linalg.solve(
                    np.array([*A.T, [1, 1, 1]]), [node[0], node[1], 1]
                )
                if alpha < 0 or beta < 0 or gamma < 0:
                    continue
                teapot_temps[i] = (
                    alpha * self.hob_temps[element[0]]
                    + beta * self.hob_temps[element[1]]
                    + gamma * self.hob_temps[element[2]]
                )
                count += 1

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_trisurf(
            self.teapot_nodes[:, 0],
            self.teapot_nodes[:, 1],
            self.teapot_nodes[:, 2],
            triangles=self.teapot_elements,
            cmap="viridis",
            edgecolor="none",
            alpha=0.5,
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.scatter(
            self.teapot_nodes[:, 0],
            self.teapot_nodes[:, 1],
            self.teapot_nodes[:, 2],
            c=teapot_temps,
            cmap="viridis",
        )

        plt.show()

        # plot with hob
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_trisurf(
            self.hob_nodes[:, 0],
            self.hob_nodes[:, 1],
            self.hob_nodes[:, 2],
            triangles=self.hob_elements,
            cmap="viridis",
            edgecolor="none",
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.scatter(
            self.hob_nodes[:, 0],
            self.hob_nodes[:, 1],
            self.hob_nodes[:, 2],
            c=self.hob_temps,
            cmap="viridis",
        )
        ax.plot_trisurf(
            self.teapot_nodes[:, 0],
            self.teapot_nodes[:, 1],
            self.teapot_nodes[:, 2],
            triangles=self.teapot_elements,
            cmap="viridis",
            edgecolor="none",
            alpha=0.5,
        )
        ax.scatter(
            self.teapot_nodes[:, 0],
            self.teapot_nodes[:, 1],
            self.teapot_nodes[:, 2],
            c=teapot_temps,
            cmap="viridis",
        )
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
