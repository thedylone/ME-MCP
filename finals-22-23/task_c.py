"""Task C"""

import os
import random
import matplotlib.pyplot as plt

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


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
    pos = 0
    steps = 0
    x_coords: list[int] = [0]
    y_coords: list[int] = [0]
    while pos < 100:
        delta: int = random.randint(1, 10)  # between 1 to 10 ->?
        pos += delta
        x_coords.append(pos)
        y_coords.append(y_coords[-1])
        x_coords.append(x_coords[-1])
        y_coords.append(pos)
        steps += 1

    print(f"Super Mario walked {pos} units horizontally.")
    print(f"Super Mario took {steps} steps to reach the winning line.")
    plt.plot(x_coords, y_coords)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Super Mario's path to the winning line")
    plt.axhline(y=100, color="r")
    plt.show()


if __name__ == "__main__":
    main()
