"""Managing lists"""

import session2.a
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Managing lists"""

    tasklist = []
    TaskA = session2.a.Task(output=False)
    TaskA.run_tasks()
    A = TaskA.A
    D = []

    @task_to_list(tasklist)
    def task1(self):
        """Starting from list A generated in Task A,
        set to zero the values in every third element."""
        self.A = [0 if i % 3 == 0 else v for i, v in enumerate(self.A)]
        return {"A": self.A}

    @task_to_list(tasklist)
    def task2(self):
        """Then create a new list D that is
        the reverse (flipped position) of list A."""
        self.D = self.A[::-1]
        return {"D": self.D}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
    print(task.D[69])
