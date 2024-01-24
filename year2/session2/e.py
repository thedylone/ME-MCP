"""Multiple integrals (with given analytical function): volume of the dome of
the Royal Albert Hall"""

import numpy as np
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from year2.session2.c import trapz


class Task(TaskBase):
    """Multiple integrals (with given analytical function): volume of the dome
    of the Royal Albert Hall
    A two-dimensional integral has the form of:
    I = int int z(x,y)dA = int_a^b dx int_m(x)^p(x) z(x,y)dy = int_a^b G(x)dx
    where A is the domain of integration.
    The two-dimensional integral can be computed numerically, by applying the
    trapezium method twice. Firstly, the integral
    G(x) = int_m(x)^p(x) z(x,y)dy
    is computed for all values of x. Then the total integral is obtained as:
    I = int_a^b G(x)dx"""

    tasklist: list = []

    @staticmethod
    def double_integral(dx: float) -> float:
        """Numerical integration of a double integral"""
        h: float = 25
        a: float = 67
        b: float = 56
        x_domain: np.ndarray = np.linspace(-a, a, int(2 * a / dx) + 1)
        g_x: np.ndarray = np.zeros(len(x_domain))
        for i, x in enumerate(x_domain):
            limit: float = b * np.sqrt(1 - (x / a) ** 2)
            y_domain: np.ndarray = np.linspace(
                -limit, limit, int(2 * limit / dx) + 1
            )
            z_values: np.ndarray = h**2 * (
                1 - (x / a) ** 2 - (y_domain / b) ** 2
            )
            z_values[z_values < 0] = 0
            z_values = np.sqrt(z_values)
            g_x[i] = trapz(y_domain, z_values)
        return trapz(x_domain, g_x)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """The dome of the Royal Albert Hall is described by the ellipsoid
        function:
        z(x,y) = sqrt(h^2 * (1 - x^2/a^2 - y^2/b^2))
        with height h = 25m.
        The base of dome A (domain of integration) is described by an ellipse A
        x^2/a^2 + y^2/b^2 = 1, with major and minor axes a = 67m and b = 56m.
        Determine the numerical value of the dome volume, by discretising the
        domain A with a mesh of equidistant intervals both along the x and y
        axes, i.e. dx = dy = 0.5m."""
        volume: float = Task.double_integral(0.5)
        return {"volume": volume}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, float]:
        """Compare the numerical value against the analytical value. Repeat
        the calculation for a mesh with elements size dx = dy = 0.05m."""
        volume: float = Task.double_integral(0.05)
        return {"volume": volume, "analytical": 196454}

    @task_to_list(tasklist)
    def task3(self):
        """Plot the function z(x,y)"""
        h: float = 25
        a: float = 67
        b: float = 56
        x_domain: np.ndarray = np.arange(-a, a + 0.05, 0.05)
        y_domain: np.ndarray = np.arange(-b, b + 0.05, 0.05)
        matrix = np.meshgrid(x_domain, y_domain)
        z_values: np.ndarray = h**2 * (
            1 - (matrix[0] / a) ** 2 - (matrix[1] / b) ** 2
        )
        z_values[z_values < 0] = 0
        z_values = np.sqrt(z_values)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(matrix[0], matrix[1], z_values)
        plt.show()


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
    print(task.double_integral(0.6))
