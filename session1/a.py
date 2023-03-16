"""Perform a list of instructions"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Perform a list of instructions"""

    tasklist: list = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, int]:
        """Perform in Python the following set of instructions"""
        var_a: int = 2
        var_b: int = 4
        var_c: int = var_a + var_b
        var_a += 1
        var_b = var_a
        var_c = var_a + var_b
        return {"c": var_c}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int]:
        """Calculate the value of z = 3x + y**2 for x = 11 and y = -3."""
        var_x: int = 11
        var_y: int = -3
        var_z: int = 3 * var_x + var_y * var_y
        return {"z": var_z}


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
