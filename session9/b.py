"""Defining and manipulating matrices"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Defining and manipulating matrices"""

    tasklist = []

    @task_to_list(tasklist)
    def task1(self):
        """Create a matrix H of zeros with dimensions 30 x 20"""
        self.matrix_H = []
        for i in range(30):
            self.matrix_H.append([0] * 20)
        return {"H": self.matrix_H}

    @task_to_list(tasklist)
    def task2(self):
        """Insert values 50 to 69 into the 6th row of H."""
        self.matrix_H[5] = list(range(50, 70))
        return {"H": self.matrix_H}

    @task_to_list(tasklist)
    def task3(self):
        """Insert values 100 to 129 into the 8th column of H."""
        for i in range(30):
            self.matrix_H[i][7] = i + 100
        return {"H": self.matrix_H}

    @task_to_list(tasklist)
    def task4(self):
        """Generate a a square matrix S, of dimension N x N,
        with the following pattern:
        [
        [1 0 0 0 0 1]
        [0 1 0 0 1 0]
        [0 0 1 1 0 0]
        [0 0 1 1 0 0]
        [0 1 0 0 1 0]
        [1 0 0 0 0 1]
        ]
        """
        dimension = get_input(int, "dimension")
        self.matrix_S = []
        for i in range(dimension):
            row = [0] * dimension
            row[i] = 1
            row[-i-1] = 1
            self.matrix_S.append(row)
        return {"S": self.matrix_S}


if __name__ == "__main__":
    task = Task("B")
    task.run_tasks()
