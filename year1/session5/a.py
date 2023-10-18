"""Factorial, again"""

from helpers.task import TaskBase, RangeValidator, get_input, task_to_list


class Task(TaskBase):
    """Factorial, again"""

    tasklist: list = []

    @staticmethod
    def factorial(n) -> int:
        """Write a function, Factorial, to compute the factorial
        of an integer number. The function receives an integer number n
        and returns the value of its factorial."""
        if not isinstance(n, int) or n < 0:
            raise TypeError("n must be an integer")
        if n < 2:
            return 1
        return n * Task.factorial(n - 1)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, int]:
        """Write a function, Factorial, to compute the factorial
        of an integer number. The function receives an integer number n
        and returns the value of its factorial."""
        num: int = get_input(int, "Enter an integer", RangeValidator(minval=0))
        return {"factorial": self.factorial(num)}


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
