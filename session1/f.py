"""Slicing and concatenation"""

from helpers.task import TaskBase, task_to_list
from session1.e import Task as TaskE


class Task(TaskBase):
    """Slicing and concatenation"""

    tasklist: list = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        task_e: TaskE = TaskE(output=False)
        task_e.run_tasks()
        self.list_a: list[int] = task_e.list_a
        self.list_b: list[int] = task_e.list_b
        self.list_c: list[int] = []
        self.list_d: list[int] = []
        self.list_e: list[int] = []
        self.list_f: list[int] = []
        self.list_g: list[int] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Slice the first six elements of list A and assign it to list C."""
        self.list_c = self.list_a[:6]
        return {"C": self.list_c}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[int]]:
        """Slice the last six elements of list B and assign it to list D."""
        self.list_d = self.list_b[-6:]
        return {"D": self.list_d}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, list[int]]:
        """Concatenate list C and D into list E."""
        self.list_e = self.list_c + self.list_d
        return {"E": self.list_e}

    @task_to_list(tasklist)
    def task4(self) -> dict[str, list[int]]:
        """Print out list E and slice the central part,
        from cell with value 13 to cell with value 26 included,
        and assign it to list F"""
        i: int = self.list_e.index(13)
        j: int = self.list_e.index(26)
        self.list_f = self.list_e[i : j + 1]
        return {"F": self.list_f}

    @task_to_list(tasklist)
    def task5(self) -> dict[str, list[int]]:
        """Concatenate list F with list C, into list G."""
        self.list_g = self.list_f + self.list_c
        return {"G": self.list_g}

    @task_to_list(tasklist)
    def task6(self) -> dict[str, list[int]]:
        """Alter the second element of list C, with the sum of
        the fifth element of list F with the fifth element of list C."""
        self.list_c[1] = self.list_f[4] + self.list_c[4]
        return {"C": self.list_c}

    @task_to_list(tasklist)
    def task7(self) -> dict[str, list[int]]:
        """Alter the last element of list C, with the sum of
        the last element of list F with the first element of list C."""
        self.list_c[-1] = self.list_f[-1] + self.list_c[0]
        return {"C": self.list_c}


if __name__ == "__main__":
    task: Task = Task("F")
    task.run_tasks()
    print(task.list_c[2])
