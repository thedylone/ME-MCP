"""Short questions"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Short questions"""

    tasklist: list = []

    @staticmethod
    def swap(var_a, var_b):
        """Write a function, Swap, that receives two variables,
        and returns their values swapped. (Max three lines of code)."""
        return var_b, var_a

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str]:
        """Write a function, Swap, that receives two variables,
        and returns their values swapped. (Max three lines of code)."""
        var_a: str = "a"
        var_b: str = "b"
        var_a, var_b = self.swap(var_a, var_b)
        return {"var_a": var_a, "var_b": var_b}

    @staticmethod
    def trace(mat_a: list[list[float]]) -> float:
        """Find and correct the mistakes in the following function, such that
        it returns the trace of matrix A."""
        rows: int = len(mat_a)
        trace: float = 0
        for i in range(rows):
            trace += mat_a[i][i]
        return trace

    @task_to_list(tasklist)
    def task2(self) -> dict[str, float | list[list[float]]]:
        """Find and correct the mistakes in the following function, such that
        it returns the trace of matrix A."""
        mat_a: list[list[float]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        trace: float = self.trace(mat_a)
        return {"matrix": mat_a, "trace": trace}

    @staticmethod
    def twins(num_n: int) -> int:
        """Write a recursive function, Twins, in the space below, that
        computes the series S = sum_{n=1}^{N} (-1)^n * n."""
        if num_n == 1:
            return -1
        return (-1) ** num_n * num_n + Task.twins(num_n - 1)

    @task_to_list(tasklist)
    def task3(self) -> dict[str, int]:
        """Write a recursive function, Twins, in the space below, that
        computes the series S = sum_{n=1}^{N} (-1)^n * n."""
        num_n: int = 5
        total: int = self.twins(num_n)
        return {"total": total}


if __name__ == "__main__":
    task: Task = Task("1")
    task.run_tasks()
    assert task.swap(2, 3) == (3, 2)
    assert (
        task.trace(
            [
                [1, 2, 3, 4, 5, 6],
                [6, 0, 3, 4, 2, 1],
                [2, 1, 9, 4, 6, 7],
                [3, 0, 8, 4, 6, 5],
                [1, 5, 4, 3, 3, 1],
                [6, 1, 4, 4, 3, 2],
            ]
        )
        == 19
    )
    assert task.twins(7) == -4
