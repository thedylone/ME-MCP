"""Creating Lists"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Creating Lists"""

    tasklist = []
    A = None
    B = None

    @task_to_list(tasklist)
    def task1(self):
        """Create manually two lists A and B,
        with integer values from 10 to 20 (included)
        and from 20 to 30 (included), respectively."""
        self.A = list(range(10, 21))
        self.B = list(range(20, 31))
        return {"A": self.A, "B": self.B}

    @task_to_list(tasklist)
    def task2(self):
        """Sum up the third and the fourth element of A
        and assign it to the fifth element of B.
        Double the sixth element of B."""
        self.B[4] = self.A[2] + self.A[3]
        self.B[5] *= 2
        return {"B": self.B}

    @task_to_list(tasklist)
    def task3(self):
        """Swap the first and the last elements of A."""
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        return {"A": self.A}

    @task_to_list(tasklist)
    def task4(self):
        """Set the two variables i and j to 3 and 5, respectively.
        Swap the i-index element of B with the j-index element of A."""
        i = 3
        j = 5
        self.B[i], self.A[j] = self.A[j], self.B[i]
        return {"A": self.A, "B": self.B}


if __name__ == "__main__":
    task = Task("E")
    task.run_tasks()
    print(task.B[3])
