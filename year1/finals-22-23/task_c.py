"""Task C"""

import os
import random
import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


class Task(TaskBase):
    """Task C"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """In a videogame, the character Super Mario is trying to reach the
        winning line by moving with a zig-zag motion only. Super Mario is
        initially located at the starting position (x = 0, y = 0), and needs to
        reach the winning line located at y = 100, Figure 3. Super Mario moves
        with incremental steps. At each step, he moves firstly horizontally,
        by a distance dx, where dx is an integer random number between 1 and
        10, and then vertically by a distance dy = dx. Write a script to keep
        Super Mario moving, until he reaches/exceeds the winning line.
        Calculate the horizontal distance D walked through
        and how many steps Super Mario needed to win. Plot the zig-zag path
        taken by Super Mario to reach the winning line."""
        # as x and y are equal at the end of a step, only one variable needed
        pos = 0
        # track the number of steps taken
        steps = 0
        # track the x and y coordinates for plotting
        coords: list[tuple[int, int]] = [(0, 0)]
        while pos < 100:  # while below the winning line
            # if between 1 and 10 is inclusive of 1 and 10
            delta: int = random.randint(1, 10)
            # else if between 1 and 10 is exclusive of 1 and 10
            # delta: int = random.randint(2, 9)
            # step horizontally
            coords.append((pos + delta, pos))
            # step vertically
            coords.append((pos + delta, pos + delta))
            # update position
            pos += delta
            # increment steps
            steps += 1

        print(f"Super Mario walked {pos} units horizontally.")
        print(f"Super Mario took {steps} steps to reach the winning line.")
        # zip(*coords) unpacks the list of tuples into two lists: x and y
        # then unpack for plt.plot
        plt.plot(*zip(*coords))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Super Mario's path to the winning line")
        plt.axhline(y=100, color="r")
        plt.show()


def main() -> None:
    """In a videogame, the character Super Mario is trying to reach the
    winning line by moving with a zig-zag motion only. Super Mario is
    initially located at the starting position (x = 0, y = 0), and needs to
    reach the winning line located at y = 100, Figure 3. Super Mario moves with
    incremental steps. At each step, he moves firstly horizontally,
    by a distance dx, where dx is an integer random number between 1 and 10,
    and then vertically by a distance dy = dx. Write a script to keep
    Super Mario moving, until he reaches/exceeds the winning line.
    Calculate the horizontal distance D walked through
    and how many steps Super Mario needed to win.
    Plot the zig-zag path taken by Super Mario to reach the winning line."""
    # since x and y are equal at the end of a step, only one variable is needed
    pos = 0
    # track the number of steps taken
    steps = 0
    # track the x and y coordinates for plotting
    coords: list[tuple[int, int]] = [(0, 0)]
    while pos < 100:  # while below the winning line
        # if between 1 and 10 is inclusive of 1 and 10
        delta: int = random.randint(1, 10)
        # else if between 1 and 10 is exclusive of 1 and 10
        # delta: int = random.randint(2, 9)
        # step horizontally
        coords.append((pos + delta, pos))
        # step vertically
        coords.append((pos + delta, pos + delta))
        # update position
        pos += delta
        # increment steps
        steps += 1

    print(f"Super Mario walked {pos} units horizontally.")
    print(f"Super Mario took {steps} steps to reach the winning line.")
    # zip(*coords) unpacks the list of tuples into two lists: x and y
    # then unpack for plt.plot
    plt.plot(*zip(*coords))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Super Mario's path to the winning line")
    plt.axhline(y=100, color="r")
    plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
