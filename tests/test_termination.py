import unittest
from pathlib import Path
from ultimate_agent.self_termination import cleanup_owned_cache, terminate


class TerminationTests(unittest.TestCase):
    def test_termination_is_injectable(self):
        calls = []
        terminate(lambda code: calls.append(code), 0)
        self.assertEqual(calls, [0])

    def test_cleanup_only_removes_supplied_owned_directory(self):
        owned = Path(__file__).parent / ".owned-test"
        owned.mkdir(exist_ok=True)
        (owned / "state").write_text("safe")
        cleanup_owned_cache(owned)
        self.assertFalse(owned.exists())
