from helpers.task import TaskBase


class Player:
    def __init__(self, name, score=0) -> None:
        self.name = name
        self.score = score

    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.score

    def __eq__(self, other) -> bool:
        return self.score == other

    def __lt__(self, other) -> bool:
        return self.score < other

    def __gt__(self, other) -> bool:
        return self.score > other

    def __le__(self, other) -> bool:
        return self.score <= other

    def __ge__(self, other) -> bool:
        return self.score >= other


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.X = None
        self.Y = None

    @TaskBase.task_to_list(tasklist)
    def getPlayerNames(self):
        self.X = Player(input("Enter Player X's name: "))
        self.Y = Player(input("Enter Player Y's name: "))

    @TaskBase.task_to_list(tasklist)
    def task1(self):
        import random

        dice_x = random.randint(1, 6)
        dice_y = random.randint(1, 6)
        if dice_x > dice_y:
            out = 1
            res = f"{self.X} wins {self.Y}"
        elif dice_x < dice_y:
            out = -1
            res = f"{self.Y} wins {self.X}"
        else:
            out = 0
            res = "Draw"

        return {"out": out, "res": res}

    @TaskBase.task_to_list(tasklist)
    def task2(self):
        n = input("Enter number of rounds: ")
        for _ in range(int(n)):
            roll = self.task1().get("out", 0)
            if roll == 1:
                self.X.score += 1
            elif roll == -1:
                self.Y.score += 1

        win = self.X if self.X >= self.Y else self.Y
        lose = self.Y if self.X >= self.Y else self.X
        out = f"{win} won {int(win)} games, {lose} won only {int(lose)} games"
        return {"winner": out}


if __name__ == "__main__":
    task = Task("D")
    task.runTasks()

    a = 0
    c = 1
    d = 2
    print((a == c or a > c) or (d < c))
