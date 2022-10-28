import a
import b
import c
import d
import e
import f


def main():
    for q in [a, b, c, d, e, f]:
        task = q.Task(q.__name__)
        task.runTasks()
        print("\n")


if __name__ == "__main__":
    main()
