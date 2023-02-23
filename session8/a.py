"""Class definition and inheritance"""

from helpers.task import TaskBase


class Student:
    """Establish a class, Student, representing a student, with attributes:
    CID, name, list of marks and average mark"""

    def __init__(self, cid, name, marks):
        """Initialise the attributes"""
        self.cid = cid
        self.name = name
        self.marks = marks
        self.average = 0


class Cohort:
    """Establish a child class of Students, Cohort, representing a cohort, with
    attributes: year, list of students."""

    def __init__(self, year, students):
        """Initialise the attributes"""
        self.year = year
        self.students = students


class Registry:
    """Establish a child class of Students, Registry, representing the
    entirety of the student population and their academic results, with
    attributes: department and enrolments."""

    def __init__(self, department, enrolments):
        """Initialise the attributes"""
        self.department = department
        self.enrolments = enrolments


class Task(TaskBase):
    """Class definition and inheritance"""


if __name__ == "__main__":
    task = Task("A")
    task.run_tasks()
