"""Managing lists"""

from helpers.task import TaskBase, task_to_list
from session2.a import Task as TaskA


class Task(TaskBase):
    """Managing lists"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        task_a: TaskA = TaskA("A", False)
        task_a.run_tasks()
        self.list_a: list[int] = task_a.list_a
        self.list_d: list[int] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Starting from list A generated in Task A,
        set to zero the values in every third element."""
        self.list_a = [
            0 if i % 3 == 0 else v for i, v in enumerate(self.list_a)
        ]
        return {"A": self.list_a}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[int]]:
        """Then create a new list D that is
        the reverse (flipped position) of list A."""
        self.list_d = self.list_a[::-1]
        return {"D": self.list_d}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
    print(task.list_d[69])
