"""Writing scripts"""

import math
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Writing scripts"""

    tasklist: list = []

    @staticmethod
    def matsum(
        matrix_a: list[list[float | int]], matrix_b: list[list[float | int]]
    ) -> list[list[float | int]]:
        """Sum of two matrices."""
        if len(matrix_a) != len(matrix_b):
            raise ValueError("Matrices must have the same number of rows")
        if len(matrix_a[0]) != len(matrix_b[0]):
            raise ValueError("Matrices must have the same number of columns")
        return [
            [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
            for i in range(len(matrix_a))
        ]

    @staticmethod
    def matmat(
        matrix_1: list[list[float | int]], matrix_2: list[list[float | int]]
    ) -> list[list[float | int]]:
        """Multiply two matrices. Return 0 if the sizes are incompatible."""
        if len(matrix_1[0]) != len(matrix_2):
            return [[0]]
        return [
            [
                sum(a * b for a, b in zip(row_A, col_B))
                for col_B in zip(*matrix_2)
            ]
            for row_A in matrix_1
        ]

    @staticmethod
    def mat_op(mat_a: list[list[float]]) -> list[list[float]]:
        """Write a function, MatOp, that receives a square matrix A and
        returns the matrix: T = CD + ED, where matrices C, D and E are the
        lower triangular, the diagonal and the upper triangular parts of A."""
        rows: int = len(mat_a)
        mat_c: list[list[float]] = [[0] * rows for _ in range(rows)]
        mat_d: list[list[float]] = [[0] * rows for _ in range(rows)]
        mat_e: list[list[float]] = [[0] * rows for _ in range(rows)]
        for i in range(rows):
            for j in range(rows):
                if i == j:
                    mat_d[i][j] = mat_a[i][j]
                elif i > j:
                    mat_c[i][j] = mat_a[i][j]
                else:
                    mat_e[i][j] = mat_a[i][j]
        return Task.matsum(
            Task.matmat(mat_c, mat_d), Task.matmat(mat_e, mat_d)
        )

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[float]]]:
        """Write a function, MatOp, that receives a square matrix A and
        returns the matrix: T = CD + ED, where matrices C, D and E are the
        lower triangular, the diagonal and the upper triangular parts of A."""
        mat_a: list[list[float]] = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        return {"mat_a": mat_a, "mat_op": Task.mat_op(mat_a)}

    @staticmethod
    def pipe(length: float, diameter: float, angle: float) -> int:
        """A massless particle is shot within a two-dimensional horizontal
        pipe of length L and diameter D. The shooting angle is q, as depicted
        in the figure below. Every time the particle hits the top or bottom
        walls of the pipe, it bounces forward at the same angle of incidence.
        Write a script, Pipe, to plot the trajectory of the particle within
        the pipe (no need to plot the walls of the pipe) and compute how many
        times the particle hits the walls before exiting the pipe."""
        # hits: int = int(abs(length * math.tan(angle)) / diameter + 0.5)
        # coordinates of bounces
        x_vals: list[float] = [0]
        y_vals: list[float] = [0]
        flip: int = 1 if angle < 0 else 0
        hits: int = 0
        while x_vals[-1] < length:
            x_vals.append(
                x_vals[-1]
                + ((-1) ** (hits + flip) * diameter / 2 - y_vals[-1])
                / math.tan(angle)
            )
            y_vals.append((-1) ** (hits + flip) * diameter / 2)
            # change angle
            angle *= -1
            hits += 1

        plt.plot(x_vals, y_vals)
        plt.axis([0, length, -diameter / 2, diameter / 2])
        plt.show()
        return hits - 1

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int]:
        """A massless particle is shot within a two-dimensional horizontal
        pipe of length L and diameter D. The shooting angle is q, as depicted
        in the figure below. Every time the particle hits the top or bottom
        walls of the pipe, it bounces forward at the same angle of incidence.
        Write a script, Pipe, to plot the trajectory of the particle within
        the pipe (no need to plot the walls of the pipe) and compute how many
        times the particle hits the walls before exiting the pipe."""
        return {"hits": Task.pipe(10, 1, math.pi / 4)}

    @task_to_list(tasklist)
    def task3(self) -> None:
        """The file xaxis.txt contains values of x, within the range -3 and 7,
        non-uniformly distributed. Read in the range and evaluate the series:
        y(x_i) = sum_{n=0}^{10} (-1)^n * x^2n / (2n + 1)!
        for all the values of x in the range.
        Determine the first derivative of the computed y(x) for all the points
        in the given range, apart from the first and the last points, as
        dy(x_i)/dx = (y(x_i+1) - y(x_i-1)) / (x_i+1 - x_i-1).
        Plot the computed y(x) and derivative vs x.
        """
        x_vals: list[float] = []
        y_vals: list[float] = []
        dy_vals: list[float] = []

        with open(
            "year1/finals-18-19/xaxis.txt", "r", encoding="utf-8"
        ) as file:
            for line in file:
                x_vals.append(float(line))

        for x_val in x_vals:
            y_vals.append(
                sum(
                    (-1) ** n * x_val ** (2 * n) / math.factorial(2 * n + 1)
                    for n in range(11)
                )
            )

        for i in range(1, len(x_vals) - 1):
            dy_vals.append(
                (y_vals[i + 1] - y_vals[i - 1])
                / (x_vals[i + 1] - x_vals[i - 1])
            )

        plt.plot(x_vals, y_vals, label="y(x)")
        plt.plot(x_vals[1:-1], dy_vals, label="dy(x)/dx")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("2")
    task.run_tasks()
    assert task.mat_op(
        [
            [1, 2, 3, 4, 5, 6],
            [6, 0, 3, 4, 2, 1],
            [2, 1, 9, 4, 6, 7],
            [3, 0, 8, 4, 6, 5],
            [1, 5, 4, 3, 3, 1],
            [6, 1, 4, 4, 3, 2],
        ]
    ) == [
        [0, 0, 27, 16, 15, 12],
        [6, 0, 27, 16, 6, 2],
        [2, 0, 0, 16, 18, 14],
        [3, 0, 72, 0, 18, 10],
        [1, 0, 36, 12, 0, 2],
        [6, 0, 36, 16, 9, 0],
    ]
    assert task.pipe(2, 0.4, -math.pi / 3) == 9
