"""Prime numbers"""

import math
import time
import numpy
from helpers.task import TaskBase, get_input, task_to_list


class Task(TaskBase):
    """Prime numbers"""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        super().__init__(name, output)
        self.limit: int = get_input(int, "N")

    @task_to_list(tasklist)
    def recursive(self):
        """Generate a list with all the prime numbers up to N. [recursive]"""

        def get_primes(limit: int) -> list:
            if limit < 2:
                return []
            primes: list = get_primes(limit - 1)
            if not any(limit % p == 0 for p in primes):
                primes.append(limit)
            return primes

        start: float = time.time()
        try:
            primes: list = get_primes(self.limit)
        except RecursionError as err:
            return {"error": err}
        end: float = time.time()
        return {"primes": primes, "time": end - start}

    @task_to_list(tasklist)
    def iterative(self):
        """Generate a list with all the prime numbers up to N. [iterative]"""

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True

        start: float = time.time()
        primes: list[int] = [i for i in range(self.limit) if is_prime(i)]
        end: float = time.time()
        return {"primes": primes, "time": end - start}

    @task_to_list(tasklist)
    def sieve(self):
        """Generate a list with all the prime numbers up to N. [sieve]"""
        if self.limit < 2:
            return {"primes": []}
        start: float = time.time()
        is_prime: list[bool] = [True] * (self.limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(self.limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, self.limit + 1, i):
                    is_prime[j] = False

        primes: list[int] = [i for i, v in enumerate(is_prime) if v]
        end: float = time.time()
        return {"primes": primes, "time": end - start}

    @task_to_list(tasklist)
    def from2(self):
        """Generate a list with all the prime numbers up to N. [from 2]"""
        if self.limit < 2:
            return {"primes": []}
        start: float = time.time()
        sieve: numpy.ndarray = numpy.ones(
            self.limit // 3 + (self.limit % 6 == 2), dtype=bool
        )
        for i in range(1, int(math.sqrt(self.limit)) // 3 + 1):
            if sieve[i]:
                k: int = 3 * i + 1 | 1
                sieve[k * k // 3 :: 2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = False
        primes = numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]
        end: float = time.time()
        return {"primes": primes, "time": end - start}


if __name__ == "__main__":
    task: Task = Task("F")
    task.run_tasks()
    print(len(task.from2()["primes"]))
