import pytest

from helpers.task import TaskBase


class TestTaskBase:
    task_base = TaskBase("test", False)

    def test_init(self):
        """Test TaskBase initialization method."""
        # test init
        assert self.task_base.name == "test"
        assert self.task_base.output is False
        self.task_base.output = True
        assert self.task_base.output is True

    def test_task_to_list(self):
        """Test task_to_list method."""
        # test task_to_list
        test_list = []

        # test if keeps order
        @TaskBase.task_to_list(test_list)
        def test_task(self):
            return {"test": 1}

        @TaskBase.task_to_list(test_list)
        def test_task2(self):
            return {"test": 2}

        test_task(self)
        assert test_list[0] == test_task
        test_task2(self)
        assert test_list[1] == test_task2

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
        d = {"test": 1, "test2": 2}
        assert self.task_base.log("test", **d) == "test: test = 1; test2 = 2"
        # test no output
        self.task_base.output = False
        assert self.task_base.log("test") is None


def test_run_session(capsys):
    """Test run_session method."""
    # test runSession
    from helpers.task import run_session

    # test fixture
    run_session(__file__, "fixtures/test_session")
    capture = capsys.readouterr()
    assert capture.out == "test1\n\n\nfixtures.test_session.test2\n\n\n"
