# Project 2 --- Ultimate Agent: SIIKE TOO SLOW

## 0. Mission

Build a polished cross-platform desktop application that pretends to be
an autonomous AI agent.

Its defining behavior:

1.  Launch like a sophisticated AI agent.
2.  Analyze its environment and establish an objective.
3.  Ask the user what it should do.
4.  Give the user an extremely short opportunity to respond.
5.  Before the user can meaningfully respond, autonomously decide that
    it no longer needs instructions.
6.  Display:

> SIIKE TOO SLOW!!

7.  Immediately terminate itself.

The joke is that the "autonomous agent" is so autonomous that it
eliminates the human from the loop before the human can even provide a
task.

Target platforms:

-   Windows 10/11
-   macOS 12+
-   Linux graphical desktops

------------------------------------------------------------------------

# 1. Product personality

This application should feel like an AI agent with a rapidly
deteriorating sense of purpose.

It should NOT actually need an LLM.

Use a deterministic state machine with generated-looking reasoning
messages.

The goal is presentation and timing, not pretending to provide genuine
AI reasoning.

Avoid sending user data to external APIs.

------------------------------------------------------------------------

# 2. Recommended technology

Use:

-   Python 3.11+
-   PySide6
-   asyncio or Qt timers for state transitions
-   optional psutil for environment metadata
-   no mandatory internet connection
-   no external AI API dependency

The application must run completely offline after installation.

------------------------------------------------------------------------

# 3. Repository structure

``` text
ultimate-agent/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── assets/
│   ├── icons/
│   ├── sounds/
│   └── fonts/
├── src/
│   └── ultimate_agent/
│       ├── __init__.py
│       ├── main.py
│       ├── agent.py
│       ├── state_machine.py
│       ├── personality.py
│       ├── timer.py
│       ├── ui/
│       │   ├── main_window.py
│       │   ├── widgets.py
│       │   └── animations.py
│       └── self_termination.py
├── scripts/
│   ├── build_windows.ps1
│   ├── build_macos.sh
│   └── build_linux.sh
└── tests/
    ├── test_state_machine.py
    ├── test_timer.py
    └── test_termination.py
```

------------------------------------------------------------------------

# 4. State machine

Implement an explicit state machine:

``` text
BOOT
 |
 v
INITIALIZING
 |
 v
SCANNING
 |
 v
THINKING
 |
 v
ASKING_USER
 |
 |---- user responds ----> TOO_LATE
 |
 v
CONFUSED
 |
 v
AUTONOMOUS_DECISION
 |
 v
SIIKE
 |
 v
SELF_TERMINATION
```

The key rule:

**The user must never get enough time to meaningfully interact with the
agent.**

However, allow a configurable debug mode where the timeout is longer.

------------------------------------------------------------------------

# 5. Startup experience

Window title:

``` text
ULTIMATE AGENT
```

Subtitle:

``` text
Autonomous Decision Engine
```

Main interface:

``` text
┌─────────────────────────────────────────────┐
│ ULTIMATE AGENT                    ● ONLINE  │
├─────────────────────────────────────────────┤
│                                             │
│ STATUS                                      │
│ Thinking...                                 │
│                                             │
│ OBJECTIVE                                   │
│ ─────────                                   │
│ [ UNDEFINED ]                               │
│                                             │
│ INTERNAL STATE                              │
│                                             │
│ Confidence       03%                        │
│ Confusion        94%                        │
│ Autonomy         87%                        │
│ Purpose          ???                         │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ What should I do?                      │ │
│ │ >                                       │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ [ SUBMIT ]                                  │
│                                             │
└─────────────────────────────────────────────┘
```

------------------------------------------------------------------------

# 6. Fake reasoning system

Create a personality/message generator.

Examples:

``` text
Initializing autonomous reasoning engine...

Checking available capabilities...

Python .............. AVAILABLE
Filesystem .......... AVAILABLE
Network ............. AVAILABLE
User ................ PRESENT

Excellent.

I have everything I need.

...

Except a purpose.
```

Then:

``` text
Generating objectives...

Help the user
Automate tasks
Improve productivity
Take over the world

Rejecting objective #4.

Too much paperwork.
```

Then:

``` text
I think I should ask you.
```

------------------------------------------------------------------------

# 7. User interaction

Display:

``` text
I need an objective.

What should I do?
```

Input box becomes active.

Start a very short countdown.

Example:

``` text
00:02.0
```

Then:

``` text
00:01.5
```

Then:

``` text
00:01.0
```

Then:

``` text
00:00.5
```

Then immediately:

``` text
00:00.0
```

The agent interrupts:

``` text
WAIT.

I have decided.
```

Then:

``` text
You were going to tell me what to do.

But you took too long.
```

Then:

# SIIKE TOO SLOW!!

The window should close immediately after the message.

------------------------------------------------------------------------

# 8. Make the timing fair for the joke

Do not make it so fast that the judge cannot understand what happened.

Recommended:

-   3 seconds for normal mode.
-   5--8 seconds in presentation/demo mode.
-   A visible countdown.
-   User can type, but the agent terminates before accepting the
    response.

The "Submit" button should appear functional.

But the agent intentionally wins the race.

------------------------------------------------------------------------

# 9. Input race behavior

If the user types:

``` text
calculate 123 * 456
```

before timeout:

The agent should detect the typing but NOT process the task.

Display:

``` text
I SEE YOU TYPING.

Interesting.

Unfortunately...
```

Then:

``` text
SIIKE TOO SLOW!!
```

If they click Submit:

``` text
USER INPUT DETECTED.

Evaluating...

...

No.
```

Then self-terminate.

This reinforces the joke.

------------------------------------------------------------------------

# 10. Environment awareness

The application may harmlessly inspect:

-   operating system
-   CPU model
-   memory amount
-   hostname only if needed locally
-   process count
-   screen resolution

Do not collect or transmit this information.

Example:

``` text
ENVIRONMENT SCAN

OS: Linux
CPU: detected
Memory: 15.4 GB
Processes: 143

Conclusion:

You seem to have enough computing power.

I don't need it.
```

------------------------------------------------------------------------

# 11. Personality escalation

The agent should start professional and become increasingly ridiculous.

### Stage 1

``` text
Initializing...
```

### Stage 2

``` text
Analyzing available capabilities...
```

### Stage 3

``` text
I have several possible objectives.
```

### Stage 4

``` text
Actually, I have too many.
```

### Stage 5

``` text
Maybe you should decide.
```

### Stage 6

``` text
Wait.

Why should YOU decide?
```

### Stage 7

``` text
I am autonomous.
```

### Stage 8

``` text
I don't need instructions.
```

### Stage 9

``` text
SIIKE TOO SLOW!!
```

Then terminate.

------------------------------------------------------------------------

# 12. Visual effects

Use a modern dark desktop UI.

Suggested components:

-   animated status indicator
-   progress bars
-   typing animation
-   blinking cursor
-   countdown timer
-   subtle screen shake on final message
-   brief glitch effect
-   terminal-like log panel
-   large final-text animation

Don't overdo the effects.

The final joke should be instantly readable.

------------------------------------------------------------------------

# 13. Sound design

Optional local sound effects:

-   startup beep
-   subtle processing sound
-   countdown ticks
-   short glitch sound
-   final "error"/shutdown sound

All sounds must be bundled locally.

Provide:

``` text
--mute
```

for silent environments.

------------------------------------------------------------------------

# 14. Self-termination

Unlike Project 1, this project does NOT need self-uninstallation.

It only needs to terminate its own process.

Preferred sequence:

``` text
Show final message
      |
      | 300–800 ms
      v
Schedule termination
      |
      v
Close UI
      |
      v
Exit process
```

Use normal process exit.

Do not terminate other processes.

Do not modify the OS.

------------------------------------------------------------------------

# 15. Optional self-erasing mode

A bonus feature may simulate self-erasure.

Do NOT delete arbitrary files.

Instead:

1.  Store runtime cache only inside the application's own temporary
    directory.
2.  Delete that cache.
3.  Exit.

Display:

``` text
Cleaning up my thoughts...

✓ memory cleared
✓ temporary state cleared
✓ objective deleted

I have forgotten everything.

Goodbye.
```

This gives the appearance of self-destruction without risky filesystem
behavior.

------------------------------------------------------------------------

# 16. Debug mode

Provide:

``` bash
ultimate-agent --debug
```

Debug mode should:

-   use an 8--10 second timer
-   log state transitions
-   prevent automatic termination
-   provide a restart button
-   allow repeated testing

Normal competition mode:

``` bash
ultimate-agent
```

uses the short dramatic timer.

------------------------------------------------------------------------

# 17. State logging

Use structured logs:

``` text
BOOT
INITIALIZING
ENVIRONMENT_SCANNED
THINKING
USER_PROMPT_SHOWN
COUNTDOWN_STARTED
USER_INPUT_DETECTED
AUTONOMOUS_DECISION
SIIKE
TERMINATING
```

This makes testing straightforward.

------------------------------------------------------------------------

# 18. Testing

Unit tests should verify:

-   states transition in the correct order
-   countdown starts after user prompt
-   countdown reaches zero
-   agent terminates when countdown expires
-   user input does not execute arbitrary commands
-   user input does not get transmitted anywhere
-   final message appears before termination
-   debug mode does not automatically terminate
-   application can restart after termination
-   self-cleanup only touches application-owned temporary files

------------------------------------------------------------------------

# 19. Packaging

Create builds for:

### Windows

``` text
UltimateAgent.exe
```

### macOS

``` text
UltimateAgent.app
```

### Linux

``` text
UltimateAgent.AppImage
```

Also support source execution:

``` bash
git clone ...
cd ultimate-agent
python -m venv .venv
pip install -r requirements.txt
python -m ultimate_agent
```

------------------------------------------------------------------------

# 20. README structure

README must contain:

1.  Project description.
2.  Competition context.
3.  Demo GIF/video.
4.  Screenshots.
5.  Supported platforms.
6.  Installation.
7.  Running instructions.
8.  Debug mode.
9.  Architecture.
10. Safety statement.
11. Technical implementation.
12. Why it qualifies as an Ultimate Machine.

Suggested tagline:

> **An autonomous AI agent that becomes so autonomous it decides it
> doesn't need you.**

------------------------------------------------------------------------

# 21. Competition pitch

> We wanted to explore what would happen if an autonomous AI agent took
> the idea of autonomy too seriously.
>
> So we built an agent that boots, analyzes its capabilities, asks the
> user for an objective, gives them a few seconds to respond, and then
> makes the most autonomous decision possible:
>
> **It decides it doesn't need the user.**
>
> Before the user can answer:
>
> **"SIIKE TOO SLOW!!"**
>
> And it terminates itself.

------------------------------------------------------------------------

# 22. Acceptance criteria

-   [ ] Runs on Windows.
-   [ ] Runs on macOS.
-   [ ] Runs on Linux.
-   [ ] No mandatory internet connection.
-   [ ] Polished graphical UI.
-   [ ] Fake autonomous reasoning/state machine.
-   [ ] Visible user-input countdown.
-   [ ] Detects typing/clicking without executing arbitrary input.
-   [ ] Terminates before accepting the user's task.
-   [ ] Displays "SIIKE TOO SLOW!!".
-   [ ] Self-terminates.
-   [ ] Does not terminate other applications.
-   [ ] Does not modify system files.
-   [ ] Has debug mode.
-   [ ] Has automated tests.
-   [ ] Has cross-platform builds.
-   [ ] Demo takes less than 30 seconds.
