"""Using methods"""

from helpers.task import TaskBase, task_to_list
from year1.session8.a import Cohort, Registry
from year1.session8.c import Task as TaskC


class Task(TaskBase):
    """Using methods"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        task_c: TaskC = TaskC(output=False)
        task_c.run_tasks()
        self.list_me: list[Cohort] = task_c.list_me
        self.registry: Registry = task_c.registry

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str]:
        """Determine and print out the name of
        the top student for each cohort."""
        return {str(c.year): c.best_student() for c in self.list_me}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, list[str]]:
        """Determine and print the list of names of students
        entering the Dean's List."""
        return {str(c.year): [s.name for s in c.deans()] for c in self.list_me}

    @task_to_list(tasklist)
    def task3(self) -> dict[str, str]:
        """For every student in Mech. Eng., print out the name and the average
        mark classification."""
        return {s.name: s.get_classify() for s in self.registry.enrolments}

    @task_to_list(tasklist)
    def task4(self) -> dict[str, int]:
        """Determine how many students overall in Mech. Eng. have achieved a
        First, a 2.1 and a 2.2, based on their marks average."""
        return {
            "1st": self.registry.get_stats("1st"),
            "2.1": self.registry.get_stats("2.1"),
            "2.2": self.registry.get_stats("2.2"),
        }


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
