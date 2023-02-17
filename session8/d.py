"""Using methods"""

from helpers.task import TaskBase, task_to_list
from session8.c import Task as TaskC


class Task(TaskBase):
    """Using methods"""

    tasklist = []
    taskC = TaskC(output=False)
    taskC.run_tasks()
    list_me = taskC.list_me
    registry = taskC.registry

    @task_to_list(tasklist)
    def task1(self):
        """Determine and print out the name of
        the top student for each cohort."""
        return {str(c.year): c.best_student() for c in self.list_me}

    @task_to_list(tasklist)
    def task2(self):
        """Determine and print the list of names of students
        entering the Dean's List."""
        return {str(c.year): [s.name for s in c.deans()] for c in self.list_me}

    @task_to_list(tasklist)
    def task3(self):
        """For every student in Mech. Eng., print out the name and the average
        mark classification."""
        return {s.name: s.get_classify() for s in self.registry.enrolments}

    @task_to_list(tasklist)
    def task4(self):
        """Determine how many students overall in Mech. Eng. have achieved a
        First, a 2.1 and a 2.2, based on their marks average."""
        return {
            "1st": self.registry.get_stats("1st"),
            "2.1": self.registry.get_stats("2.1"),
            "2.2": self.registry.get_stats("2.2"),
        }


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()
