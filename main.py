"""finds all sessions in the current directory and runs them via input"""

import argparse
import os
import sys
from string import Template
from collections.abc import Callable
from helpers.session import SessionBase


def validate_session_decorator(func: Callable) -> Callable:
    """Decorator to validate a session name."""

    def wrapper(self, session: str, file: str = __file__):
        self.validate_session(session, file)
        return func(self, session, file)

    return wrapper


def validate_input_decorator(func: Callable) -> Callable:
    """Decorator to validate an input string."""

    def wrapper(self, _input: str, file: str = __file__):
        self.validate_input(_input, file)
        return func(self, _input, file)

    return wrapper


def flatten(list_of_lists: list[list]) -> list:
    """Flatten a list of lists."""
    return [item for sublist in list_of_lists for item in sublist]


class SessionRunner:
    """Class to run a session."""

    inputs: list[str] = []
    session_prefix: tuple[str, str] = ("session", "consolidation")

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_sessions(file: str = __file__) -> list[str]:
        """Get all sessions in a directory."""
        sessions: list[str] = []
        directory: str = os.path.dirname(file)
        for _file in os.listdir(directory):
            if not os.path.isdir(os.path.join(directory, _file)):
                continue
            if _file.startswith(SessionRunner.session_prefix):
                sessions.append(_file)
        return sorted(sessions)

    @classmethod
    def validate_session(cls, session: str, file: str = __file__) -> bool:
        """Validate a session name."""
        if session not in cls.get_sessions(file):
            raise ValueError(f"Session {session} not found.")
        return True

    @classmethod
    def validate_input(cls, inputs: list[str], file: str = __file__) -> bool:
        """Validate a list of inputs."""
        if "all" in inputs:
            cls.inputs = ["all"]
            return True
        sessions: list[str] = cls.get_sessions(file)
        valid_inputs: list[str] = []
        for i in inputs:
            if i == "":
                continue
            if i.isdigit():
                _i: int = int(i)
                if _i < 1 or _i > len(sessions):
                    raise ValueError(f"Invalid input {_i}.")
                valid_inputs.append(sessions[_i - 1])
            else:
                if i not in sessions:
                    raise ValueError(f"Invalid input {i}.")
                valid_inputs.append(i)
        if not valid_inputs:
            raise ValueError("No valid inputs.")
        cls.inputs = valid_inputs
        return True

    @validate_session_decorator
    def run_session(self, session: str, file: str = __file__) -> None:
        """Run a session."""
        if file == __file__:
            print(f"running {session}...")
            print("~~~~~~~~~~~~~~~~~~~~")
        SessionBase.run_session(file, session)
        if file == __file__:
            print("~~~~~~~~~~~~~~~~~~~~\n")

    def run_all_sessions(self, file: str = __file__) -> None:
        """Run all sessions."""
        for session in self.get_sessions(file):
            self.run_session(session, file)

    @validate_input_decorator
    def run_session_input(self, _inputs, file: str = __file__) -> None:
        """Run a session based on user input."""
        if self.inputs == ["all"]:
            self.run_all_sessions(file)
        else:
            for session in self.inputs:
                self.run_session(session, file)

    def user_select(self, file: str = __file__, debug: bool = False) -> None:
        """Prompt user to select a session."""
        if not debug:
            print("Select a session to run:")
            for i, session in enumerate(self.get_sessions(file)):
                print(f"{i + 1}. {session}")
            print("all. Run all sessions")
        while True:
            try:
                inputs_str: str = input("Enter session(s) to run: ")
                inputs: list[str] = inputs_str.split(",")
                self.run_session_input(inputs, file)
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
            os.makedirs(session_name)
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
        with open(f"{session}/{task_name}.py", "w", encoding="utf-8") as file:
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
        if args.all:
            SessionRunner().run_all_sessions()
        elif args.create:
            SessionRunner().create_session()
        elif args.task:
            SessionRunner().create_task(args.task)
        elif args.session:
            SessionRunner().run_session_input(flatten(args.session))
        else:
            SessionRunner().user_select()
    except ValueError as err:
        print(err)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
