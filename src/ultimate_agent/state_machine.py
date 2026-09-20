"""Explicit, UI-independent state machine for the agent performance."""
from __future__ import annotations

from enum import Enum, auto
from typing import Callable


class State(Enum):
    BOOT = auto()
    INITIALIZING = auto()
    SCANNING = auto()
    THINKING = auto()
    ASKING_USER = auto()
    TOO_LATE = auto()
    CONFUSED = auto()
    AUTONOMOUS_DECISION = auto()
    SIIKE = auto()
    SELF_TERMINATION = auto()


class AgentStateMachine:
    """Validates transitions and records a structured event history."""

    _allowed = {
        State.BOOT: {State.INITIALIZING},
        State.INITIALIZING: {State.SCANNING},
        State.SCANNING: {State.THINKING},
        State.THINKING: {State.ASKING_USER},
        State.ASKING_USER: {State.TOO_LATE, State.CONFUSED},
        State.TOO_LATE: {State.SIIKE},
        State.CONFUSED: {State.AUTONOMOUS_DECISION},
        State.AUTONOMOUS_DECISION: {State.SIIKE},
        State.SIIKE: {State.SELF_TERMINATION},
        State.SELF_TERMINATION: set(),
    }

    def __init__(self, on_transition: Callable[[State, State], None] | None = None):
        self.state = State.BOOT
        self.history = [State.BOOT]
        self.events = ["BOOT"]
        self._on_transition = on_transition

    def transition(self, target: State) -> None:
        if target not in self._allowed[self.state]:
            raise ValueError(f"Invalid transition: {self.state.name} -> {target.name}")
        previous = self.state
        self.state = target
        self.history.append(target)
        self.events.append(target.name)
        if self._on_transition:
            self._on_transition(previous, target)

    def user_input(self) -> None:
        if self.state is not State.ASKING_USER:
            raise ValueError("User input is only accepted while asking")
        self.transition(State.TOO_LATE)
