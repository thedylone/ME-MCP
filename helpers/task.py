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


class TaskBase:
    """Base class for tasks."""

    tasklist = []

    def __init__(self, name="", output=True) -> None:
        """Initialize a TaskBase object."""
        self.name = name
        self.output = output
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log("################")

    @staticmethod
    def int_input(varname, debug=False):
        """Get an integer input from the user."""
        while True:
            try:
                return int(input(f"Enter {varname}: "))
            except ValueError as err:
                if debug:
                    raise ValueError from err
                print("Invalid input. Please enter an integer.")

    def run_tasks(self):
        """Run all tasks in the tasklist."""
        for task in self.tasklist:
            res = task(self)
            if res:
                self.log(task.__name__, **res)
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
