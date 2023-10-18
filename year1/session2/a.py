"""Generating lists"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Generating lists"""

    tasklist: list = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.list_a: list[int] = []
        self.list_b: list[int] = []
        self.list_c: list[int] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Generate a list A of N = 100 elements,
        containing the integer numbers from 1 to 100."""
        self.list_a = list(range(1, 101))
        return {"A": self.list_a}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[int]]:
        """Create a second list B that contains
        the squared values of the elements of A."""
        self.list_b = list(map(lambda x: x * x, self.list_a))
        return {"B": self.list_b}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, list[int]]:
        """Sum up the two lists together into a new list C."""
        self.list_c = list(map(sum, zip(self.list_a, self.list_b)))
        return {"C": self.list_c}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    print(task.list_c[9])
