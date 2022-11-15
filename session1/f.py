"""Slicing and concatenation"""

import session1.e
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Slicing and concatenation"""

    # Following up from Task E:
    tasklist = []
    TaskE = session1.e.Task(output=False)
    TaskE.run_tasks()
    A = TaskE.A
    B = TaskE.B
    C = []
    D = []
    E = []
    F = []
    G = []

    @task_to_list(tasklist)
    def task1(self):
        """Slice the first six elements of list A and assign it to list C."""
        self.C = self.A[:6]
        return {"C": self.C}

    @task_to_list(tasklist)
    def task2(self):
        """Slice the last six elements of list B and assign it to list D."""
        self.D = self.B[-6:]
        return {"D": self.D}

    @task_to_list(tasklist)
    def task3(self):
        """Concatenate list C and D into list E."""
        self.E = self.C + self.D
        return {"E": self.E}

    @task_to_list(tasklist)
    def task4(self):
        """Print out list E and slice the central part,
        from cell with value 13 to cell with value 26 included,
        and assign it to list F"""
        i = self.E.index(13)
        j = self.E.index(26)
        self.F = self.E[i : j + 1]
        return {"F": self.F}

    @task_to_list(tasklist)
    def task5(self):
        """Concatenate list F with list C, into list G."""
        self.G = self.F + self.C
        return {"G": self.G}

    @task_to_list(tasklist)
    def task6(self):
        """Alter the second element of list C, with the sum of
        the fifth element of list F with the fifth element of list C."""
        self.C[1] = self.F[4] + self.C[4]
        return {"C": self.C}

    @task_to_list(tasklist)
    def task7(self):
        """Alter the last element of list C, with the sum of
        the last element of list F with the first element of list C."""
        self.C[-1] = self.F[-1] + self.C[0]
        return {"C": self.C}


if __name__ == "__main__":
    task = Task("F")
    task.run_tasks()
    print(task.C[2])
