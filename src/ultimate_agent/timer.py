"""A deterministic countdown model, independent of tkinter."""
from __future__ import annotations


class Countdown:
    def __init__(self, duration: float):
        if duration <= 0:
            raise ValueError("duration must be positive")
        self.duration = float(duration)
        self.remaining = float(duration)
        self.running = False

    def start(self) -> None:
        self.running = True

    def tick(self, elapsed: float) -> float:
        if elapsed < 0:
            raise ValueError("elapsed must not be negative")
        if self.running:
            self.remaining = max(0.0, self.remaining - elapsed)
            if self.remaining == 0:
                self.running = False
        return self.remaining

    @property
    def expired(self) -> bool:
        return self.remaining == 0.0
