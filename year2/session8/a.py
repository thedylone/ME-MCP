"""Complex numbers and phasors"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Complex numbers and phasors"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Plot, in the range t = [0:2𝜋], a cosine wave with amplitude 10 and
        frequency f = 0.5Hz and another cosine wave with same frequency,
        amplitude 5 and lagged by 90 degree.
        y(t) = V_m * sin(𝜔𝑡 + 𝜑)"""
        amp: float = 10
        freq: float = 0.5
        angular = 2 * np.pi * freq
        phase: float = np.pi / 2
        self.time: np.ndarray = np.linspace(0, 2 * np.pi, 100)
        self.wave_a: np.ndarray = amp * np.cos(angular * self.time)
        self.wave_b: np.ndarray = amp * np.cos(angular * self.time - phase)
        plt.plot(self.time, self.wave_a, label="Wave A")
        plt.plot(self.time, self.wave_b, label="Wave B")
        plt.legend()
        plt.title("Task 1")
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Offset the second signal by 5 (DC component)."""
        self.wave_b = self.wave_b + 5
        plt.plot(self.time, self.wave_a, label="Wave A")
        plt.plot(self.time, self.wave_b, label="Wave B")
        plt.legend()
        plt.title("Task 2: Offset Wave B by 5")
        plt.show()

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Plot, in the range t = [0:𝜋], a cosine wave with amplitude 10 and
        frequency f = 0.5Hz and another cosine wave with same amplitude, but
        double frequency."""
        amp: float = 10
        freq: float = 0.5
        angular = 2 * np.pi * freq
        time: np.ndarray = np.linspace(0, np.pi, 100)
        wave_c: np.ndarray = amp * np.cos(angular * time)
        wave_d: np.ndarray = amp * np.cos(2 * angular * time)
        plt.plot(time, wave_c, label="Wave C")
        plt.plot(time, wave_d, label="Wave D")
        plt.legend()
        plt.title("Task 3")
        plt.show()

    @task_to_list(tasklist)
    def task4(self) -> None:
        """Plot, in the range t = [0:𝜋], a cosine wave with amplitude 10 and
        frequency f = 0.5Hz and another cosine wave with same amplitude,
        double frequency and lagged by 45 degrees."""
        amp: float = 10
        freq: float = 0.5
        angular = 2 * np.pi * freq
        phase: float = np.pi / 4
        time: np.ndarray = np.linspace(0, np.pi, 100)
        self.wave_e: np.ndarray = amp * np.cos(angular * time)
        self.wave_f: np.ndarray = amp * np.cos(2 * angular * time - phase)
        plt.plot(time, self.wave_e, label="Wave E")
        plt.plot(time, self.wave_f, label="Wave F")
        plt.legend()
        plt.title("Task 4")
        plt.show()

    @task_to_list(tasklist)
    def task5(self) -> None:
        """Represent the two cosine waves in Task 4 with phasors and plot them
        in the complex plane."""
        amp: float = 10
        phase: float = np.pi / 4
        self.phasor_e: complex = amp * np.exp(1j * 0)
        self.phasor_f: complex = amp * np.exp(1j * -phase)
        plt.arrow(
            0,
            0,
            self.phasor_e.real,
            self.phasor_e.imag,
            label="Phasor E",
            color="r",
            width=0.1,
        )
        plt.arrow(
            0,
            0,
            self.phasor_f.real,
            self.phasor_f.imag,
            label="Phasor F",
            color="b",
            width=0.1,
        )
        plt.legend()
        plt.title("Task 5")
        plt.show()

    @task_to_list(tasklist)
    def task6(self) -> None:
        """Add the two signals, both in time domain and as phasors. Plot the
        corresponding results."""
        # time domain
        time_sum: np.ndarray = self.wave_e + self.wave_f
        plt.plot(self.time, time_sum, label="Time Domain")
        plt.legend()
        plt.title("Task 6: Time Domain")
        plt.show()
        # phasor domain
        phasor_sum: complex = self.phasor_e + self.phasor_f
        plt.arrow(
            0,
            0,
            self.phasor_e.real,
            self.phasor_e.imag,
            label="Phasor E",
            color="r",
            width=0.1,
        )
        plt.arrow(
            0,
            0,
            self.phasor_f.real,
            self.phasor_f.imag,
            label="Phasor F",
            color="b",
            width=0.1,
        )
        plt.arrow(
            0,
            0,
            phasor_sum.real,
            phasor_sum.imag,
            label="Phasor Sum",
            color="g",
            width=0.1,
        )
        plt.legend()
        plt.title("Task 6: Phasor Domain")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
