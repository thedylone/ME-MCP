"""Searching values in a list"""

import session3.b
from helpers.task import TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Searching values in a list"""

    tasklist = []
    TaskB = session3.b.Task(output=False)
    TaskB.import_marks()
    marks = TaskB.marks
    cids = []

    @task_to_list(tasklist)
    def task1(self):
        """Write a script to search and display the score of a student,
        specifying their CID from the keyboard."""
        index = -1
        cid = get_input(int, "CID")
        with open("session3/CID.txt", "r", encoding="utf-8") as file:
            for i, line in enumerate(file.readlines()):
                line = int(line)
                if line == cid:
                    index = i
                self.cids.append(line)
        if index == -1:
            return {"error": "CID not found"}
        return {"mark": self.marks[index]}

    @task_to_list(tasklist)
    def task2(self):
        """Display the list of students who achieved the maximum mark.
        Save the list into the file Best.txt."""
        maximum = 0
        indices = []
        for i, mark in enumerate(self.marks):
            if mark > maximum:
                maximum = mark
                indices = [i]
            elif mark == maximum:
                indices.append(i)
        with open("session3/Best.txt", "w", encoding="utf-8") as file:
            for index in indices:
                file.write(f"{self.cids[index]}\n")


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
