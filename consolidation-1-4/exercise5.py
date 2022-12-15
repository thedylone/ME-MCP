"""Lists and Tuples"""

from helpers.task import TaskBase, task_to_list


class Task(TaskBase):
    """Lists and Tuples"""

    tasklist = []

    @task_to_list(tasklist)
    def exercise5(self):
        """The budget of a company (in thousands pounds) for year 2018
        is stored in the file Budget.txt with the following numerical format
        1 this month
        4 num. of expenses this month
        5.5 expenses 1
        15.5 expenses 2
        2.3 expenses 3
        4.5 expenses 4
        3 num. of incomes this month
        2.6 income 1
        4.8 income 2
        1.0 income 3
        2 this month
        3 num. of expenses this month
        2.5 expenses 1
        etc
        Write a script to read the file and organise the data
        in a list of tuples: (month, total expenses, total incomes)
        For every month compute the total savings
        and store them in the file Savings.txt.
        """
        current_month = -1
        expenses_num = -1
        income_num = -1
        current_expenses = 0
        current_income = 0
        savings = []
        with open("consolidation-1-4/Budget.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                # print(line)
                if current_month == -1:
                    current_month = int(line)
                    continue
                if expenses_num == -1:
                    expenses_num = int(line)
                    continue
                if expenses_num > 0:
                    current_expenses += float(line)
                    expenses_num -= 1
                    continue
                if income_num == -1:
                    income_num = int(line)
                    continue
                if income_num > 0:
                    current_income += float(line)
                    income_num -= 1
                    continue
                if expenses_num == 0 and income_num == 0:
                    savings.append(current_income - current_expenses)
                    current_month = int(line)
                    expenses_num = -1
                    income_num = -1
                    current_expenses = 0
                    current_income = 0
            savings.append(current_income - current_expenses)

        with open("consolidation-1-4/Savings.txt", "w", encoding="utf-8") as f:
            for month in savings:
                f.write(f"{month}\n")
        return {"savings": savings}


if __name__ == "__main__":
    task = Task("Exercise 5")
    task.run_tasks()
