"""Two-dimensional interpolation"""

import numpy as np
import matplotlib.pyplot as plt

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Two-dimensional interpolation"""

    tasklist: list = []

    flower: np.ndarray = np.array([])
    shrunk: np.ndarray = np.array([])
    larger: np.ndarray = np.array([])

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Read the image Flower.jpg and plot it."""
        self.flower: np.ndarray = plt.imread("year2/session3/Flower.jpg")
        plt.imshow(self.flower)
        plt.show()

    @task_to_list(tasklist)
    def task2(self) -> None:
        """Shrink the image into a new image, n time smaller, and save it into
        a new file, Shrunk.jpg."""
        n = 2
        self.shrunk = self.flower[::n, ::n]
        plt.imshow(self.shrunk)
        plt.show()
        plt.imsave("year2/session3/Shrunk.jpg", self.shrunk)

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Resize the image, m time larger, by using the bilinear
        interpolation (slide 92), starting from the shrunk image,
        Shrunk.jpg."""
        m = 3
        self.larger = np.ndarray(
            (m * self.shrunk.shape[0], m * self.shrunk.shape[1], 3)
        )
        
        plt.imshow(self.larger)
        plt.show()



if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
