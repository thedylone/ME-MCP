"""Warfare: the shooting videogame"""

import random
import matplotlib.pyplot as plt
import math
import time

from matplotlib.animation import FuncAnimation
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Warfare: the shooting videogame"""

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.target = (random.random(), random.random())
        self.radius = 0.01
        self.trajectory_y = []
        self.trajectory_x = []
        self.angle = 0
        self.vel = 0
        self.failed = False
        self.failed_twice = False

    def check_if_hit(self, x, y):
        """Check if the shot hit the target."""
        distance = (x - self.target[0]) ** 2 + (y - self.target[1]) ** 2
        return distance <= self.radius**2

    def update(self, i):
        """Update the plot."""
        if self.failed:
            if self.failed_twice:
                time.sleep(1)
                self.anim.event_source.stop()
                plt.close()
            else:
                self.failed_twice = True
            return

        x = i * 0.01
        y = x * math.tan(self.angle) - (0.5 * 9.81 * x**2) / (
            self.vel**2 * math.cos(self.angle) ** 2
        )
        self.trajectory_x.append(x)
        self.trajectory_y.append(y)
        self.ax.clear()
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect("equal")
        self.ax.plot(self.trajectory_x, self.trajectory_y, color="r")
        self.ax.add_artist(plt.Circle(self.target, self.radius, color="g"))
        # show selected angle and velocity
        self.ax.text(
            0.05,
            0.95,
            f"angle: {math.degrees(self.angle):.2f}°",
            ha="left",
            va="top",
            size=10,
        )
        self.ax.text(
            0.05,
            0.90,
            f"velocity: {self.vel:.2f} m/s",
            ha="left",
            va="top",
            size=10,
        )
        if self.check_if_hit(x, y):
            self.ax.text(0.5, 0.5, "HIT!", ha="center", va="center", size=20)
            self.anim.event_source.stop()
        elif y < 0 or x > 1:
            self.ax.text(0.5, 0.5, "MISS!", ha="center", va="center", size=20)
            self.failed = True
            # self.anim.event_source.stop()

    def attempt(self):
        """Create the target and asksthe user to play until the target is hit.
        For every attempt, plot the war scenery
        (i.e. the trajectory and the target)."""
        # reset
        self.trajectory_x = []
        self.trajectory_y = []
        self.failed = False
        self.failed_twice = False

        self.angle = math.radians(float(input("Enter the angle: ")))
        self.vel = float(input("Enter the velocity: "))
        self.fig, self.ax = plt.subplots()
        self.anim = FuncAnimation(self.fig, self.update, interval=10)
        plt.show()

    @task_to_list(tasklist)
    def task1(self):
        """Create the target and asksthe user to play until the target is hit.
        For every attempt, plot the war scenery
        (i.e. the trajectory and the target)."""
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect("equal")
        self.ax.add_artist(plt.Circle(self.target, self.radius, color="g"))
        plt.show()
        while True:
            self.attempt()
            if self.failed:
                print("You missed!")
            else:
                print("You hit the target!")
                break


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()
