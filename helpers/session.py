"""contains the helper class and functions for the sessions"""

import glob
import importlib
import sys
from os.path import basename, dirname, isfile, join
from types import ModuleType


class SessionBase:
    """Base class for sessions."""

    def __init__(self, name: str, file=__file__, subdir="") -> None:
        self.name: str = name
        print(f"running {self.name}...")
        SessionBase.run_session(file=file, subdir=subdir)

    @staticmethod
    def run_session(file: str, subdir: str = "") -> None:
        """Run all tasks in all files in directory of the file.
        Optional argument dir can be used to specify a child directory.
        Ignores main.py and files starting with _."""

        files: list[str] = sorted(
            glob.glob(join(dirname(file), subdir, "*.py"))
        )
        for _file in files:
            if not isfile(_file):
                continue
            fname: str = basename(_file)
            if _file.endswith("main.py") or fname.startswith("_"):
                continue
            sdir: str = subdir.replace("/", ".").replace("\\", ".")
            modname: str = f"{sdir}.{fname[:-3]}" if sdir else fname[:-3]
            importlib.import_module(modname)
            mod: ModuleType = sys.modules[modname]
            try:
                mod.Task(mod.__name__).run_tasks()
            except AttributeError as err:
                print(err)
            except ValueError as err:
                print(err)
            print("\n")
