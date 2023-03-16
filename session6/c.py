"""Permutation of letters (How to crack a password)"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Permutation of letters (How to crack a password)"""

    tasklist: list = []

    @staticmethod
    def permute(values: list) -> list[list]:
        """Permute a list of values"""
        if len(values) == 0:
            return []
        if len(values) == 1:
            return [values]
        output: list[list] = []
        for i, val in enumerate(values):
            rem_list: list = values[:i] + values[i + 1 :]
            for perm in Task.permute(rem_list):
                output.append([val] + perm)
        return output

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[list[str]]]:
        """Given a list of N values, write a recursive function, Permute,
        to determine all the possible permutations of these values."""
        string: str = get_input(
            str, "Enter a list of values separated by commas"
        )
        return {"permutations": Task.permute(string.split(","))}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
    print(task.permute([1, 2, 3, 4]))
