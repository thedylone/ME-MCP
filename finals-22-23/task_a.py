"""Task A"""

import os
import math
import matplotlib.pyplot as plt

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


def series(limit: int) -> float:
    """Calculate the sries
    S = sum_{j=-N}^{N+2} ( 1/j! sum_{k=2, k even}^{10j} (-1)^j j^k/k!)"""
    return sum(
        (
            1
            / math.factorial(j)
            * sum(
                (-1) ** j * j**k / math.factorial(k)
                for k in range(2, 10 * j + 1, 2)
            )
            for j in range(0, limit + 2)
        )
    )


def main() -> None:
    """Compute the sum S eight times, taking N as each digit of your CID.
    Plot the various values of S against the number of terms N."""
    s_vals: list[float] = []
    cid = list(map(int, list(CID)))
    for digit in cid:
        s_vals.append(series(digit))

    plt.bar(cid, s_vals)
    plt.xlabel("N")
    plt.ylabel("S")
    plt.title("S vs N")
    plt.show()


if __name__ == "__main__":
    main()
