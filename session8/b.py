"""Method definition"""

from helpers.task import TaskBase, task_to_list
from session8.a import Student, Cohort, Registry


# Student class
def get_average(self):
    """Within the class Student, write a method, Average, to determine the
    average mark of the student."""
    avg = sum(self.marks) / len(self.marks)
    self.average = avg
    return avg


def get_classify(self):
    """Within the class Student, write a method, Classify, to determine mark
    result classification of a student."""
    avg = self.get_average()
    classifications = [("1st", 70), ("2.1", 60), ("2.2", 50), ("3rd", 40)]
    out = "Fail"
    for classification, mark in classifications:
        if avg >= mark:
            out = classification
            break
    return out


# Cohort class
def sort_students(self):
    """Sort the students by average mark"""
    self.students.sort(key=lambda x: x.get_average(), reverse=True)


def sort_students_decorator(func):
    """Decorator to sort students by average mark"""

    def wrapper(self):
        self.sort_students()
        return func(self)

    return wrapper


@sort_students_decorator
def best_student(self):
    """Within the class Cohort, write a method to determine the name of the
    best student of the cohort."""
    return self.students[0].name


@sort_students_decorator
def deans(self):
    """Within the class Cohort, write a method to determine the Dean’s List
    (top 10% students)."""
    out = []
    slow = 0
    fast = 10
    while fast < len(self.students):
        out.append(self.students[slow])
        slow += 1
        fast += 10
    return out


# Registry class
def get_stats(self, clss):
    """Within the class Registry, write a method, Statistics, to determine the
    number of all students with a given classification."""
    return len([s for s in self.enrolments if s.get_classify() == clss])


class Task(TaskBase):
    """Method definition"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Within the class Student, write a method to
        determine the average mark of the student and a method to
        determine mark result classification of a student"""
        Student.get_average = get_average
        Student.get_classify = get_classify

    @task_to_list(tasklist)
    def task2(self):
        """Within the class Cohort, write a method to determine
        the name of the best student of the cohort and a method to
        determine the Dean's List (top 10% students)."""
        Cohort.sort_students = sort_students
        Cohort.best_student = best_student
        Cohort.deans = deans

    @task_to_list(tasklist)
    def task3(self):
        """Within the class Registry, write a method to determine
        the number of all students with a given classification."""
        Registry.get_stats = get_stats


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
