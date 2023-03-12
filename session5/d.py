"""Warfare: the shooting videogame"""

import random
import math
import time
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Warfare: the shooting videogame"""

    tasklist: list = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.target: tuple[float, float] = (random.random(), random.random())
        self.radius: float = 0.01
        self.trajectory_y: list[float] = []
        self.trajectory_x: list[float] = []
        self.angle: float = 0
        self.vel: float = 0
        self.failed: bool = False
        self.failed_twice: bool = False
        self.fig: matplotlib.figure.Figure
        self.axes: plt.Axes
        self.anim: FuncAnimation

    def check_if_hit(self, x_pos: float, y_pos: float) -> bool:
        """Check if the shot hit the target."""
        dist: float = (x_pos - self.target[0]) ** 2 + (
            y_pos - self.target[1]
        ) ** 2
        return dist <= self.radius**2

    def update(self, i) -> None:
        """Update the plot."""
        if self.failed:
            if self.failed_twice:
                time.sleep(1)
                self.anim.event_source.stop()
                plt.close()
            else:
                self.failed_twice = True
            return

        x_pos: float = i * 0.01
        y_pos: float = x_pos * math.tan(self.angle) - (
            0.5 * 9.81 * x_pos**2
        ) / (self.vel**2 * math.cos(self.angle) ** 2)
        self.trajectory_x.append(x_pos)
        self.trajectory_y.append(y_pos)
        self.axes.clear()
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(0, 1)
        self.axes.set_aspect("equal")
        self.axes.plot(self.trajectory_x, self.trajectory_y, color="r")
        self.axes.add_artist(plt.Circle(self.target, self.radius, color="g"))
        # show selected angle and velocity
        self.axes.text(
            0.05,
            0.95,
            f"angle: {math.degrees(self.angle):.2f}°",
            ha="left",
            va="top",
            size=10,
        )
        self.axes.text(
            0.05,
            0.90,
            f"velocity: {self.vel:.2f} m/s",
            ha="left",
            va="top",
            size=10,
        )
        if self.check_if_hit(x_pos, y_pos):
            self.axes.text(0.5, 0.5, "HIT!", ha="center", va="center", size=20)
            self.anim.event_source.stop()
        elif y_pos < 0 or x_pos > 1:
            self.axes.text(
                0.5, 0.5, "MISS!", ha="center", va="center", size=20
            )
            self.failed = True
            # self.anim.event_source.stop()

    def attempt(self) -> bool:
        """Create the target and asksthe user to play until the target is hit.
        For every attempt, plot the war scenery
        (i.e. the trajectory and the target)."""
        # reset
        self.trajectory_x = []
        self.trajectory_y = []
        self.failed = False
        self.failed_twice = False

        self.fig, self.axes = plt.subplots()
        self.anim = FuncAnimation(self.fig, self.update, interval=10)
        plt.show()
        return not self.failed

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Create the target and asksthe user to play until the target is hit.
        For every attempt, plot the war scenery
        (i.e. the trajectory and the target)."""
        self.fig, self.axes = plt.subplots()
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(0, 1)
        self.axes.set_aspect("equal")
        self.axes.add_artist(plt.Circle(self.target, self.radius, color="g"))
        plt.show()
        while True:
            self.angle = math.radians(float(input("Enter the angle: ")))
            self.vel = float(input("Enter the velocity: "))
            self.attempt()
            if self.failed:
                print("You missed!")
            else:
                print("You hit the target!")
                break


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    task.target = (0.3, 0.7)
    task.radius = 0.01
    combinations: list[tuple[float, float]] = [
        (73, 21),
        (60, 21),
        (67, 21),
        (63, 21),
    ]
    for angle, vel in combinations:
        task.angle = math.radians(angle)
        task.vel = vel
        if task.attempt():
            print(f"Angle: {angle}°, velocity: {vel} m/s")
            break
