"""Merge sort (Divide et Conquer)"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Merge sort (Divide et Conquer)"""

    tasklist = []

    @staticmethod
    def mergesort(values):
        """Merge sort a list of values"""
        length = len(values)
        if length == 0:
            return []
        if length == 1:
            return values
        i = 0
        j = 0
        list_a = Task.mergesort(values[: length // 2])
        list_b = Task.mergesort(values[length // 2 :])
        output = []
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
    def task1(self):
        """Write a recursive function, MergeSort(List), that receives
        a list of values and returns the same list sorted in ascending values,
        by using the Merge Sort method algorithm."""
        values = get_input(str, "Enter values separated by commas").split(",")
        values = [int(val) for val in values]
        return {"sorted": Task.mergesort(values)}


if __name__ == "__main__":
    task = Task("G")
    task.run_tasks()
