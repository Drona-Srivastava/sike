import unittest

from ultimate_agent.agent import AgentController
from ultimate_agent.state_machine import State


class StateMachineTests(unittest.TestCase):
    def test_normal_states_transition_in_order(self):
        agent = AgentController()
        agent.begin()
        self.assertIs(agent.machine.state, State.ASKING_USER)
        agent.tick(3)
        self.assertEqual(agent.machine.history, [
            State.BOOT, State.INITIALIZING, State.SCANNING, State.THINKING,
            State.ASKING_USER, State.CONFUSED, State.AUTONOMOUS_DECISION,
            State.SIIKE, State.SELF_TERMINATION,
        ])
        self.assertTrue(agent.final_message_shown)

    def test_input_is_detected_but_never_executed(self):
        agent = AgentController()
        agent.begin()
        agent.submit_or_detect()
        self.assertIn("USER_INPUT_DETECTED", agent.machine.events)
        self.assertIs(agent.machine.state, State.SELF_TERMINATION)

    def test_debug_can_restart_and_does_not_expire_early(self):
        agent = AgentController(debug=True)
        agent.begin()
        self.assertFalse(agent.tick(8))
        self.assertIs(agent.machine.state, State.ASKING_USER)
        self.assertTrue(agent.tick(1))
        agent.restart()
        self.assertIs(agent.machine.state, State.BOOT)
