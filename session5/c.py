"""Sorting data"""

import random

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Sorting data"""

    tasklist = []

    @staticmethod
    def sort_ascending(data):
        """Write a function that receives an array of numbers
        and returns the same array sorted in ascending order."""
        # return sorted(data)
        sorted_list = []
        for num in data:
            # binary search to find the insertion point
            left = 0
            right = len(sorted_list) - 1
            while left <= right:
                mid = (left + right) // 2
                if num < sorted_list[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            sorted_list.insert(left, num)
        return sorted_list

    @task_to_list(tasklist)
    def task1(self):
        """Write a function, SortAscending, that receives an array of numbers
        and returnsthe same array sorted in ascending order.
        Test the function by generating an array of 50 integer random numbers
        between 1 and 100 and sorting them."""
        data = [random.randint(1, 100) for _ in range(50)]
        data = self.sort_ascending(data)
        return {"data": data}


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
