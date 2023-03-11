"""contains the helper class and functions for the sessions"""

import glob
import importlib
import sys
from os.path import basename, dirname, isfile, join


class SessionBase:
    """Base class for sessions."""

    def __init__(self, name, file=__file__, subdir=""):
        self.name = name
        print(f"running {self.name}...")
        SessionBase.run_session(file=file, subdir=subdir)

    @staticmethod
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
