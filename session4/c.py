"""Count occurrences"""

import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list
from session4.b import Task as TaskB


class Task(TaskBase):
    """Count occurrences"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        task_b: TaskB = TaskB(output=False)
        task_b.run_tasks()
        self.combined_list: list[tuple[str, str, int]] = task_b.combined_list
        self.occ_list: list[tuple[int, int, list[str]]] = []

    @task_to_list(tasklist)
    def task1(self) -> dict[str, list[tuple[int, int, list[str]]]]:
        """Count the occurrences of every mark and form a list of tuples with:
        a) the numerical mark,
        b) the number of occurrences of that mark,
        c) the list of students who achieved that mark."""
        self.occ_list = []
        freq: int = 0
        students: list[str] = []
        current_mark: int = self.combined_list[0][2]
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
    def task2(self) -> None:
        """Plot graphically Occurrences vs Marks."""
        marks: list[int] = [int(t[0]) for t in self.occ_list]
        freq: list[int] = [t[1] for t in self.occ_list]
        plt.plot(marks, freq)
        plt.xlabel("Marks")
        plt.ylabel("Occurrences")
        plt.title("Occurrences vs Marks")
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
    for occ in task.occ_list:
        if occ[0] == "92":
            print(occ[1])
            break
