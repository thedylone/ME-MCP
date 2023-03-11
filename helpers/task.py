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
        self.minval = minval
        self.minexc = minexc
        self.maxval = maxval
        self.maxexc = maxexc

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
    vartype,
    varname,
    validator=None,
    debug=False,
):
    """Get input from user and convert to vartype.
    Optional arguments minval and maxval can be used to specify a range."""
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

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        """Initialize a TaskBase object."""
        self.name = name
        self.output = output
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log(self.__doc__)
        self.log("################")

    def run_tasks(self):
        """Run all tasks in the tasklist."""
        for task in self.tasklist:
            self.log(task.__doc__)
            res = task(self)
            if res:
                self.log(task.__name__, **res)
            self.log("\n")
        self.log("done")
        self.log("################")

    def log(self, msg, **kwargs):
        """Print a message with variables.
        Checks if output is enabled."""
        if not self.output:
            return
        if not kwargs:
            print(msg)
            return msg
        var_list = []
        msg += ":"
        for key, value in kwargs.items():
            var_list.append(f"{key} = {value}")
        var_str = "; ".join(var_list)
        print(msg, var_str)
        return f"{msg} {var_str}"
