"""finds all sessions in the current directory and runs them via input"""

import argparse
import os
import sys

from helpers import task


def validate_session_decorator(func):
    """Decorator to validate a session name."""

    def wrapper(self, session, file=__file__):
        self.validate_session(session, file)
        return func(self, session, file)

    return wrapper


def validate_input_decorator(func):
    """Decorator to validate an input string."""

    def wrapper(self, _input, file=__file__):
        self.validate_input(_input, file)
        return func(self, _input, file)

    return wrapper


def flatten(list_of_lists):
    """Flatten a list of lists."""
    return [item for sublist in list_of_lists for item in sublist]


class SessionRunner:
    """Class to run a session."""

    inputs = []

    def __init__(self):
        pass

    @staticmethod
    def get_sessions(file=__file__):
        """Get all sessions in a directory."""
        sessions = []
        directory = os.path.dirname(file)
        for _file in os.listdir(directory):
            if not os.path.isdir(os.path.join(directory, _file)):
                continue
            if _file.startswith("session"):
                sessions.append(_file)
        return sorted(sessions)

    @classmethod
    def validate_session(cls, session, file=__file__):
        """Validate a session name."""
        if session not in cls.get_sessions(file):
            raise ValueError(f"Session {session} not found.")
        return True

    @classmethod
    def validate_input(cls, inputs, file=__file__):
        """Validate a list of inputs."""
        if "all" in inputs:
            cls.inputs = ["all"]
            return True
        sessions = cls.get_sessions(file)
        valid_inputs = []
        for i in inputs:
            if i == "":
                continue
            if i.isdigit():
                i = int(i)
                if i < 1 or i > len(sessions):
                    raise ValueError(f"Invalid input {i}.")
                valid_inputs.append(sessions[i - 1])
            else:
                if i not in sessions:
                    raise ValueError(f"Invalid input {i}.")
                valid_inputs.append(i)
        if not valid_inputs:
            raise ValueError("No valid inputs.")
        cls.inputs = valid_inputs
        return True

    @validate_session_decorator
    def run_session(self, session, file=__file__):
        """Run a session."""
        if file == __file__:
            print(f"running {session}...")
            print("~~~~~~~~~~~~~~~~~~~~")
        task.run_session(file, session)
        if file == __file__:
            print("~~~~~~~~~~~~~~~~~~~~\n")

    def run_all_sessions(self, file=__file__):
        """Run all sessions."""
        for session in self.get_sessions(file):
            self.run_session(session, file)

    @validate_input_decorator
    def run_session_input(self, inputs, file=__file__):
        """Run a session based on user input."""
        if self.inputs == ["all"]:
            self.run_all_sessions(file)
        else:
            for session in self.inputs:
                self.run_session(session, file)

    def user_select(self, file=__file__, debug=False):
        """Prompt user to select a session."""
        if not debug:
            print("Select a session to run:")
            for i, session in enumerate(self.get_sessions(file)):
                print(f"{i + 1}. {session}")
            print("all. Run all sessions")
        while True:
            try:
                inputs = input("Enter session(s) to run: ").split(" ")
                self.run_session_input(inputs, file)
                break
            except ValueError as err:
                if debug:
                    raise ValueError from err
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="run me1 sessions tasks")
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
        args = parser.parse_args()
        if args.all:
            SessionRunner().run_all_sessions()
        elif args.session:
            SessionRunner().run_session_input(flatten(args.session))
        else:
            SessionRunner().user_select()
    except ValueError:
        print("Invalid input. Please try again.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
