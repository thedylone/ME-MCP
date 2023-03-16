"""Reverse a string"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Reverse a string"""

    tasklist: list = []

    @staticmethod
    def reverse(string: str) -> str:
        """Reverse a string"""
        if len(string) == 0:
            return string
        return Task.reverse(string[1:]) + string[0]

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str]:
        """Write a recursive function, Reverse(string),
        to reverse a given string, i.e., from
        "stressed" to "desserts"."""
        string: str = get_input(str, "Enter a string")
        return {"reverse": Task.reverse(string)}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
