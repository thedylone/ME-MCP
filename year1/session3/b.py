"""I/O Files"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """I/O Files"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.marks: list[int] = []

    def import_marks(self) -> None:
        """Import Marks.txt and save to self.marks"""
        with open("year1/session3/Marks.txt", "r", encoding="utf-8") as file:
            self.marks: list[int] = list(map(int, file.readlines()))

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float | list[int]]:
        """Write a script to compute the average mark
        and to find the maximum mark"""
        self.import_marks()
        total: int = 0
        maximum: int = 0
        for mark in self.marks:
            total += mark
            maximum = max(maximum, mark)
        average: float = total / len(self.marks)
        return {"average": average, "maximum": maximum}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
    print(sum(task.marks[:50]) / 50)
