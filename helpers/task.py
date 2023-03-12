"""contains the helper class and functions for the tasks"""


def task_to_list(tasklist):
    """Decorator to add a function to a list of tasks.
    Function should return a dictionary of variables to log."""

    def subtask(func):
        tasklist.append(func)
        return func

    return subtask


class RangeValidator:
    """Class to validate a range of values."""

    def __init__(self, minval=None, minexc=False, maxval=None, maxexc=False):
        self.minval: float | None = minval
        self.minexc: bool = minexc
        self.maxval: float | None = maxval
        self.maxexc: bool = maxexc

    def __call__(self, value):
        if self.minval is not None:
            if self.minexc:
                if value <= self.minval:
                    raise ValueError(f"Must be greater than {self.minval}")
            elif value < self.minval:
                raise ValueError(f"Must be at least {self.minval}")
        if self.maxval is not None:
            if self.maxexc:
                if value >= self.maxval:
                    raise ValueError(f"Must be less than {self.maxval}")
            elif value > self.maxval:
                raise ValueError(f"Must be at most {self.maxval}")
        return value


def get_input(
    vartype: type,
    varname: str,
    validator: RangeValidator | None = None,
    debug: bool = False,
):
    """Get input from user and convert to vartype.
    If validator is not None, validate the input with the validator."""
    while True:
        try:
            value = vartype(input(f"{varname}: "))
            if validator is not None:
                value = validator(value)
            return value
        except ValueError as err:
            if debug:
                raise ValueError from err
            print(err)


class TaskBase:
    """Base class for tasks."""

    tasklist: list = []

    def __init__(self, name: str = "", output: bool = True) -> None:
        """Initialize a TaskBase object."""
        self.name: str = name
        self.output: bool = output
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log(self.__doc__ or "Task")
        self.log("################")

    def run_tasks(self) -> None:
        """Run all tasks in the tasklist."""
        for task in self.tasklist:
            self.log(task.__doc__)
            res: dict = task(self)
            if res:
                self.log(task.__name__, **res)
            self.log("\n")
        self.log("done")
        self.log("################")

    def log(self, msg: str, **kwargs) -> str | None:
        """Print a message with variables.
        Checks if output is enabled."""
        if not self.output:
            return None
        if not kwargs:
            print(msg)
            return msg
        var_list: list = []
        msg += ":"
        for key, value in kwargs.items():
            var_list.append(f"{key} = {value}")
        var_str: str = "; ".join(var_list)
        print(msg, var_str)
        return f"{msg} {var_str}"
