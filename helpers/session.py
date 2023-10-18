"""contains the helper class and functions for the sessions"""

import importlib
import sys
from pathlib import Path
from types import ModuleType


class SessionBase:
    """Base class for sessions."""

    def __init__(self, name: str, file=__file__, subdir="") -> None:
        self.name: str = name
        print(f"running {self.name}...")
        SessionBase.run_session(Path(file).parent, subdir=subdir)

    @staticmethod
    def run_session(directory: Path, subdir: str = "") -> None:
        """Run all tasks in all files in directory of the file.
        Optional argument dir can be used to specify a child directory.
        Ignores main.py and files starting with _."""

        if subdir:
            directory = directory / subdir
        files: list[Path] = sorted(directory.glob("*.py"))
        for file in files:
            if not file.is_file():
                continue
            fname: str = file.stem
            if fname.startswith("_") or fname == "main":
                continue
            sdir: str = subdir.replace("/", ".").replace("\\", ".")
            modname: str = f"{sdir}.{fname}" if sdir else fname
            importlib.import_module(modname)
            mod: ModuleType = sys.modules[modname]
            try:
                mod.Task(mod.__name__).run_tasks()
            except AttributeError as err:
                print(err)
            except ValueError as err:
                print(err)
            print("\n")
