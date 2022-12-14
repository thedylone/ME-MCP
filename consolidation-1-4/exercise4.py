"""Lists: Anagrams"""

from helpers.task import TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Lists: Anagrams"""

    tasklist = []

    @task_to_list(tasklist)
    def exercise4(self):
        """Given two strings, write a script to determine whether
        one string is the anagram of the other."""
        string1 = get_input(str, "string 1").lower()
        string2 = get_input(str, "string 2").lower()
        return {"is anagram": sorted(string1) == sorted(string2)}


if __name__ == "__main__":
    task = Task("Exercise 4")
    task.run_tasks()
