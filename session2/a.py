"""Generating lists"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Generating lists"""

    tasklist = []
    A = []
    B = []
    C = []

    @task_to_list(tasklist)
    def task1(self):
        """Generate a list A of N = 100 elements,
        containing the integer numbers from 1 to 100."""
        self.A = list(range(1, 101))
        return {"A": self.A}

    @task_to_list(tasklist)
    def task2(self):
        """Create a second list B that contains
        the squared values of the elements of A."""
        self.B = list(map(lambda x: x * x, self.A))
        return {"B": self.B}

    @task_to_list(tasklist)
    def task3(self):
        """Sum up the two lists together into a new list C."""
        self.C = list(map(sum, zip(self.A, self.B)))
        return {"C": self.C}


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
    print(task.C[9])
