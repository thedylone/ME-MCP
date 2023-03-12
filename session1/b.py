"""Assignments and basic variable operations"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Assignments and basic variable operations"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, float]:
        """Create a variable var and assign the value 3.14 to it.
        Copy the value of var into another variable varcopy.
        Double the value of var."""
        var: float = 3.14
        varcopy: float = var
        var *= 2
        return {"var": var, "varcopy": varcopy}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int]:
        """Create a variable MyPints and assign the value 3 to it.
        Create another variable drink2more with value 2.
        Increment the value of MyPints by the value of drink2more.
        Increment it again (you are getting drunk!)."""
        my_pints: int = 3
        drink2more: int = 2
        my_pints += drink2more
        my_pints += drink2more
        return {"MyPints": my_pints}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, float]:
        """Create a variable Num with value 3 and a variable Den with value 4.
        Divide the value of Num by the value of Den
        and assign the result to the variable Res."""
        num: int = 3
        den: int = 4
        res: float = num / den
        return {"Res": res}


if __name__ == "__main__":
    task: Task = Task("B")
    task.run_tasks()
