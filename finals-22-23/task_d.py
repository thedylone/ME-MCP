"""Task D"""

import os

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


def sequence(num) -> float:
    """Write a RECURSIVE function, Sequence(), to calculate the sequence:
    y1 = 0
    y2 = 1
    yn = yn-1 - (n+1) * yn-2"""
    if num == 1:
        return 0
    if num == 2:
        return 1
    return sequence(num - 1) - (num + 1) * sequence(num - 2)


def main() -> None:
    """Print the first 20 values of the sequence."""
    for i in range(1, 21):
        print(sequence(i))


if __name__ == "__main__":
    main()
