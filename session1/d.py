"""Type conversion"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Type conversion"""

    tasklist: list[int] = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.var_a: str | int = ""
        self.var_b: int = 0
        self.var_c: str | int = ""
        self.var_d: int = 0

    @task_to_list(tasklist)
    def task1(self) -> None:
        """Assign the value 2 as a string to variable a
        and the value 2 as a number to variable b."""
        self.var_a: str | int = str(2)
        self.var_b: int = 2

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int | TypeError]:
        """Add a and b into variable f.
        What does happen when you run the code and why?"""
        try:
            var_f = self.var_a + self.var_b
            return {"var_f": var_f}
        except TypeError as err:
            return {"error": err}

    @task_to_list(tasklist)
    def task3(self) -> None:
        """Assign the value 3 as a string to variable c
        and the value 3 as a number to variable d."""
        self.var_c: str | int = str(3)
        self.var_d: int = 3

    @task_to_list(tasklist)
    def task4(self) -> dict[str, str | int]:
        """Add a and c into variable g. Add b and d into variable h."""
        var_g: str = self.var_a + self.var_c
        var_h: int = self.var_b + self.var_d
        return {"var_g": var_g, "var_h": var_h}

    @task_to_list(tasklist)
    def task5(self) -> dict[str, int | type]:
        """Convert a and c into numbers
        and add again a and c into variable m."""
        self.var_a = int(self.var_a)
        self.var_c = int(self.var_c)
        var_m: int = self.var_a + self.var_c
        return {"m": var_m, "m_type": type(var_m)}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
