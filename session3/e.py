"""Series expansions"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Series expansions"""

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.x_input = TaskBase.float_input("xp")
        if abs(self.x_input) > 1:
            raise ValueError("xp must be in [-1, 1]")
        self.q_input = TaskBase.int_input("Q")
        self.accuracy = 10**-self.q_input
        self.approx = 0

    @task_to_list(tasklist)
    def task1(self):
        """Given the series in Task D write a script to calculate a
        finite approximation of such function at a given point xp, i.e. y(xp).
        Add terms of the series until approximation reaches a given accuracy.
        The accuracy is reached when |y_n+1 - y_n| < 10^-Q."""
        index = -1
        term = 1
        while term >= self.accuracy:
            self.approx += term
            index += 1
            term *= self.x_input
        return {"approximation": self.approx, "limit": index}

    @task_to_list(tasklist)
    def task2(self):
        """Evaluate the exact value of y(xp),
        and display the error from the computed value.
        Observe the value of the error against 10^-Q."""
        true_y = 1 / (1 - self.x_input)
        error = self.approx - true_y
        return {"true_y": true_y, "error": error}


if __name__ == "__main__":
    task = Task("E")
    task.run_tasks()
