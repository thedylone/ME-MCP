"""Merge sort (Divide et Conquer)"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Merge sort (Divide et Conquer)"""

    tasklist: list = []

    @staticmethod
    def mergesort(values) -> list[int]:
        """Merge sort a list of values"""
        length: int = len(values)
        if length == 0:
            return []
        if length == 1:
            return values
        i: int = 0
        j: int = 0
        list_a: list[int] = Task.mergesort(values[: length // 2])
        list_b: list[int] = Task.mergesort(values[length // 2 :])
        output: list[int] = []
        while i < len(list_a) or j < len(list_b):
            if i >= len(list_a):
                output += list_b[j:]
                break
            if j >= len(list_b):
                output += list_a[i:]
                break
            if list_a[i] < list_b[j]:
                output.append(list_a[i])
                i += 1
            elif list_b[j] < list_a[i]:
                output.append(list_b[j])
                j += 1
            elif list_b[j] == list_a[i]:
                output.append(list_a[i])
                output.append(list_b[j])
                i += 1
                j += 1
        return output

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int]]:
        """Write a recursive function, MergeSort(List), that receives
        a list of values and returns the same list sorted in ascending values,
        by using the Merge Sort method algorithm."""
        values_str: str = get_input(str, "Enter values separated by commas")
        values: list[int] = [int(val) for val in values_str.split(",")]
        return {"sorted": Task.mergesort(values)}


if __name__ == "__main__":
    task: Task = Task("G")
    task.run_tasks()
