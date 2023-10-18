"""test the main module."""

from pathlib import Path

import pytest

from main import (
    SessionRunner,
    validate_session_input_decorator,
    validate_session_decorator,
)

FXT_DIR: Path = Path(__file__).parent / "fixtures/test_root/"
SESSION_RUNNER: SessionRunner = SessionRunner(Path(__file__).parent)
SESSION_RUNNER.year = FXT_DIR
SESSION_RUNNER.sessions = SESSION_RUNNER.get_sessions(FXT_DIR)


def test_validate_session_decorator() -> None:
    """Test validate_session_decorator method."""

    @validate_session_decorator
    def test(_self, _session: Path) -> bool:
        return True

    # test valid session
    assert test(SESSION_RUNNER, FXT_DIR / "session1") is True
    # test invalid session
    with pytest.raises(ValueError):
        test(SESSION_RUNNER, FXT_DIR / "session3")


def test_validate_input_decorator() -> None:
    """Test validate_input_decorator method."""

    @validate_session_input_decorator
    def test(_self, _inputs: list[str]) -> bool:
        return True

    # test valid input
    assert test(SESSION_RUNNER, ["1", "2"]) is True
    # test invalid input
    with pytest.raises(ValueError):
        test(SESSION_RUNNER, ["3"])
    # test all input
    assert test(SESSION_RUNNER, ["all"]) is True
    # test empty input
    with pytest.raises(ValueError):
        test(SESSION_RUNNER, [""])


class TestSessionRunner:
    """Test the SessionRunner class."""

    def test_get_sessions(self) -> None:
        """Test get_sesssions method."""
        sessions: list[Path] = SESSION_RUNNER.get_sessions(FXT_DIR)
        assert sessions == [FXT_DIR / "session1", FXT_DIR / "session2"]

    def test_validate_session(self) -> None:
        """Test validate_session method."""
        # test valid session
        assert SESSION_RUNNER.validate_session(FXT_DIR / "session1") is True
        # test invalid session
        with pytest.raises(ValueError):
            SESSION_RUNNER.validate_session(FXT_DIR / "session3")

    def test_validate_input(self) -> None:
        """Test validate_input method."""
        # test valid input
        assert SESSION_RUNNER.validate_session_input(["1", "2"]) is True
        # test invalid input
        with pytest.raises(ValueError):
            SESSION_RUNNER.validate_session_input(["3"])
        # test all input
        assert SESSION_RUNNER.validate_session_input(["all"]) is True
        # test empty input
        with pytest.raises(ValueError):
            SESSION_RUNNER.validate_session_input([""])

    def test_run_session(self, capsys) -> None:
        """Test run_session method."""
        # test valid input
        SESSION_RUNNER.run_session(FXT_DIR / "session1")
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # # test invalid input
        with pytest.raises(ValueError):
            SESSION_RUNNER.run_session(FXT_DIR / "session3")

    def test_run_all_sessions(self, capsys) -> None:
        """Test run_all_sessions method."""
        SESSION_RUNNER.run_all_sessions()
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\ntest\n\n\n"

    def test_run_session_input(self, capsys):
        """Test run_session_input method."""
        # test valid input
        SESSION_RUNNER.run_session_input(["session1"])
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid input
        with pytest.raises(ValueError):
            SESSION_RUNNER.run_session_input(["3"])
        # test all input
        SESSION_RUNNER.run_session_input(["all"])
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\ntest\n\n\n"
        # test empty input
        with pytest.raises(ValueError):
            SESSION_RUNNER.run_session_input([""])

    def test_user_select(self, monkeypatch, capsys) -> None:
        """Test user_select method."""
        # test valid integer input
        monkeypatch.setattr("builtins.input", lambda _: "1")
        SESSION_RUNNER.select_session(debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid integer input
        monkeypatch.setattr("builtins.input", lambda _: "3")
        with pytest.raises(ValueError):
            SESSION_RUNNER.select_session(debug=True)
        # test valid string input
        monkeypatch.setattr("builtins.input", lambda _: "session1")
        SESSION_RUNNER.select_session(debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid string input
        monkeypatch.setattr("builtins.input", lambda _: "session3")
        with pytest.raises(ValueError):
            SESSION_RUNNER.select_session(debug=True)
        # test all input
        monkeypatch.setattr("builtins.input", lambda _: "all")
        SESSION_RUNNER.select_session(debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\ntest\n\n\n"
        # test empty input
        monkeypatch.setattr("builtins.input", lambda _: "")
        with pytest.raises(ValueError):
            SESSION_RUNNER.select_session(debug=True)
