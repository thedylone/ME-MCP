""""Lists: Dammit I'm mad!"""

import re

from helpers.task import TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Lists: Dammit I'm mad!"""

    tasklist: list = []

    @task_to_list(tasklist)
    def exercise3(self) -> dict[str, bool]:
        """Write a script to establish if a sequence of characters
        is palindrome. A word or sentence (excluding any punctuation,
        upper/lower case and blank spaces) is palindrome if it is
        the same when read from left to right or right to left.
        Input the word to be examined from the keyboard"""
        string: str = get_input(str, "string of characters").lower()
        string = re.sub("[^a-zA-Z0-9]", "", string)
        # return {"is palindrome": string == string[::-1]}
        front: int = 0
        back: int = len(string) - 1
        while front < back:
            if string[front] != string[back]:
                return {"is palindrome": False}
            front += 1
            back -= 1
        return {"is palindrome": True}


if __name__ == "__main__":
    task: Task = Task("Exercise 3")
    task.run_tasks()
