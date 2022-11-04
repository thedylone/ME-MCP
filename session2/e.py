from helpers.task import TaskBase


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.N = 0
        self.inside = 0
        self.outside = 0
        self.inside_pts = []
        self.outside_pts = []

    @TaskBase.task_to_list(tasklist)
    def getNPoints(self):
        self.N = int(input("Enter number of points: "))

    @TaskBase.task_to_list(tasklist)
    def task1(self, pts=None):
        import random

        for _ in range(int(self.N)):
            x = random.random()
            y = random.random()
            if x * x + y * y <= 1:
                self.inside += 1
                if pts:
                    self.inside_pts.append((x, y))
            else:
                self.outside += 1
                if pts:
                    self.outside_pts.append((x, y))
        pi = 4 * self.inside / (self.inside + self.outside)
        return {"pi": pi}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        import matplotlib.pyplot as plt

        self.getNPoints()
        self.task1(pts=True)

        s = min(max(5000 / self.inside, 1), 50)

        plt.scatter(*zip(*self.inside_pts), color="red", s=s)
        plt.scatter(*zip(*self.outside_pts), color="blue", s=s)
        plt.gca().set_aspect("equal", adjustable="box")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.show()


if __name__ == "__main__":
    task = Task("E")
    task.runTasks()

    import random

    rand = [random.random() * 6 - 3 for _ in range(50)]
    print(min(rand), max(rand))
