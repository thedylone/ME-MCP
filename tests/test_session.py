"""test the session module."""

from pathlib import Path

from helpers.session import SessionBase


def test_run_session(capsys) -> None:
    """Test run_session method."""
    # test fixture
    SessionBase.run_session(Path(__file__).parent, "fixtures/test_session")
    capture = capsys.readouterr()
    assert capture.out == "test1\n\n\nfixtures.test_session.test2\n\n\n"
