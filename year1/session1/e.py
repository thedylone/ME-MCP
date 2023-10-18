"""Creating Lists"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Creating Lists"""

    tasklist: list = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.list_a: list[int] = []
        self.list_b: list[int] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Create manually two lists A and B,
        with integer values from 10 to 20 (included)
        and from 20 to 30 (included), respectively."""
        self.list_a: list[int] = list(range(10, 21))
        self.list_b: list[int] = list(range(20, 31))
        return {"A": self.list_a, "B": self.list_b}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[int]]:
        """Sum up the third and the fourth element of A
        and assign it to the fifth element of B.
        Double the sixth element of B."""
        self.list_b[4] = self.list_a[2] + self.list_a[3]
        self.list_b[5] *= 2
        return {"B": self.list_b}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, list[int]]:
        """Swap the first and the last elements of A."""
        self.list_a[0], self.list_a[-1] = self.list_a[-1], self.list_a[0]
        return {"A": self.list_a}

    @task_to_list(tasklist)
    def task4(self) -> dict[str, list[int]]:
        """Set the two variables i and j to 3 and 5, respectively.
        Swap the i-index element of B with the j-index element of A."""
        i: int = 3
        j: int = 5
        self.list_b[i], self.list_a[j] = self.list_a[j], self.list_b[i]
        return {"A": self.list_a, "B": self.list_b}


if __name__ == "__main__":
    task: Task = Task("E")
    task.run_tasks()
    print(task.list_b[3])
