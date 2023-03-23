"""Task C"""

import matplotlib.pyplot as plt
from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Task C"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.first_doses: list[int] = []
        self.second_doses: list[int] = []
        self.pfizer: int = 0
        self.astrazeneca: int = 0
        self.largest_day: str = ""

    @task_to_list(tasklist)
    def task1(self) -> None:
        """The file Vax.txt contains the statistics of COVID-19 vaccinations
        in the UK, for the days in the period from 11.01.21 to 23.03.21.
        The data in the file are organised sequentially as:
        Day 1
        First dose vaccinations with Pfizer
        First dose vaccinations with AstraZeneca
        Second dose vaccinations with Pfizer
        Second dose vaccinations with AstraZeneca
        Day 2
        First dose vaccinations with Pfizer
        First dose vaccinations with AstraZeneca
        Second dose vaccinations with Pfizer
        Second dose vaccinations with AstraZeneca
        ...
        Write a script to determine and print out (in this order):
        1. The overall number of first dose vaccinations inoculated
        2. The overall number of second dose vaccinations inoculated
        3. The day with the largest overall number of vaccinations
        4. The overall number of vaccinations done with Pfizer and those
        with AstraZeneca
        Plot graphically, on the same plot:
        1. The number of first doses per each day
        2. The number of second doses per each day"""
        days: list[str] = []
        counter = 0
        with open("finals-20-21/Vax.txt", "r", encoding="utf-8") as file:
            for line in file:
                if counter % 5 == 0:
                    days.append(line.strip())
                elif counter % 5 == 1:
                    self.first_doses.append(int(line))
                    self.pfizer += int(line)
                elif counter % 5 == 2:
                    self.first_doses[-1] += int(line)
                    self.astrazeneca += int(line)
                elif counter % 5 == 3:
                    self.second_doses.append(int(line))
                    self.pfizer += int(line)
                elif counter % 5 == 4:
                    self.second_doses[-1] += int(line)
                    self.astrazeneca += int(line)
                counter += 1

        combined = list(zip(self.first_doses, self.second_doses))
        self.largest_day = days[combined.index(max(combined))]
        print(f"1. {sum(self.first_doses)}")
        print(f"2. {sum(self.second_doses)}")
        print(f"3. {self.largest_day}")
        print(f"4. Pfizer: {self.pfizer}, AstraZeneca: {self.astrazeneca}")

        plt.bar(days, self.first_doses, label="First Doses")
        plt.bar(days, self.second_doses, label="Second Doses")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    task: Task = Task("C")
    task.run_tasks()
    assert sum(task.first_doses) == 26366879
    assert sum(task.second_doses) == 2141368
    assert task.largest_day == "20/03/2021"
    assert task.pfizer == 13859388
    assert task.astrazeneca == 14648859
