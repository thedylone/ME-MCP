"""I/O Files"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """I/O Files"""

    tasklist = []
    marks = []

    def import_marks(self):
        """Import Marks.txt and save to self.marks"""
        with open("session3/Marks.txt", "r", encoding="utf-8") as file:
            self.marks = list(map(int, file.readlines()))

    @task_to_list(tasklist)
    def task1(self):
        """Write a script to compute the average mark
        and to find the maximum mark"""
        self.import_marks()
        total = 0
        maximum = 0
        for mark in self.marks:
            total += mark
            maximum = max(maximum, mark)
        average = total / len(self.marks)
        return {"average": average, "maximum": maximum}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
    print(sum(task.marks[:50]) / 50)
