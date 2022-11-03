from os.path import dirname, basename, isfile, join
import glob
import importlib
import sys


def main():
    files = glob.glob(join(dirname(__file__), "*.py"))
    for f in files:
        if isfile(f) and not f.endswith(("__init__.py", "main.py")):
            importlib.import_module(basename(f)[:-3])
            mod = sys.modules[basename(f)[:-3]]
            try:
                mod.Task(mod.__name__).runTasks()
            except Exception as e:
                print(e)
            print("\n")


if __name__ == "__main__":
    main()
