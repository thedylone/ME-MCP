"""List of tuples"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """List of tuples"""

    tasklist = []
    combined_list = []

    @task_to_list(tasklist)
    def task1(self):
        """Write a script to form a list of tuples,
        associating every line content of the three files into a tuple."""
        with (
            open("session4/Names.txt", "r", encoding="utf-8") as names,
            open("session4/Groups.txt", "r", encoding="utf-8") as groups,
            open("session4/Marks.txt", "r", encoding="utf-8") as marks,
        ):
            self.combined_list = list(
                map(
                    lambda x, y, z: (x.strip(), y.strip(), int(z)),
                    names,
                    groups,
                    marks,
                )
            )

        return {"combined_list head": self.combined_list[:5]}


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
    print(task.combined_list[20][2])
