"""Sorting algorithm"""

import session4.a
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Sorting algorithm"""

    tasklist = []

    TaskA = session4.a.Task(output=False)
    TaskA.run_tasks()
    combined_list = TaskA.combined_list

    @task_to_list(tasklist)
    def task1(self):
        """Sort, in descending order by marks,
        the list of tuples formed in Task A."""
        self.combined_list.sort(key=lambda x: x[2], reverse=True)
        return {"sorted_list head": self.combined_list[:5]}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
    print(task.combined_list[40])
