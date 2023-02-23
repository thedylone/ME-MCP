"""Object definition"""

from helpers.task import TaskBase, task_to_list
from session8.a import Cohort, Student, Registry
from session8.b import Task as TaskB


class Task(TaskBase):
    """Object definition"""

    tasklist = []
    taskB = TaskB(output=False)
    taskB.run_tasks()

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.list_me = []
        self.registry = Registry("Mechanical Engineering", [])

    @task_to_list(tasklist)
    def task1(self):
        """ME is a list of objects of class Cohort. There are four elements,
        one for each year entry: 2019, 2020, 2021 and 2022, respectively.
        Each element of ME is an object containing the year of the entry
        and a list of objects of class Student."""
        self.list_me = [Cohort(i, []) for i in range(2019, 2023)]
        with (
            open("session8/CIDs.txt", "r", encoding="utf-8") as cids,
            open("session8/Names.txt", "r", encoding="utf-8") as names,
            open("session8/Marks.txt", "r", encoding="utf-8") as marks,
        ):
            cids, names, marks = (
                cids.readlines(),
                names.readlines(),
                marks.readlines(),
            )
            for i, val in enumerate(cids):
                cid = int(val)
                index = min(cid // 2000, 3)
                student = Student(
                    cid,
                    names[i].strip(),
                    list(map(int, marks[i * 10 : i * 10 + 10])),
                )
                self.list_me[index].students.append(student)
                self.registry.enrolments.append(student)


if __name__ == "__main__":
    task = Task("C")
    task.run_tasks()
