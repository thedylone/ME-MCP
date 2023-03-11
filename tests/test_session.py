"""test the session module."""

from helpers.session import SessionBase


def test_run_session(capsys):
    """Test run_session method."""
    # test fixture
    SessionBase.run_session(__file__, "fixtures/test_session")
    capture = capsys.readouterr()
    assert capture.out == "test1\n\n\nfixtures.test_session.test2\n\n\n"
