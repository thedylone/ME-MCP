"""Higher order ODEs"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session5.c import fwd_euler_n


class Task(TaskBase):
    """Higher order ODEs
    An ODEs of higher order nth can be decomposed into a set of n first
    order ODEs.
    d^n y/dt^n + a_n-1 d^n-1 y/dt^n-1 + ... + a1 dy/dt + a0 y = b(t)
    This can be achieved by introducing artifical variables:
    dy/dt = w1
    d^2 y/dt^2 = dw1/dt = w2
    ...
    d^n y/dt^n = dw_n-1/dt = - a_n-1 w_n-1 - ... - a2 w2 - a1 w1 - a0 y + b(t)
    The set of first order ODEs, is then made of n equations, with variables
    y, w1, w2, ..., w_n-1."""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self):
        """Damped non-linear motion of a pendulum
        The oscillation of a pendulum of mass m, attached to a
        weightless string, is described by the second order ODE:
        d^2 theta/dt^2 + c/m d theta/dt + g/l sin(theta) = 0
        where c is the damping coefficient, g the gravitational acceleration
        and L the length of the string.
        The pendulum initially is at rest, displaced at an angle theta0.
        Determine the motion of the pendulum, theta(t), for the first initlal
        15 seconds, with initial condition theta0 = 𝜋/4. (Use FwEulerN with
        Δt = 0.005s).
        Plot into two subplots: the displacement y(t) vs time t, and, the
        velocity w1(t) vs time t. Use a mass of 0.5Kg and a string L = 1m.
        Observe the difference between the swinging within a dry place
        (c = 0.05Ns/m) and within a humid viscous environment (c = 0.18Ns/m).
        """
        t0 = 0
        t_end = 4
        h = 0.005
        y0 = np.array([np.pi / 4, 0])
        m = 0.5
        length = 1
        c1 = 0.05
        c2 = 0.18
        g = 9.81

        def f1(_t, _w1: float, w2: float) -> float:
            return w2

        def f2_wrapper(c: float) -> Callable:
            def f2(_t, w1: float, w2: float) -> float:
                return -g / length * np.sin(w1) - c / m * w2

            return f2

        t1, y1 = fwd_euler_n([f1, f2_wrapper(c1)], t0, y0, t_end, h)
        t2, y2 = fwd_euler_n([f1, f2_wrapper(c2)], t0, y0, t_end, h)
        _fig, (ax1, ax2) = plt.subplots(2)
        ax1.plot(t1, y1[:, 0], label="c = 0.05Ns/m")
        ax1.plot(t2, y2[:, 0], label="c = 0.18Ns/m")
        ax1.legend()
        ax1.set_title("Displacement")
        ax2.plot(t1, y1[:, 1], label="c = 0.05Ns/m")
        ax2.plot(t2, y2[:, 1], label="c = 0.18Ns/m")
        ax2.legend()
        ax2.set_title("Velocity")
        plt.show()

    @task_to_list(tasklist)
    def task2(self):
        """Coupled spring-mass systems
        The system in Figure D2 consists of three masses and four springs,
        fixed between two rigid walls. The masses are 𝑚1 𝑚2 and 𝑚3; the
        springs have Young modulus K1 K2 and K3; the relaxed length of each
        spring is L1 L2 L3 and L4. The displacement of the three masses is
        described by the set of second order ODEs:
        m1 d^2 x1/dt^2 = -k1(x1-L1) + k2(x2-x1-L2)
        m2 d^2 x2/dt^2 = -k2(x2-x1-L2) + k3(x3-x2-L3)
        m3 d^2 x3/dt^2 = -k3(x3-x2-L3) + k4(L1+L2+L3-x3)
        Calculate and plot the displacement of the three masses x1(t), x2(t)
        and x3(t), for various values of the system parameters and initial
        conditions of your choice."""
        t0 = 0
        t_end = 100
        h = 0.01
        l1 = 1
        l2 = 1
        l3 = 1
        l4 = 1
        k1 = 1
        k2 = 1
        k3 = 1
        k4 = 1
        m1 = 1
        m2 = 1
        m3 = 1
        # x1, v1, x2, v2, x3, v3
        x0 = np.array([1, 0, 1.5, 0, 3, 0])

        def f1(_t, _x1, v1, _x2, _v2, _x3, _v3) -> float:
            return v1

        def f2(_t, x1, _v1, x2, _v2, _x3, _v3) -> float:
            return (-k1 * (x1 - l1) + k2 * (x2 - x1 - l2)) / m1

        def f3(_t, _x1, _v1, x2, v2, _x3, _v3) -> float:
            return v2

        def f4(_t, x1, _v1, x2, _v2, x3, _v3) -> float:
            return (-k2 * (x2 - x1 - l2) + k3 * (x3 - x2 - l3)) / m2

        def f5(_t, _x1, _v1, _x2, _v2, _x3, v3) -> float:
            return v3

        def f6(_t, x1, _v1, x2, _v2, x3, _v3) -> float:
            return (-k3 * (x3 - x2 - l3) + k4 * (l1 + l2 + l3 - x3)) / m3

        t, y = fwd_euler_n([f1, f2, f3, f4, f5, f6], t0, x0, t_end, h)
        _fig, (ax1, ax2, ax3) = plt.subplots(3)
        ax1.plot(t, y[:, 0])
        ax1.set_title("x1")
        ax2.plot(t, y[:, 2])
        ax2.set_title("x2")
        ax3.plot(t, y[:, 4])
        ax3.set_title("x3")
        plt.show()

    @task_to_list(tasklist)
    def task3(self):
        """Motion of a double pendulum
        The dynamics of the double pendulum, in an ideal viscous free
        environment, is described by the set of ODEs (slide 299)
        Calculate and plot the displacement of the two masses
        𝜃1(t) and 𝜃2(t) for:
        L1 = 1m, L2 = 0.5m
        m1 = 1kg and 2kg, m2 = 1kg
        𝜃1(0) = 𝜋/4, 𝜃2(0) = -𝜋/4
        Zero initial velocities
        Time step h = 0.002
        t_end = 40s
        """
        l1 = 1
        l2 = 0.5
        m1 = 1
        m2 = 1
        g = 9.81
        t0 = 0
        t_end = 40
        h = 0.002
        y0 = np.array([np.pi / 4, 0, -np.pi / 4, 0])

        def f1(_t, _w1, w2, _w3, w4) -> float:
            return w2

        def f2(_t, w1, w2, w3, w4) -> float:
            return (
                m2 * g * np.sin(w3) * np.cos(w1 - w3)
                - m2
                * np.sin(w1 - w3)
                * (l1 * w2**2 * np.cos(w1 - w3) + l2 * w4**2)
                - (m1 + m2) * g * np.sin(w1)
            ) / (l1 * (m1 + m2 * np.sin(w1 - w3) ** 2))

        def f3(_t, _w1, w2, _w3, w4) -> float:
            return w4

        def f4(_t, w1, w2, w3, w4) -> float:
            return (
                (m1 + m2)
                * (
                    l1 * w2**2 * np.sin(w1 - w3)
                    + g * np.sin(w1) * np.cos(w1 - w3)
                    - g * np.sin(w3)
                )
                + m2 * l2 * w4**2 * np.sin(w1 - w3) * np.cos(w1 - w3)
            ) / (l2 * (m1 + m2 * np.sin(w1 - w3) ** 2))

        t, y = fwd_euler_n([f1, f2, f3, f4], t0, y0, t_end, h)
        _fig, (ax1, ax2) = plt.subplots(2)
        ax1.plot(t, y[:, 0])
        ax1.set_title("theta1")
        ax2.plot(t, y[:, 2])
        ax2.set_title("theta2")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
