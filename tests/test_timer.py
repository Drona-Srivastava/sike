import unittest
from ultimate_agent.timer import Countdown


class CountdownTests(unittest.TestCase):
    def test_countdown_reaches_zero(self):
        timer = Countdown(3)
        timer.start()
        self.assertEqual(timer.tick(1.25), 1.75)
        self.assertEqual(timer.tick(2), 0)
        self.assertTrue(timer.expired and not timer.running)

    def test_invalid_duration_and_elapsed(self):
        with self.assertRaises(ValueError):
            Countdown(0)
        timer = Countdown(1)
        with self.assertRaises(ValueError):
            timer.tick(-1)
