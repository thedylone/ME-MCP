"""Type conversion"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Type conversion"""

    tasklist = []
    a = None
    b = None
    c = None
    d = None

    @task_to_list(tasklist)
    def task1(self):
        """Assign the value 2 as a string to variable a
        and the value 2 as a number to variable b."""
        self.a = str(2)
        self.b = 2

    @task_to_list(tasklist)
    def task2(self):
        """Add a and b into variable f.
        What does happen when you run the code and why?"""
        try:
            f = self.a + self.b
            return {"f": f}
        except TypeError as e:
            return {"error": e}

    @task_to_list(tasklist)
    def task3(self):
        """Assign the value 3 as a string to variable c
        and the value 3 as a number to variable d."""
        self.c = str(3)
        self.d = 3

    @task_to_list(tasklist)
    def task4(self):
        """Add a and c into variable g. Add b and d into variable h."""
        g = self.a + self.c
        h = self.b + self.d
        return {"g": g, "h": h}

    @task_to_list(tasklist)
    def task5(self):
        """Convert a and c into numbers
        and add again a and c into variable m."""
        self.a = int(self.a)
        self.c = int(self.c)
        m = self.a + self.c
        return {"m": m, "m_type": type(m)}


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()
