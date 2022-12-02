"""Sorting algorithm"""

from helpers.task import TaskBase, task_to_list

import session4.a


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
        self.combined_list.sort(key=lambda x: int(x[2]), reverse=True)
        return {"combined_list": self.combined_list[:5]}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
    print(task.combined_list[40])
