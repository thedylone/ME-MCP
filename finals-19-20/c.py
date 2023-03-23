"""Task C"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Task C"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.total: int = 0
        self.weekly: list[int] = []
        self.exceeded: list[str] = []
        self.increment: list[float] = []
        self.max_week: int = 1

    @task_to_list(tasklist)
    def task1(self) -> None:
        """The file CV19.txt contains the number of COVID-19 infections
        per day in the UK, between the period from 02.03.20 to 31.05.20.
        The data in the file are organised sequentially as:
        Week 1;
        Day 1 date;
        Number of infections;
        Day 2 date;
        Number of infections; ...
        Write a script (name the file ExC) to determine and print out:
        1. The overall number of infections registered in the given period
        2. The weekly number of infections per every week provided
        3. The list of days when the number of infected people exceeded 2000
        4. The weekly percentage increment of infections (apart from week 1)
        increment in % = (wn - wn-1) / wn-1 * 100,
        where wn is the number of infections in week n
        5. The week with the highest number of infections
        """

        week_running: int = 0
        date: str = ""

        with open("finals-19-20/CV19.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("Week"):
                    self.total += week_running
                    self.weekly.append(week_running)
                    week_running = 0
                    continue
                if date == "":
                    date = line.strip()
                    continue
                number: int = int(line.strip())
                if number > 2000:
                    self.exceeded.append(date)
                week_running += number
                date = ""

        self.total += week_running
        self.weekly.append(week_running)
        self.weekly.pop(0)
        self.increment: list[float] = [
            (self.weekly[i] - self.weekly[i - 1]) / self.weekly[i - 1] * 100
            for i in range(1, len(self.weekly))
        ]
        self.max_week = self.weekly.index(max(self.weekly)) + 1

        print(f"1. {self.total}")
        print(f"2. {self.weekly}")
        print(f"3. {self.exceeded}")
        print(f"4. {self.increment}")
        print(f"5. Week {self.max_week}")


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
    assert task.total == 273319
    assert task.weekly == [
        241,
        1118,
        3623,
        12075,
        24814,
        37088,
        35226,
        34160,
        33883,
        33000,
        24901,
        17518,
        15672,
    ]
    assert task.exceeded == [
        "2020-03-27",
        "2020-03-28",
        "2020-03-29",
        "2020-03-30",
        "2020-03-31",
        "2020-04-01",
        "2020-04-02",
        "2020-04-03",
        "2020-04-04",
        "2020-04-05",
        "2020-04-06",
        "2020-04-07",
        "2020-04-08",
        "2020-04-09",
        "2020-04-10",
        "2020-04-11",
        "2020-04-12",
        "2020-04-13",
        "2020-04-14",
        "2020-04-15",
        "2020-04-16",
        "2020-04-17",
        "2020-04-18",
        "2020-04-19",
        "2020-04-20",
        "2020-04-21",
        "2020-04-22",
        "2020-04-23",
        "2020-04-24",
        "2020-04-25",
        "2020-04-26",
        "2020-04-27",
        "2020-04-28",
        "2020-04-29",
        "2020-04-30",
        "2020-05-01",
        "2020-05-02",
        "2020-05-03",
        "2020-05-04",
        "2020-05-05",
        "2020-05-06",
        "2020-05-07",
        "2020-05-08",
        "2020-05-09",
        "2020-05-10",
        "2020-05-11",
        "2020-05-12",
        "2020-05-13",
        "2020-05-14",
        "2020-05-15",
        "2020-05-16",
        "2020-05-17",
        "2020-05-18",
        "2020-05-19",
        "2020-05-20",
        "2020-05-22",
        "2020-05-23",
        "2020-05-24",
        "2020-05-25",
        "2020-05-27",
        "2020-05-28",
        "2020-05-30",
    ]
    assert task.increment == [
        363.9004149377593,
        224.06082289803223,
        233.28733094120895,
        105.49896480331262,
        49.464012251148546,
        -5.020491803278689,
        -3.026173848861636,
        -0.8108899297423887,
        -2.60602662101939,
        -24.542424242424243,
        -29.64941167021405,
        -10.537732617878753,
    ]
    assert task.max_week == 6
