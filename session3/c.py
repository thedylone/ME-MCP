"""Searching values in a list"""

from helpers.task import TaskBase, get_input, task_to_list
from session3.b import Task as TaskB


class Task(TaskBase):
    """Searching values in a list"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        task_b: TaskB = TaskB()
        task_b.import_marks()
        self.marks: list[int] = task_b.marks
        self.cids: list[int] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str] | dict[str, int]:
        """Write a script to search and display the score of a student,
        specifying their CID from the keyboard."""
        index: int = -1
        cid: int = get_input(int, "CID")
        with open("session3/CID.txt", "r", encoding="utf-8") as file:
            for i, line in enumerate(file.readlines()):
                if int(line) == cid:
                    index = i
                self.cids.append(int(line))
        if index == -1:
            return {"error": "CID not found"}
        return {"mark": self.marks[index]}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int | list[int]]:
        """Display the list of students who achieved the maximum mark.
        Save the list into the file Best.txt."""
        maximum: int = 0
        indices: list[int] = []
        for i, mark in enumerate(self.marks):
            if mark > maximum:
                maximum = mark
                indices = [i]
            elif mark == maximum:
                indices.append(i)
        students: list[int] = [self.cids[index] for index in indices]
        with open("session3/Best.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(map(str, students)))
        return {"maximum": maximum, "students": students}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
