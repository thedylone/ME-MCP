"""Complex functions: analogue filters and Bode plots"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Complex functions: analogue filters and Bode plots"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Consider the complex function of 𝜔:
        H(𝜔) = 1/(1 + j0.1𝜔)
        Plot the Bode diagram (with log scale x-axis), for both amplitude and
        phase, in the range 𝜔 = [0:10K]
        Plot the Bode diagram (with log scale x-axis), with amplitude
        expressed in dB (decibel).
        """
        w = np.logspace(0, 4, 1000)
        H = 1 / (1 + 0.1j * w)
        plt.plot(w, np.abs(H), label="Amplitude")
        plt.plot(w, np.angle(H), label="Phase")
        plt.xscale("log")
        plt.title("Bode Diagram")
        plt.xlabel("Frequency (rad/s)")
        plt.ylabel("Amplitude and Phase")
        plt.legend()
        plt.show()
        plt.plot(w, 20 * np.log10(np.abs(H)), label="Amplitude (dB)")
        plt.plot(w, np.angle(H), label="Phase")
        plt.xscale("log")
        plt.title("Bode Diagram (dB)")
        plt.xlabel("Frequency (rad/s)")
        plt.ylabel("Amplitude (dB) and Phase")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Determine the gain function, H(𝜔), of this electronic linear
        circuit (make use of impedance concepts):
        Vi input, connected in series to a resistor R1 = 1kΩ and a
        capacitor C1 = 1mF in parallel, and connected in parallel to a
        resistor R2 = 2kΩ and a capacitor C2 = 2mF. Vo output.
        Plot the Bode diagram (with log scale x-axis), for both amplitude
        (in dB) and phase, in the range 𝜔 = [0.001: 10]"""
        w = np.logspace(-3, 1, 1000)
        R1 = 1e3
        C1 = 1e-3
        R2 = 2e3
        C2 = 2e-3
        z1 = 1 / (1 / R1 + 1j * w * C1)
        z2 = 1 / (1 / R2 + 1j * w * C2)
        H = z2 / (z1 + z2)
        plt.plot(w, 20 * np.log10(np.abs(H)), label="Amplitude (dB)")
        plt.plot(w, np.angle(H), label="Phase")
        plt.xscale("log")
        plt.title("Bode Diagram")
        plt.xlabel("Frequency (rad/s)")
        plt.ylabel("Amplitude (dB) and Phase")
        plt.legend()
        plt.show()

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Express all the components in the above circuit as impedances, in
        the range 𝜔 = [0.001:10], and determine the numerical equivalent of
        H(𝜔)."""

    @task_to_list(tasklist)
    def task4(self) -> None:
        """Consider the two gain functions of a passive low pass filter and a
        passive high pass filter:
        H_LP(𝜔) = 1/(1 + j0.01𝜔)
        H_HP(𝜔) = j40𝜔 / (1 + j40𝜔)
        Cascade the two filters, decoupling them with an op-amp voltage
        follower buffer:
        Plot the Bode diagram (with log scale x-axis), for both amplitude (in
        dB) and phase, in the range 𝜔 = [0.0001:10000], for the two
        individual filters and the cascaded filter. Plot a point
        correspondingly to the corner frequencies of the two individual
        filters."""
        w = np.logspace(-4, 4, 1000)
        H_LP = 1 / (1 + 0.01j * w)
        H_HP = 40j * w / (1 + 40j * w)
        H_cascade = H_LP * H_HP
        # corner frequencies where the amplitude is 1/sqrt(2)
        w_lp = 1 / 0.01
        w_hp = 1 / 40
        plt.plot(w, 20 * np.log10(np.abs(H_LP)), label="LP Amplitude (dB)")
        plt.plot(w, np.angle(H_LP), label="LP Phase")
        plt.plot(w, 20 * np.log10(np.abs(H_HP)), label="HP Amplitude (dB)")
        plt.plot(w, np.angle(H_HP), label="HP Phase")
        plt.plot(
            w, 20 * np.log10(np.abs(H_cascade)), label="Cascade Amplitude (dB)"
        )
        plt.plot(w, np.angle(H_cascade), label="Cascade Phase")
        plt.scatter(w_lp, 20 * np.log10(1 / np.sqrt(2)), color="red")
        plt.scatter(w_hp, 20 * np.log10(1 / np.sqrt(2)), color="red")
        plt.xscale("log")
        plt.title("Bode Diagram")
        plt.xlabel("Frequency (rad/s)")
        plt.ylabel("Amplitude (dB) and Phase")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
