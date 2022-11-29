"""test the task module."""

import pytest

from helpers.task import TaskBase, run_session, task_to_list, get_input


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


def test_get_input(monkeypatch):
    """Test get_input method."""
    # test successful input - int
    monkeypatch.setattr("builtins.input", lambda x: "1")
    assert get_input(int, "test") == 1

    # test successful input - float
    monkeypatch.setattr("builtins.input", lambda x: "1.1")
    assert get_input(float, "test") == 1.1

    # test successful input - str
    monkeypatch.setattr("builtins.input", lambda x: "test")
    assert get_input(str, "test") == "test"

    # test successful input - bool
    monkeypatch.setattr("builtins.input", lambda x: "True")
    assert get_input(bool, "test") is True

    # test successful input - list
    monkeypatch.setattr("builtins.input", lambda x: "123")
    assert get_input(list, "test") == ["1", "2", "3"]

    # test successful input - tuple
    monkeypatch.setattr("builtins.input", lambda x: "123")
    assert get_input(tuple, "test") == ("1", "2", "3")

    # test successful input - set
    monkeypatch.setattr("builtins.input", lambda x: "1231")
    assert get_input(set, "test") == {"1", "2", "3"}

    # test failed input - int
    monkeypatch.setattr("builtins.input", lambda x: "a")
    with pytest.raises(ValueError):
        get_input(int, "test", debug=True)

    # test failed input - int out of range
    monkeypatch.setattr("builtins.input", lambda x: "2")
    with pytest.raises(ValueError):
        get_input(int, "test", maxval=1, debug=True)

    # test failed input - float
    monkeypatch.setattr("builtins.input", lambda x: "a")
    with pytest.raises(ValueError):
        get_input(float, "test", debug=True)

    # test failed input - float out of range
    monkeypatch.setattr("builtins.input", lambda x: "2.1")
    with pytest.raises(ValueError):
        get_input(float, "test", maxval=2, debug=True)


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
