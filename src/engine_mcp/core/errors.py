"""Custom exceptions for engine communication and commands.

See docs/ARCHITECTURE.md for where these are raised and caught.
"""


class EngineConnectionError(RuntimeError):
    """Could not reach the target engine (Blender, Unreal, ...)."""


class EngineCommandError(RuntimeError):
    """The engine reached, but rejected or failed a command."""

    def __init__(self, command: str, detail: str):
        super().__init__(f"'{command}' failed: {detail}")
        self.command = command
        self.detail = detail
