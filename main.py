import os
import argparse
from helpers.task import runSession


class SessionRunner:
    inputs = None

    def __init__(self):
        pass

    @staticmethod
    def getSessions(file=__file__):
        """Get all sessions in a directory."""
        sessions = []
        dir = os.path.dirname(file)
        for f in os.listdir(dir):
            if not os.path.isdir(os.path.join(dir, f)):
                continue
            if f.startswith("session"):
                sessions.append(f)
        return sessions

    @classmethod
    def validateSession(cls, session, file=__file__):
        """Validate a session name."""
        if session not in cls.getSessions(file):
            raise ValueError(f"Session {session} not found.")
        return True

    def validateSessionDecorator(func):
        """Decorator to validate a session name."""

        def wrapper(self, session, file=__file__):
            self.validateSession(session, file)
            return func(self, session, file)

        return wrapper

    @classmethod
    def validateInput(cls, inputs, file=__file__):
        """Validate a list of inputs."""
        if "all" in inputs:
            cls.inputs = ["all"]
            return True
        sessions = cls.getSessions(file)
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

    def validateInputDecorator(func):
        """Decorator to validate an input string."""

        def wrapper(self, _input, file=__file__):
            self.validateInput(_input, file)
            return func(self, _input, file)

        return wrapper

    @validateSessionDecorator
    def _runSession(self, session, file=__file__):
        """Run a session."""
        if file == __file__:
            print(f"running {session}...")
            print("~~~~~~~~~~~~~~~~~~~~")
        runSession(file, session)
        if file == __file__:
            print("~~~~~~~~~~~~~~~~~~~~\n")

    def runAllSessions(self, file=__file__):
        """Run all sessions."""
        for session in self.getSessions(file):
            self._runSession(session, file)

    @validateInputDecorator
    def runSessionInput(self, inputs, file=__file__):
        """Run a session based on user input."""
        if self.inputs == ["all"]:
            self.runAllSessions(file)
        else:
            for session in self.inputs:
                self._runSession(session, file)

    def userSelect(self):
        """Prompt user to select a session."""
        print("Select a session to run:")
        for i, session in enumerate(self.getSessions()):
            print(f"{i + 1}. {session}")
        print("all. Run all sessions")
        while True:
            try:
                inputs = input("Enter session(s) to run: ").split(" ")
                self.runSessionInput(inputs)
                break
            except ValueError:
                print("Invalid input. Please try again.")
                continue


def flatten(list):
    return [item for sublist in list for item in sublist]


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
            SessionRunner().runAllSessions()
        elif args.session:
            SessionRunner().runSessionInput(flatten(args.session))
        else:
            SessionRunner().userSelect()
    except ValueError:
        print("Invalid input. Please try again.")
        exit(1)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
