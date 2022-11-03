class TaskBase:
    def __init__(self, name, output=True) -> None:
        """Initialize a TaskBase object."""
        self.name = name
        self.output = output

    def task_to_list(list):
        """Decorator to add a function to a list of tasks.
        Function should return a dictionary of variables to log."""

        def subtask(func):
            list.append(func)
            return func

        return subtask

    def runTasks(self):
        """Run all tasks in the tasklist."""
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log("################")
        for task in self.tasklist:
            res = task(self)
            if res:
                self.log(task.__name__, **res)
        self.log("done")
        self.log("################")

    def log(self, msg, **vars):
        """Print a message with variables.
        Checks if output is enabled."""
        if not self.output:
            return
        if not vars:
            print(msg)
            return
        var_list = []
        msg += ":"
        for key, value in vars.items():
            var_list.append(f"{key} = {value}")
        var_str = "; ".join(var_list)
        print(msg, var_str)


def runSession(file):
    """Run all tasks in all files in the same directory as file.
    Ignores main.py and files starting with _."""
    from os.path import dirname, basename, isfile, join
    import glob
    import importlib
    import sys

    files = glob.glob(join(dirname(file), "*.py"))
    for f in files:
        if not isfile(f):
            continue
        fname = basename(f)
        if f.endswith("main.py") or fname.startswith("_"):
            continue
        importlib.import_module(fname[:-3])
        mod = sys.modules[fname[:-3]]
        try:
            mod.Task(mod.__name__).runTasks()
        except Exception as e:
            print(e)
        print("\n")
