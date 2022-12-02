"""Count occurrences"""

import matplotlib.pyplot as plt

import session4.b
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Count occurrences"""

    tasklist = []

    TaskB = session4.b.Task(output=False)
    TaskB.run_tasks()
    combined_list = TaskB.combined_list
    occ_list = []

    @task_to_list(tasklist)
    def task1(self):
        """Count the occurrences of every mark and form a list of tuples with:
        a) the numerical mark,
        b) the number of occurrences of that mark,
        c) the list of students who achieved that mark."""
        self.occ_list = []
        freq = 0
        students = []
        current_mark = self.combined_list[0][2]
        for tup in self.combined_list:
            if tup[2] == current_mark:
                freq += 1
                students.append(tup[0])
            else:
                self.occ_list.append((current_mark, freq, students))
                current_mark = tup[2]
                freq = 1
                students = [tup[0]]
        self.occ_list.append((current_mark, freq, students))
        return {"occ_list head": self.occ_list[:5]}

    @task_to_list(tasklist)
    def task2(self):
        """Plot graphically Occurrences vs Marks."""
        marks = [int(t[0]) for t in self.occ_list]
        freq = [t[1] for t in self.occ_list]
        plt.plot(marks, freq)
        plt.xlabel("Marks")
        plt.ylabel("Occurrences")
        plt.title("Occurrences vs Marks")
        plt.show()


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
    for occ in task.occ_list:
        if occ[0] == "92":
            print(occ[1])
            break
