# ME1MCP
 
run [`main.py`](main.py) in the root directory and select which session to run. alternatively, run `main.py` with arguments:

- `-a, --all` to run all tasks
- `-s [SESSION ...], --session [SESSION ...]` to specify which sessions to run. input either the session's full name or index number (starting from 1)

to run `main.py` in each session, the root directory should be installed as a package for `main.py` in the session to access the `helpers` directory.

---
## environment variable

create a ```.env``` file in the root directory, and add the following:

```env
CID=[your CID]
```

else if CID is not found in the environment variables, it will just use the default CID ```02345678```.

---

## creating a new session

create a new session by running the `-c` or `--create` argument.

each session can have as many tasks (`*.py`). any file that starts with an underscore `_` is ignored, as well as `main.py`, and will not be treated as a task.

in each task, create a `Task` class with the `run_tasks()` method. the `Task` class can also inherit from the `helpers.task.TaskBase` class, which will have its own `run_tasks()` method and other methods too.

for each subtask in the `Task` class that `run_tasks()` will run, it should not accept any arguments other than `self`. any variables requiring input should be retrieved via `input()` to the terminal, or pre-set in the subtask or `Task` class.