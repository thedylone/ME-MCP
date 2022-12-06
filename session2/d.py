"""Conditional flow"""

import random

from helpers.task import TaskBase, get_input, task_to_list


class Player:
    """Player class with name and score attributes"""

    def __init__(self, name, score=0) -> None:
        self.name = name
        self.score = score

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.score


class Task(TaskBase):
    """Conditional flow"""

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.X = Player(input("Enter Player X's name: "))
        self.Y = Player(input("Enter Player Y's name: "))

    @task_to_list(tasklist)
    def task1(self):
        """Two people intend to play dice.
        Input from the keyboard the names of these two people.
        Throw the dice once for each person. Establish who is the winner.
        Display the winner in the format 'Player X wins player Y'."""
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

    @task_to_list(tasklist)
    def task2(self):
        """The same two people throw the dice N times.
        Amend the previous script to allow so
        and count the winning games (not the scores) for each person.
        At the end display the winner in the format
        'Player X won x games, player Y won only y games'."""
        times = get_input(int, "N")
        for _ in range(int(times)):
            roll = self.task1().get("out", 0)
            if roll == 1:
                self.X.score += 1
            elif roll == -1:
                self.Y.score += 1

        if int(self.X) >= int(self.Y):
            win, lose = self.X, self.Y
        else:
            win, lose = self.Y, self.X
        out = f"{win} won {int(win)} games, {lose} won only {int(lose)} games"
        return {"winner": out}


if __name__ == "__main__":
    task = Task("D")
    task.run_tasks()

    a = 0
    c = 1
    d = 2
    print((a == c or a > c) or (d < c))
