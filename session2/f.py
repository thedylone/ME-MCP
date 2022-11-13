from helpers.task import TaskBase
import time


class Task(TaskBase):
    tasklist = []

    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.N = TaskBase.int_input("N")

    @TaskBase.task_to_list(tasklist)
    def recursive(self):
        def getPrimes(n):
            if n < 2:
                return []
            primes = getPrimes(n - 1)
            if not any(n % p == 0 for p in primes):
                primes.append(n)
            return primes

        start = time.time()
        try:
            primes = getPrimes(self.N)
        except RecursionError as e:
            return {"error": e}
        end = time.time()
        return {"primes": primes, "time": end - start}

    @TaskBase.task_to_list(tasklist)
    def iterative(self):
        import math

        def isPrime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    return False
            return True

        start = time.time()
        primes = [i for i in range(self.N) if isPrime(i)]
        end = time.time()
        return {"primes": primes, "time": end - start}

    @TaskBase.task_to_list(tasklist)
    def sieve(self):
        import math

        start = time.time()
        primes = [True] * (self.N + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(self.N)) + 1):
            if primes[i]:
                for j in range(i * i, self.N + 1, i):
                    primes[j] = False

        primes = [i for i, v in enumerate(primes) if v]
        end = time.time()
        return {"primes": primes, "time": end - start}

    @TaskBase.task_to_list(tasklist)
    def from2(self):
        import numpy
        import math

        start = time.time()
        sieve = numpy.ones(self.N // 3 + (self.N % 6 == 2), dtype=bool)
        for i in range(1, int(math.sqrt(self.N)) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3 :: 2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = False
        primes = numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]
        end = time.time()
        return {"primes": primes, "time": end - start}


if __name__ == "__main__":
    task = Task("F")
    task.run_tasks()
    print(len(task.from2()["primes"]))
