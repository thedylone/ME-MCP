"""Sorting algorithm"""

from helpers.task import TaskBase, task_to_list
from year1.session4.a import Task as TaskA


class Task(TaskBase):
    """Sorting algorithm"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        task_a = TaskA(output=False)
        task_a.run_tasks()
        self.combined_list: list[tuple[str, str, int]] = task_a.combined_list

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[tuple[str, str, int]]]:
        """Sort, in descending order by marks,
        the list of tuples formed in Task A."""
        self.combined_list.sort(key=lambda x: x[2], reverse=True)
        return {"sorted_list head": self.combined_list[:5]}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
    print(task.combined_list[40])
