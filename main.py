"""finds all sessions in the current directory and runs them via input"""

import argparse
from pathlib import Path
import sys
from string import Template
from collections.abc import Callable
from helpers.session import SessionBase


def validate_session_decorator(func: Callable) -> Callable:
    """Decorator to validate a session name."""

    def wrapper(self: "SessionRunner", session: Path):
        self.validate_session(session)
        return func(self, session)

    return wrapper


def validate_session_input_decorator(func: Callable) -> Callable:
    """Decorator to validate an input string."""

    def wrapper(
        self: "SessionRunner",
        _input: list[str],
    ):
        self.validate_session_input(_input)
        return func(self, _input)

    return wrapper


def flatten(list_of_lists: list[list]) -> list:
    """Flatten a list of lists."""
    return [item for sublist in list_of_lists for item in sublist]


class SessionRunner:
    """Class to run a session."""

    session_prefix: tuple[str, str, str] = (
        "session",
        "consolidation",
        "finals",
    )

    def __init__(self, directory: Path = Path(__file__).parent) -> None:
        self.directory: Path = directory
        self.years: list[Path] = self.get_years(directory)
        self.year: Path
        self.sessions: list[Path] = []
        self.inputs: list[Path] | list[str] = []

    @staticmethod
    def get_sessions(directory: Path) -> list[Path]:
        """Get all sessions in a directory."""
        sessions: list[Path] = []
        for file in directory.iterdir():
            if not file.is_dir():
                continue
            if file.name.startswith(SessionRunner.session_prefix):
                sessions.append(file)
        return sorted(sessions)

    @staticmethod
    def get_years(directory: Path) -> list[Path]:
        """Get all years in a directory."""
        years: list[Path] = []
        for file in directory.iterdir():
            if not file.is_dir():
                continue
            if file.name.startswith("year"):
                years.append(file)
        return sorted(years)

    def validate_year_input(self, input_str: str) -> bool:
        """Validate a year input."""
        if input_str.isdigit():
            _input: int = int(input_str)
            if _input < 1 or _input > len(self.years):
                raise ValueError(f"Invalid input {_input}.")
            self.year = self.years[_input - 1]
        else:
            if Path(input_str) not in self.years:
                raise ValueError(f"Invalid input {input_str}.")
            self.year = Path(input_str)
        return True

    def validate_session(self, session: Path) -> bool:
        """Validate a session name."""
        if session not in self.sessions:
            raise ValueError(f"Session {session} not found.")
        return True

    def validate_session_input(self, inputs: list[str]) -> bool:
        """Validate a list of inputs."""
        if "all" in inputs:
            self.inputs = ["all"]
            return True
        valid_inputs: list[Path] = []
        for i in inputs:
            i: str = i.strip()
            if i == "":
                continue
            if i.isdigit():
                _i: int = int(i)
                if _i < 1 or _i > len(self.sessions):
                    raise ValueError(f"Invalid input {_i}.")
                valid_inputs.append(self.sessions[_i - 1])
            else:
                if self.year / i not in self.sessions:
                    raise ValueError(f"Invalid input {i}.")
                valid_inputs.append(self.year / i)
        if not valid_inputs:
            raise ValueError("No valid inputs.")
        self.inputs = valid_inputs
        return True

    @validate_session_decorator
    def run_session(self, session: Path) -> None:
        """Run a session."""
        if __name__ == "__main__":
            print(f"running {session}...")
            print("~~~~~~~~~~~~~~~~~~~~")
        SessionBase.run_session(
            self.directory, str(session.relative_to(self.directory))
        )
        if __name__ == "__main__":
            print("~~~~~~~~~~~~~~~~~~~~\n")

    def run_all_sessions(self) -> None:
        """Run all sessions."""
        for session in self.sessions:
            self.run_session(session)

    @validate_session_input_decorator
    def run_session_input(self, _inputs) -> None:
        """Run a session based on user input."""
        if self.inputs == ["all"]:
            self.run_all_sessions()
        else:
            for session in self.inputs:
                self.run_session(session)

    def select_year(self) -> None:
        """Prompt user to select a year."""
        print("Select a year to run:")
        for i, year in enumerate(self.years):
            print(f"{i + 1}. {year}")
        while True:
            try:
                input_str: str = input("Enter year to run: ")
                self.validate_year_input(input_str)
                self.sessions = self.get_sessions(self.year)
                break
            except ValueError:
                print("Invalid input. Please try again.")
                continue

    def select_session(self, debug: bool = False) -> None:
        """Prompt user to select a session."""
        if not debug:
            print("Select a session to run:")
            for i, session in enumerate(self.sessions):
                print(f"{i + 1}. {session.name}")
            print("all. Run all sessions")
        while True:
            try:
                inputs_str: str = input("Enter session(s) to run: ")
                inputs: list[str] = inputs_str.split(",")
                self.run_session_input(inputs)
                break
            except ValueError as error:
                if debug:
                    raise ValueError from error
                print("Invalid input. Please try again.")
                continue

    def create_session(self) -> None:
        """Create a session."""
        session_name: str = input("Enter session name: ")
        # create directory
        self.create_dir_and_main(session_name)
        # create tasks
        while True:
            self.create_task(session_name)
            if input("Create another task? (y/n): ").lower() != "y":
                break

    def create_dir_and_main(self, session_name: str) -> None:
        """Create a session directory and main.py."""
        if not session_name.startswith(SessionRunner.session_prefix):
            print(f"Name must start with {SessionRunner.session_prefix}")
            raise ValueError(f"Invalid session name {session_name}.")
        # create directory
        try:
            # os.makedirs(session_name)
            (self.year / session_name).mkdir()
        except FileExistsError as exc:
            print("Session name already exists, exiting...")
            raise ValueError(f"Invalid session name {session_name}.") from exc
        # create main.py
        with open("helpers/templates/main.txt", "r", encoding="utf-8") as file:
            main_template: Template = Template(file.read())
        with open(f"{session_name}/main.py", "w", encoding="utf-8") as file:
            session_doc: str = input("Enter session description: ")
            file.write(main_template.substitute(docstring=session_doc))

    @validate_session_decorator
    def create_task(self, session: str, _file=__file__) -> None:
        """Create a task."""
        task_name: str = input("Enter task name: ")
        with open("helpers/templates/task.txt", "r", encoding="utf-8") as file:
            task_template: Template = Template(file.read())
        with open(
            f"{self.year}/{session}/{task_name}.py", "w", encoding="utf-8"
        ) as file:
            task_doc: str = input("Enter task description: ")
            task_d: dict[str, str] = {
                "docstring": task_doc,
                "name": task_name.title(),
            }
            file.write(task_template.substitute(task_d))


if __name__ == "__main__":
    try:
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            description="run me1 sessions tasks"
        )
        parser.add_argument(
            "-a",
            "--all",
            action="store_true",
            help="run all tasks",
        )
        parser.add_argument(
            "-s",
            "--session",
            nargs="*",
            action="append",
            help="select session(s) to run",
        )
        parser.add_argument(
            "-c",
            "--create",
            action="store_true",
            help="create session",
        )
        parser.add_argument(
            "-t",
            "--task",
            help="create task in existing session",
        )
        args: argparse.Namespace = parser.parse_args()
        session_runner: SessionRunner = SessionRunner()
        session_runner.select_year()
        if args.all:
            session_runner.run_all_sessions()
        elif args.create:
            session_runner.create_session()
        elif args.task:
            session_runner.create_task(args.task)
        elif args.session:
            session_runner.run_session_input(flatten(args.session))
        else:
            session_runner.select_session()
    except ValueError as err:
        print(err)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
