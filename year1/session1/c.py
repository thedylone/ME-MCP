"""Swapping"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Swapping"""

    tasklist: list[int] = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.var_a: int = 0
        self.var_b: int = 0
        self.var_c: int = 0

    @task_to_list(tasklist)
    def task1(self) -> dict[str, int]:
        """Create two variables a and b with values 10 and 5 respectively.
        Swap their values."""
        self.var_a: int = 10
        self.var_b: int = 5
        self.var_a, self.var_b = self.var_b, self.var_a
        return {"a": self.var_a, "b": self.var_b}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int]:
        """Continuing on the previous point,
        create a third variable c with value = 20.
        Swap a with c and then c with b."""
        self.var_c: int = 20
        self.var_a, self.var_b, self.var_c = self.var_c, self.var_a, self.var_b
        return {"a": self.var_a, "b": self.var_b, "c": self.var_c}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
