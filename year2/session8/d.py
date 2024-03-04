"""Discrete Fourier Transform"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


def dft(yn: list | np.ndarray) -> np.ndarray:
    N = len(yn)
    k = np.arange(N)
    FT = np.sum(
        [yn * np.exp(-1j * 2 * np.pi * k * n / N) for n in range(N)], axis=1
    )
    return FT


def dft_inv(FT: list | np.ndarray) -> np.ndarray:
    N = len(FT)
    n = np.arange(N)
    yn = (
        np.sum(
            [FT * np.exp(1j * 2 * np.pi * k * n / N) for k in range(N)],
            axis=1,
        )
        / N
    )
    return yn


class Task(TaskBase):
    """Discrete Fourier Transform"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Write a function DFT(), that receives a set of numerical values,
        yn, and returns another set of values, FTk, as the Discrete Fourier
        Transform of yn
        FTk = sum_{n=0}^{N-1} yn * exp(-j2𝜋kn/N)
        with k = 0,1,...,N-1"""

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Write a function DFTInv(), that receives a set of numerical values,
        FTk, and returns another set of values, yn, as the Inverse Discrete
        Fourier Transform of FTk
        yn = 1/N sum_{k=0}^{N-1} FTk * exp(j2𝜋kn/N)
        with n = 0,1,...,N-1"""

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Create a discrete function, in the range t = [0:6𝜋], with the
        following cases:
        a) yn = sin(tn)
        b) yn = sin(tn + sin(3tn)
        c) yn = sin(tn + sin(3tn) + sin(6tn)
        d) yn = exp(-(tn - 5)^2 / 0.5)
        e) yn = exp(-(tn - 5)^2 / 4)
        For each case, determine the Discrete Fourier Transform of yn(tn),
        and plot it vs frequency."""
        N = 1000
        t = np.linspace(0, 6 * np.pi, N)
        f = np.linspace(0, N / (6 * np.pi), N)
        case_a = np.sin(t)
        self.ft_a = dft(case_a)
        plt.plot(
            f[: N // 2],
            np.abs(self.ft_a)[: N // 2],
            label="a) sin(tn)",
        )
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()
        case_b = np.sin(t) + np.sin(3 * t)
        self.ft_b = dft(case_b)
        plt.plot(
            f[: N // 2],
            np.abs(self.ft_b)[: N // 2],
            label="b) sin(tn) + sin(3tn)",
        )
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()
        case_c = np.sin(t) + np.sin(3 * t) + np.sin(6 * t)
        self.ft_c = dft(case_c)
        plt.plot(
            f[: N // 2],
            np.abs(self.ft_c)[: N // 2],
            label="c) sin(tn) + sin(3tn) + sin(6tn)",
        )
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()
        case_d = np.exp(-((t - 5) ** 2) / 0.5)
        self.ft_d = dft(case_d)
        plt.plot(
            f[: N // 2],
            np.abs(self.ft_d)[: N // 2],
            label="d) exp(-(tn - 5)^2 / 0.5)",
        )
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()
        case_e = np.exp(-((t - 5) ** 2) / 4)
        self.ft_e = dft(case_e)
        plt.plot(
            f[: N // 2],
            np.abs(self.ft_e)[: N // 2],
            label="e) exp(-(tn - 5)^2 / 4)",
        )
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task4(self) -> None:
        """For each of the Discrete Fourier Transform found in iii),
        reconstruct the signal by computing the Inverse Discrete Transform."""
        case_a = dft_inv(self.ft_a)
        plt.plot(case_a, label="a) sin(tn)")
        plt.title("Reconstructed Signal")
        plt.xlabel("t")
        plt.ylabel("yn(tn)")
        plt.legend()
        plt.show()
        case_b = dft_inv(self.ft_b)
        plt.plot(case_b, label="b) sin(tn) + sin(3tn)")
        plt.title("Reconstructed Signal")
        plt.xlabel("t")
        plt.ylabel("yn(tn)")
        plt.legend()
        plt.show()
        case_c = dft_inv(self.ft_c)
        plt.plot(case_c, label="c) sin(tn) + sin(3tn) + sin(6tn)")
        plt.title("Reconstructed Signal")
        plt.xlabel("t")
        plt.ylabel("yn(tn)")
        plt.legend()
        plt.show()
        case_d = dft_inv(self.ft_d)
        plt.plot(case_d, label="d) exp(-(tn - 5)^2 / 0.5)")
        plt.title("Reconstructed Signal")
        plt.xlabel("t")
        plt.ylabel("yn(tn)")
        plt.legend()
        plt.show()
        case_e = dft_inv(self.ft_e)
        plt.plot(case_e, label="e) exp(-(tn - 5)^2 / 4)")
        plt.title("Reconstructed Signal")
        plt.xlabel("t")
        plt.ylabel("yn(tn)")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
