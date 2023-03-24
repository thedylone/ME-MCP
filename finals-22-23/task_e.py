"""Task E"""

import os
import numpy as np
import matplotlib.pyplot as plt

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


class Trigonometry:
    def __init__(self, x: list[float], unit: bool) -> None:
        self.x: list[float] = x
        # unit is True if x is in radians, False if x is in degrees
        self.unit: bool = unit

    def cos(self) -> list[float]:
        """Write a method, cos(), to determine the cosine of an object of
        class Trigonometry, taking into consideration if the sequence of
        values are given in radians or degree."""
        if self.unit:
            return list(np.cos(self.x))
        return list(np.cos(np.radians(self.x)))


def main():
    """Define an object xr of class Trigonometry, containing 100 values,
    equally spaced, in radians, in the range [0:2𝜋] and another object of
    the same class, xd, containing 100 values, equally spaced, in degree,
    in the range [0:360].
    Apply the method cos() to both objects
    and plot the results in two different plots."""
    xr = Trigonometry(list(np.linspace(0, 2 * np.pi, 100)), True)
    xd = Trigonometry(list(np.linspace(0, 360, 100)), False)

    plt.plot(xr.x, xr.cos())
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("cos(x) vs x (radians)")
    plt.show()

    plt.plot(xd.x, xd.cos())
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("cos(x) vs x (degrees)")
    plt.show()


if __name__ == "__main__":
    main()
