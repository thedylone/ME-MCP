from main import SessionRunner
from os.path import dirname, join
import pytest


class TestMain:
    session_runner = SessionRunner()

    fxt_dir = join(dirname(__file__), "fixtures\\test_root")

    def test_getSessions(self):
        """Test getSesssions method."""
        sessions = self.session_runner.getSessions(self.fxt_dir)
        assert sessions == ["session1", "session2"]

    def test_validateSession(self):
        """Test validateSession method."""
        # test valid session
        assert SessionRunner.validateSession("session1", self.fxt_dir) is True
        # test invalid session
        with pytest.raises(ValueError):
            self.session_runner.validateSession("session3", self.fxt_dir)

    def test_validateSessionDecorator(self):
        """Test validateSessionDecorator method."""

        @SessionRunner.validateSessionDecorator
        def test(self, session, dir=None):
            return True

        # test valid session
        assert test(SessionRunner, "session1", self.fxt_dir) is True
        # test invalid session
        with pytest.raises(ValueError):
            test(SessionRunner, "session3", self.fxt_dir)

    def test_validateInput(self):
        """Test validateInput method."""
        # test valid input
        assert SessionRunner.validateInput(["1", "2"], self.fxt_dir) is True
        # test invalid input
        with pytest.raises(ValueError):
            SessionRunner.validateInput(["3"], self.fxt_dir)
        # test all input
        assert SessionRunner.validateInput(["all"], self.fxt_dir) is True
        # test empty input
        with pytest.raises(ValueError):
            SessionRunner.validateInput([""], self.fxt_dir)

    def test_validateInputDecorator(self):
        """Test validateInputDecorator method."""

        @SessionRunner.validateInputDecorator
        def test(self, inputs, dir=None):
            return True

        # test valid input
        assert test(SessionRunner, ["1", "2"], self.fxt_dir) is True
        # test invalid input
        with pytest.raises(ValueError):
            test(SessionRunner, ["3"], self.fxt_dir)
        # test all input
        assert test(SessionRunner, ["all"], self.fxt_dir) is True
        # test empty input
        with pytest.raises(ValueError):
            test(SessionRunner, [""], self.fxt_dir)
