"""Swapping"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Swapping"""

    tasklist = []
    a = 0
    b = 0
    c = 0

    @task_to_list(tasklist)
    def task1(self):
        """Create two variables a and b with values 10 and 5 respectively.
        Swap their values."""
        self.a = 10
        self.b = 5
        self.a, self.b = self.b, self.a
        return {"a": self.a, "b": self.b}

    @task_to_list(tasklist)
    def task2(self):
        """Continuing on the previous point,
        create a third variable c with value = 20.
        Swap a with c and then c with b."""
        self.c = 20
        self.a, self.b, self.c = self.c, self.a, self.b
        return {"a": self.a, "b": self.b, "c": self.c}


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
