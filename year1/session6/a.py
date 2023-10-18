"""Fibonacci sequence"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Fibonacci sequence"""

    tasklist: list = []

    @staticmethod
    def fibonacci(num: int) -> int:
        """Fibonacci sequence"""
        if num < 0:
            return 0
        if num == 1:
            return 1
        return Task.fibonacci(num - 1) + Task.fibonacci(num - 2)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Write a recursive function, Fibonacci(n),
        to compute the n-th Fibonacci number.
        Generate the first N numbers of the sequence"""
        num: int = get_input(int, "Enter a number")
        fibonacci: list[int] = [Task.fibonacci(i) for i in range(1, num + 1)]
        return {"fibonacci": fibonacci}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    print(task.fibonacci(27))
