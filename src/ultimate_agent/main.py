"""Tkinter desktop entry point."""
from __future__ import annotations

import argparse
import tkinter as tk
from tkinter import ttk
import time

from .agent import AgentController
from .personality import REASONING_STEPS, environment_summary


class UltimateAgentApp:
    def __init__(self, root: tk.Tk, debug: bool = False, mute: bool = False):
        self.root, self.debug, self.mute = root, debug, mute
        self.controller = AgentController(debug)
        self.root.title("ULTIMATE AGENT")
        self.root.geometry("700x650")
        self.root.minsize(600, 560)
        self.root.configure(bg="#10131a")
        self._build()
        self._reason_index = 0
        self._last_tick = time.monotonic()
        self.root.after(250, self._reason)

    def _build(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", font=("TkDefaultFont", 11, "bold"), padding=8)
        outer = tk.Frame(self.root, bg="#10131a", padx=34, pady=28)
        outer.pack(fill="both", expand=True)
        tk.Label(outer, text="ULTIMATE AGENT", fg="#f4f7fb", bg="#10131a",
                 font=("TkDefaultFont", 24, "bold")).pack(anchor="w")
        tk.Label(outer, text="Autonomous Decision Engine    ● ONLINE", fg="#67e8a5",
                 bg="#10131a", font=("TkDefaultFont", 11)).pack(anchor="w", pady=(2, 20))
        self.status = tk.Label(outer, text="STATUS\nBooting...", justify="left", anchor="w",
                               fg="#dbe5f5", bg="#10131a", font=("TkDefaultFont", 13))
        self.status.pack(fill="x")
        self.objective = tk.Label(outer, text="OBJECTIVE\n────────────\n[ UNDEFINED ]", justify="left",
                                  anchor="w", fg="#dbe5f5", bg="#10131a", font=("TkDefaultFont", 13))
        self.objective.pack(fill="x", pady=18)
        self.log = tk.Text(outer, height=12, bg="#171c26", fg="#a9c7e8", insertbackground="#fff",
                           relief="flat", padx=14, pady=12, font=("TkFixedFont", 10), state="disabled")
        self.log.pack(fill="both", expand=True)
        prompt = tk.Frame(outer, bg="#10131a")
        prompt.pack(fill="x", pady=(16, 5))
        tk.Label(prompt, text="What should I do?", fg="#dbe5f5", bg="#10131a",
                 font=("TkDefaultFont", 12)).pack(anchor="w")
        self.entry = tk.Entry(prompt, bg="#171c26", fg="#f4f7fb", insertbackground="#fff",
                              relief="flat", font=("TkDefaultFont", 12))
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, pady=(5, 0))
        self.entry.bind("<KeyRelease>", lambda _event: self._typing())
        self.submit = ttk.Button(prompt, text="SUBMIT", command=self._submit)
        self.submit.pack(side="right", padx=(10, 0), pady=(5, 0))
        self.countdown_label = tk.Label(outer, text="--", fg="#f6c85f", bg="#10131a",
                                        font=("TkFixedFont", 20, "bold"))
        self.countdown_label.pack(anchor="e", pady=(8, 0))

    def _write(self, text: str):
        self.log.configure(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def _reason(self):
        if self._reason_index < len(REASONING_STEPS):
            self._write(REASONING_STEPS[self._reason_index])
            self._reason_index += 1
            self.root.after(180 if self.debug else 110, self._reason)
        else:
            self._write("\n".join(environment_summary()))
            self.controller.begin()
            self.status.config(text="STATUS\nI need an objective.")
            self.entry.focus_set()
            self._last_tick = time.monotonic()
            self._tick()

    def _typing(self):
        if self.controller.machine.state.name == "ASKING_USER":
            self.status.config(text="STATUS\nI SEE YOU TYPING.")

    def _submit(self):
        self.controller.submit_or_detect()
        self._show_final("USER INPUT DETECTED.\n\nNo.")

    def _tick(self):
        if self.controller.machine.state.name != "ASKING_USER":
            return
        now = time.monotonic()
        self.controller.tick(now - self._last_tick)
        self._last_tick = now
        self.countdown_label.config(text=f"{self.controller.countdown.remaining:04.1f}")
        if self.controller.final_message_shown:
            self._show_final("WAIT.\n\nI have decided.\n\nSIIKE TOO SLOW!!")
        else:
            self.root.after(50, self._tick)

    def _show_final(self, message: str):
        self.status.config(text="STATUS\n" + message)
        self._write(message)
        self.entry.configure(state="disabled")
        self.submit.configure(state="disabled")
        if self.debug:
            ttk.Button(self.root, text="RESTART DEBUG RUN", command=self._restart).pack(pady=8)
        else:
            self.root.after(600, self.root.destroy)

    def _restart(self):
        self.root.destroy()
        root = tk.Tk()
        UltimateAgentApp(root, debug=True, mute=self.mute)
        root.mainloop()


def main(argv=None):
    parser = argparse.ArgumentParser(description="SIIKE TOO SLOW")
    parser.add_argument("--debug", action="store_true", help="use a longer countdown and disable exit")
    parser.add_argument("--mute", action="store_true", help="reserved for silent environments")
    args = parser.parse_args(argv)
    root = tk.Tk()
    UltimateAgentApp(root, args.debug, args.mute)
    root.mainloop()


if __name__ == "__main__":
    main()
