"""Sorting data"""

import random
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Sorting data"""

    tasklist: list = []

    @staticmethod
    def sort_ascending(array: list[int | float]) -> list[int | float]:
        """Write a function that receives an array of numbers
        and returns the same array sorted in ascending order."""
        # return sorted(data)
        sorted_list: list[int | float] = []
        for num in array:
            # binary search to find the insertion point
            left: int = 0
            right: int = len(sorted_list) - 1
            while left <= right:
                mid: int = (left + right) // 2
                if num < sorted_list[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            sorted_list.insert(left, num)
        return sorted_list

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[int | float]]:
        """Write a function, SortAscending, that receives an array of numbers
        and returnsthe same array sorted in ascending order.
        Test the function by generating an array of 50 integer random numbers
        between 1 and 100 and sorting them."""
        array: list[int | float] = [random.randint(1, 100) for _ in range(50)]
        array = self.sort_ascending(array)
        return {"data": array}


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
    with open("session5/Set.txt", "r", encoding="utf-8") as f:
        data: list[int | float] = [int(line) for line in f]
    print(Task.sort_ascending(data)[124])
