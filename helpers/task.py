"""contains the helper functions for the tasks and sessions"""

import glob
import importlib
import sys
from os.path import basename, dirname, isfile, join


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

    # @staticmethod
    # def int_input(varname, debug=False):
    #     """Get an integer input from the user."""
    #     while True:
    #         try:
    #             return int(input(f"Enter {varname}: "))
    #         except ValueError as err:
    #             if debug:
    #                 raise ValueError from err
    #             print("Invalid input. Please enter an integer.")

    # @staticmethod
    # def float_input(varname, debug=False):
    #     """Get a float input from the user."""
    #     while True:
    #         try:
    #             return float(input(f"Enter {varname}: "))
    #         except ValueError as err:
    #             if debug:
    #                 raise ValueError from err
    #             print("Invalid input. Please enter a float.")

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


def run_session(file, subdir=""):
    """Run all tasks in all files in directory of the file.
    Optional argument dir can be used to specify a child directory.
    Ignores main.py and files starting with _."""

    files = sorted(glob.glob(join(dirname(file), subdir, "*.py")))
    for _file in files:
        if not isfile(_file):
            continue
        fname = basename(_file)
        if _file.endswith("main.py") or fname.startswith("_"):
            continue
        subdir = subdir.replace("/", ".").replace("\\", ".")
        modname = f"{subdir}.{fname[:-3]}" if subdir else fname[:-3]
        importlib.import_module(modname)
        mod = sys.modules[modname]
        try:
            mod.Task(mod.__name__).run_tasks()
        except AttributeError as err:
            print(err)
        except ValueError as err:
            print(err)
        print("\n")
