"""Signal processing"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list
from year2.session8.d import dft, dft_inv


class Task(TaskBase):
    """Signal processing"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str]:
        """The file Vibration.txt contains the temporal response of a
        vibrating beam, excited by a hammer bang, with vibrating signal
        sampled every 0.01 sec.
        Determine the resonant frequency of the beam."""
        dt = 0.01
        with open("year2/session8/Vibration.txt") as file:
            data = file.readlines()
        yn = [float(d.strip()) for d in data]
        N = len(yn)
        t = np.arange(N) * dt
        plt.plot(t, yn)
        plt.title("Vibration")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
        f = np.arange(N) / (N * dt)
        ft = dft(yn)
        plt.plot(f[: int(N / 2)], np.abs(ft)[: int(N / 2)])
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.show()
        resonant = f[np.argmax(np.abs(ft))]
        return {"resonance": f"{resonant} Hz {resonant * 2 * np.pi} rad/s"}

    @task_to_list(tasklist)
    def task2(self) -> None:
        """The file Noisy.txt contains a Gaussian signal, disturbed by a
        superimposed random noise. The signal has been sampled with a sampling
        rate of 20 samples per sec.
        Apply a numerical filter to cut off the disturbing noise."""
        dt = 1 / 20
        with open("year2/session8/Noisy.txt") as file:
            data = file.readlines()
        yn = [float(d.strip()) for d in data]
        N = len(yn)
        t = np.arange(N) * dt
        plt.plot(t, yn)
        plt.title("Noisy Signal")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
        f = np.arange(N) / (N * dt)
        ft = dft(yn)
        plt.plot(f[: int(N / 2)], np.abs(ft)[: int(N / 2)])
        plt.title("Discrete Fourier Transform")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.show()
        # low pass filter
        fc = 0.2
        H = 1 / (1 + 1j * f / fc)
        yn_clean = dft_inv(ft * H)
        plt.plot(t, yn_clean)
        plt.title("Clean Signal")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
        # Plot both signals
        plt.plot(t, yn, label="Noisy Signal")
        plt.plot(t, yn_clean, label="Clean Signal")
        plt.title("Noisy vs Clean Signal")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
