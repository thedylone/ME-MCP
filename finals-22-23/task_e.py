"""Task E"""

import os
import numpy as np
import matplotlib.pyplot as plt

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"

# pylint: disable=invalid-name


class Trigonometry:
    """Define a class Trigonometry, with attributes x and unit. Attribute x
    represents a sequence of numbers. Attribute unit is a Boolean variable
    with value True if numbers in x are given in radians and
    with value False if numbers in x are given in degree."""

    def __init__(self, x: list[float], unit: bool) -> None:
        self.x: list[float] = x
        # unit is True if x is in radians, False if x is in degrees
        self.unit: bool = unit

    def cos(self) -> list[float]:
        """Write a method, cos(), to determine the cosine of an object of
        class Trigonometry, taking into consideration if the sequence of
        values are given in radians or degree."""
        if self.unit:
            # x is in radians
            return list(np.cos(self.x))
        # x is in degrees
        # convert to radians
        return list(np.cos(np.radians(self.x)))


def main():
    """Define an object xr of class Trigonometry, containing 100 values,
    equally spaced, in radians, in the range [0:2𝜋] and another object of
    the same class, xd, containing 100 values, equally spaced, in degree,
    in the range [0:360].
    Apply the method cos() to both objects
    and plot the results in two different plots."""
    # create xr, np.linspace() returns 100 evenly spaced numbers from 0 to 2pi
    # set unit to True to indicate that x is in radians
    xr = Trigonometry(list(np.linspace(0, 2 * np.pi, 100)), True)
    # create xd, np.linspace() returns 100 evenly spaced numbers from 0 to 360
    # set unit to False to indicate that x is in degrees
    xd = Trigonometry(list(np.linspace(0, 360, 100)), False)

    # plot xr
    plt.plot(xr.x, xr.cos())
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("cos(x) vs x (radians)")
    plt.show()

    # plot xd
    plt.plot(xd.x, xd.cos())
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("cos(x) vs x (degrees)")
    plt.show()

    # subplots
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(xr.x, xr.cos())
    ax1.set_xlabel("x")
    ax1.set_ylabel("cos(x)")
    ax1.set_title("cos(x) vs x (radians)")
    ax2.plot(xd.x, xd.cos())
    ax2.set_xlabel("x")
    ax2.set_ylabel("cos(x)")
    ax2.set_title("cos(x) vs x (degrees)")
    fig.align_ylabels()
    plt.show()


if __name__ == "__main__":
    main()
