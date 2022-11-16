"""test the task module."""

import pytest

from helpers.task import TaskBase, run_session, task_to_list


def test_task_to_list():
    """Test task_to_list method."""
    # test task_to_list
    test_list = []

    # test if keeps order
    @task_to_list(test_list)
    def test_task():
        return {"test": 1}

    @task_to_list(test_list)
    def test_task2():
        return {"test": 2}

    test_task()
    assert test_list[0].__name__ == test_task.__name__
    test_task2()
    assert test_list[1].__name__ == test_task2.__name__


class TestTaskBase:
    """Test the TaskBase class."""

    task_base = TaskBase("test", False)

    def test_init(self):
        """Test TaskBase initialization method."""
        # test init
        assert self.task_base.name == "test"
        assert self.task_base.output is False
        self.task_base.output = True
        assert self.task_base.output is True

    def test_int_input(self, monkeypatch):
        """Test int_input method."""
        # test valid input
        monkeypatch.setattr("builtins.input", lambda x: "1")
        assert TaskBase.int_input("test") == 1

        # test invalid input
        with pytest.raises(ValueError):
            monkeypatch.setattr("builtins.input", lambda x: "1.1")
            TaskBase.int_input("test", True)

        # test invalid alpha input
        with pytest.raises(ValueError):
            monkeypatch.setattr("builtins.input", lambda x: "a")
            TaskBase.int_input("test", True)

    def test_log(self):
        """Test log method."""
        self.task_base.output = True
        # test log msg
        assert self.task_base.log("test") == "test"
        # test log msg and kwargs
        assert self.task_base.log("test", test=1) == "test: test = 1"
        # test log msg and kwargs with multiple values
        val = {"test": 1, "test2": 2}
        assert self.task_base.log("test", **val) == "test: test = 1; test2 = 2"
        # test no output
        self.task_base.output = False
        assert self.task_base.log("test") is None


def test_run_session(capsys):
    """Test run_session method."""
    # test fixture
    run_session(__file__, "fixtures/test_session")
    capture = capsys.readouterr()
    assert capture.out == "test1\n\n\nfixtures.test_session.test2\n\n\n"
