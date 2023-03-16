"""Class definition and inheritance"""

from collections.abc import Callable
from helpers.task import TaskBase


class Student:
    """Establish a class, Student, representing a student, with attributes:
    CID, name, list of marks and average mark"""

    get_average: Callable[..., float]
    get_classify: Callable[..., str]

    def __init__(self, cid: int, name: str, marks: list[int]) -> None:
        """Initialise the attributes"""
        self.cid: int = cid
        self.name: str = name
        self.marks: list[int] = marks
        self.average: float = 0


class Cohort:
    """Establish a child class of Students, Cohort, representing a cohort, with
    attributes: year, list of students."""

    sort_students: Callable[..., None]
    best_student: Callable[..., str]
    deans: Callable[..., list[Student]]

    def __init__(self, year: int, students: list[Student]) -> None:
        """Initialise the attributes"""
        self.year: int = year
        self.students: list[Student] = students


class Registry:
    """Establish a child class of Students, Registry, representing the
    entirety of the student population and their academic results, with
    attributes: department and enrolments."""

    get_stats: Callable[..., int]

    def __init__(self, department: str, enrolments: list[Student]) -> None:
        """Initialise the attributes"""
        self.department: str = department
        self.enrolments: list[Student] = enrolments


class Task(TaskBase):
    """Class definition and inheritance"""


if __name__ == "__main__":
    task: Task = Task("A")
    task.run_tasks()
