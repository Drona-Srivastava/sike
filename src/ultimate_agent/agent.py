"""Orchestration layer shared by the graphical app and headless tests."""
from __future__ import annotations

from .state_machine import AgentStateMachine, State
from .timer import Countdown


class AgentController:
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.machine = AgentStateMachine()
        self.countdown = Countdown(9.0 if debug else 3.0)
        self.final_message_shown = False

    @property
    def can_restart(self) -> bool:
        return self.debug and self.machine.state is State.SELF_TERMINATION

    def begin(self) -> None:
        for state in (State.INITIALIZING, State.SCANNING, State.THINKING, State.ASKING_USER):
            self.machine.transition(state)
        self.machine.events.append("USER_PROMPT_SHOWN")
        self.machine.events.append("COUNTDOWN_STARTED")
        self.countdown.start()

    def submit_or_detect(self) -> None:
        if self.machine.state is State.ASKING_USER:
            self.machine.events.append("USER_INPUT_DETECTED")
            self.machine.user_input()
            self.machine.transition(State.SIIKE)
            self.final_message_shown = True
            self.machine.transition(State.SELF_TERMINATION)

    def tick(self, elapsed: float) -> bool:
        if self.machine.state is not State.ASKING_USER:
            return False
        if self.countdown.tick(elapsed) == 0:
            self.machine.transition(State.CONFUSED)
            self.machine.transition(State.AUTONOMOUS_DECISION)
            self.machine.transition(State.SIIKE)
            self.final_message_shown = True
            self.machine.transition(State.SELF_TERMINATION)
            self.machine.events.append("TERMINATING")
            return True
        return False

    def restart(self) -> None:
        if not self.can_restart:
            raise RuntimeError("Restart is available only after a debug run")
        self.__init__(debug=True)
