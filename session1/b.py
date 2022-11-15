"""Assignments and basic variable operations"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Assignments and basic variable operations"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Create a variable var and assign the value 3.14 to it.
        Copy the value of var into another variable varcopy.
        Double the value of var."""
        var = 3.14
        varcopy = var
        var *= 2
        return {"var": var, "varcopy": varcopy}

    @task_to_list(tasklist)
    def task2(self):
        """Create a variable MyPints and assign the value 3 to it.
        Create another variable drink2more with value 2.
        Increment the value of MyPints by the value of drink2more.
        Increment it again (you are getting drunk!)."""
        MyPints = 3
        drink2more = 2
        MyPints += drink2more
        MyPints += drink2more
        return {"MyPints": MyPints}

    @task_to_list(tasklist)
    def task3(self):
        """Create a variable Num with value 3 and a variable Den with value 4.
        Divide the value of Num by the value of Den
        and assign the result to the variable Res."""
        Num = 3
        Den = 4
        Res = Num / Den
        return {"Res": Res}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
