"""List of tuples"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """List of tuples"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.combined_list: list[tuple[str, str, int]] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[tuple[str, str, int]]]:
        """Write a script to form a list of tuples,
        associating every line content of the three files into a tuple."""
        with (
            open("year1/session4/Names.txt", "r", encoding="utf-8") as names,
            open("year1/session4/Groups.txt", "r", encoding="utf-8") as groups,
            open("year1/session4/Marks.txt", "r", encoding="utf-8") as marks,
        ):
            self.combined_list = list(
                map(
                    lambda x, y, z: (x.strip(), y.strip(), int(z)),
                    names,
                    groups,
                    marks,
                )
            )

        return {"combined_list head": self.combined_list[:5]}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
    print(task.combined_list[20][2])
