"""Adding mathematical fractions"""

from helpers.task import TaskBase, task_to_list, get_input


class Task(TaskBase):
    """Adding mathematical fractions"""

    tasklist: list = []

    @staticmethod
    def gcd(num_a: int, num_b: int) -> int:
        """Greatest Common Divisor"""
        if num_a == 0:
            return num_b
        return Task.gcd(num_b % num_a, num_a)

    @task_to_list(tasklist)
    def task1(self) -> dict[str, int]:
        """Write a recursive function, GCD(a,b), that evaluates
        the Greatest Common Divisor (i.e., the largest common factor)
        between two numbers, a and b."""
        num_a: int = get_input(int, "Enter the first number")
        num_b: int = get_input(int, "Enter the second number")
        return {"gcd": Task.gcd(num_a, num_b)}

    @staticmethod
    def lcm(num_a: int, num_b: int) -> int:
        """Least Common Multiple"""
        return (num_a * num_b) // Task.gcd(num_a, num_b)

    @task_to_list(tasklist)
    def task2(self) -> dict[str, int]:
        """Write a function, LCM(a,b), that evaluates
        the Least Common Multiple (i.e., the largest common factor)
        between two numbers, a and b."""
        num_a: int = get_input(int, "Enter the first number")
        num_b: int = get_input(int, "Enter the second number")
        return {"lcm": Task.lcm(num_a, num_b)}

    @staticmethod
    def add_fractions(list_n: list[int], list_d: list[int]) -> tuple[int, int]:
        """Add fractions"""
        num: int = 0
        denom: int = 1
        for i, val in enumerate(list_d):
            num *= val
            num += denom * list_n[i]
            denom *= val
        gcd: int = Task.gcd(num, denom)
        return num // gcd, denom // gcd

    @task_to_list(tasklist)
    def task3(self) -> dict[str, int]:
        """Write a function, AddFractions(N,D), that receives two lists of
        integer values, N and D, representing the numerators and denominators
        of some fractions, respectively, and returns two values, Nt and Dt.
        Ensure that the final fraction, Nt/Dt, is at its minimal form."""
        str_n: str = get_input(str, "Enter numerators separated by commas")
        str_d: str = get_input(str, "Enter denominators separated by commas")
        list_n: list[int] = [int(i) for i in str_n.split(",")]
        list_d: list[int] = [int(i) for i in str_d.split(",")]
        num: int
        denom: int
        num, denom = Task.add_fractions(list_n, list_d)
        return {"nt": num, "dt": denom}


if __name__ == "__main__":
    task: Task = Task("D")
    task.run_tasks()
    quiz_n: list[int] = [3, 1, 3, 2, 5, 7, 2, 4, 6, 1, 7, 4]
    quiz_d: list[int] = [4, 5, 8, 16, 2, 4, 32, 2, 4, 3, 36, 45]
    print(Task.add_fractions(quiz_n, quiz_d))
