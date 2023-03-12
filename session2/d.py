"""Conditional flow"""

import random
from helpers.task import TaskBase, get_input, task_to_list


class Player:
    """Player class with name and score attributes"""

    def __init__(self, name, score=0) -> None:
        self.name = name
        self.score: int = score

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.score


class Task(TaskBase):
    """Conditional flow"""

    tasklist: list = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.player_x: Player = Player(input("Enter Player X's name: "))
        self.player_y: Player = Player(input("Enter Player Y's name: "))

    @task_to_list(tasklist)
    def task1(self) -> dict[str, str | int]:
        """Two people intend to play dice.
        Input from the keyboard the names of these two people.
        Throw the dice once for each person. Establish who is the winner.
        Display the winner in the format 'Player X wins player Y'."""
        dice_x: int = random.randint(1, 6)
        dice_y: int = random.randint(1, 6)
        if dice_x > dice_y:
            out: int = 1
            res: str = f"{self.player_x} wins {self.player_y}"
        elif dice_x < dice_y:
            out = -1
            res = f"{self.player_y} wins {self.player_x}"
        else:
            out = 0
            res = "Draw"

        return {"out": out, "res": res}

    @task_to_list(tasklist)
    def task2(self) -> dict[str, str]:
        """The same two people throw the dice N times.
        Amend the previous script to allow so
        and count the winning games (not the scores) for each person.
        At the end display the winner in the format
        'Player X won x games, player Y won only y games'."""
        times: int = int(get_input(int, "N"))
        for _ in range(int(times)):
            roll: str | int = self.task1().get("out", 0)
            if roll == 1:
                self.player_x.score += 1
            elif roll == -1:
                self.player_y.score += 1

        win: Player
        lose: Player
        if int(self.player_x) >= int(self.player_y):
            win, lose = self.player_x, self.player_y
        else:
            win, lose = self.player_y, self.player_x
        out: str = (
            f"{win} won {int(win)} games, {lose} won only {int(lose)} games"
        )
        return {"winner": out}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()

    A: int = 0
    C: int = 1
    D: int = 2
    print((A == C or A > C) or (D < C))
