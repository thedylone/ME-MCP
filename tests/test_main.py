"""test the main module."""

from os.path import dirname, join

import pytest

from main import (SessionRunner, validate_input_decorator,
                  validate_session_decorator)

FXT_DIR = join(dirname(__file__), "fixtures/test_root/")


def test_validate_session_decorator():
    """Test validate_session_decorator method."""

    @validate_session_decorator
    def test(self, session, file=None):
        return True

    # test valid session
    assert test(SessionRunner, "session1", FXT_DIR) is True
    # test invalid session
    with pytest.raises(ValueError):
        test(SessionRunner, "session3", FXT_DIR)


def test_validate_input_decorator():
    """Test validate_input_decorator method."""

    @validate_input_decorator
    def test(self, inputs, file=None):
        return True

    # test valid input
    assert test(SessionRunner, ["1", "2"], FXT_DIR) is True
    # test invalid input
    with pytest.raises(ValueError):
        test(SessionRunner, ["3"], FXT_DIR)
    # test all input
    assert test(SessionRunner, ["all"], FXT_DIR) is True
    # test empty input
    with pytest.raises(ValueError):
        test(SessionRunner, [""], FXT_DIR)


class TestSessionRunner:
    """Test the SessionRunner class."""

    session_runner = SessionRunner()

    def test_get_sessions(self):
        """Test get_sesssions method."""
        sessions = self.session_runner.get_sessions(FXT_DIR)
        assert sessions == ["session1", "session2"]

    def test_validate_session(self):
        """Test validate_session method."""
        # test valid session
        assert SessionRunner.validate_session("session1", FXT_DIR) is True
        # test invalid session
        with pytest.raises(ValueError):
            self.session_runner.validate_session("session3", FXT_DIR)

    def test_validate_input(self):
        """Test validate_input method."""
        # test valid input
        assert SessionRunner.validate_input(["1", "2"], FXT_DIR) is True
        # test invalid input
        with pytest.raises(ValueError):
            SessionRunner.validate_input(["3"], FXT_DIR)
        # test all input
        assert SessionRunner.validate_input(["all"], FXT_DIR) is True
        # test empty input
        with pytest.raises(ValueError):
            SessionRunner.validate_input([""], FXT_DIR)

    def test_run_session(self, capsys):
        """Test run_session method."""
        # test valid input
        self.session_runner.run_session("session_test", __file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # # test invalid input
        with pytest.raises(ValueError):
            self.session_runner.run_session("session3", __file__)

    def test_run_all_sessions(self, capsys):
        """Test run_all_sessions method."""
        self.session_runner.run_all_sessions(__file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"

    def test_run_session_input(self, capsys):
        """Test run_session_input method."""
        # test valid input
        self.session_runner.run_session_input(["session_test"], __file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid input
        with pytest.raises(ValueError):
            self.session_runner.run_session_input(["3"], __file__)
        # test all input
        self.session_runner.run_session_input(["all"], __file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test empty input
        with pytest.raises(ValueError):
            self.session_runner.run_session_input([""], __file__)

    def test_user_select(self, monkeypatch, capsys):
        """Test user_select method."""
        # test valid integer input
        monkeypatch.setattr("builtins.input", lambda _: "1")
        self.session_runner.user_select(file=__file__, debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid integer input
        monkeypatch.setattr("builtins.input", lambda _: "3")
        with pytest.raises(ValueError):
            self.session_runner.user_select(file=__file__, debug=True)
        # test valid string input
        monkeypatch.setattr("builtins.input", lambda _: "session_test")
        self.session_runner.user_select(file=__file__, debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid string input
        monkeypatch.setattr("builtins.input", lambda _: "session3")
        with pytest.raises(ValueError):
            self.session_runner.user_select(file=__file__, debug=True)
        # test all input
        monkeypatch.setattr("builtins.input", lambda _: "all")
        self.session_runner.user_select(file=__file__, debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test empty input
        monkeypatch.setattr("builtins.input", lambda _: "")
        with pytest.raises(ValueError):
            self.session_runner.user_select(file=__file__, debug=True)
