"""Perform a list of instructions"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Perform a list of instructions"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Perform in Python the following set of instructions"""
        a = 2
        b = 4
        c = a + b
        a += 1
        b = a
        c = a + b
        return {"c": c}

    @task_to_list(tasklist)
    def task2(self):
        """Calculate the value of z = 3x + y**2 for x = 11 and y = -3."""
        x = 11
        y = -3
        z = 3 * x + y * y
        return {"z": z}


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
