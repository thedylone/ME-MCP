import os
from helpers.task import runSession


def getSessions():
    """Get all sessions in the current directory."""
    sessions = []
    for file in os.listdir():
        if not os.path.isdir(file):
            continue
        if file.startswith("session"):
            sessions.append(file)
    return sessions


def runAllSessions():
    """Run all sessions in the current directory."""
    sessions = getSessions()
    for session in sessions:
        print(f"running {session}...")
        print("~~~~~~~~~~~~~~~~~~~~")
        runSession(__file__, session)
        print("~~~~~~~~~~~~~~~~~~~~\n")


def runSelectedSession(session):
    """Run a selected session."""
    print(f"running {session}...")
    print("~~~~~~~~~~~~~~~~~~~~")
    runSession(__file__, session)
    print("~~~~~~~~~~~~~~~~~~~~\n")


def userSelectSession():
    """Ask the user to select a session to run."""
    str_input = False
    sessions = getSessions()
    print("Select a session to run:")
    for i, session in enumerate(sessions):
        print(f"{i+1}: {session}")
    while True:
        try:
            selection = input("Select a session: ")
            if selection.isdigit():
                selection = int(selection)
                if selection < 1 or selection > len(sessions):
                    raise ValueError
                break
            elif selection in sessions:
                str_input = True
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid selection.")
    cls()
    if str_input:
        runSelectedSession(selection)
    else:
        runSelectedSession(sessions[selection - 1])


def cls():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    try:
        userSelectSession()
    except KeyboardInterrupt:
        print("Exiting...")
