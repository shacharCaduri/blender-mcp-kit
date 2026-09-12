"""Thin Blender-specific wrapper around the generic SocketTransport."""

from ..config import DEFAULT_HOST, DEFAULT_PORT
from ..core.transport import SocketTransport


class BlenderConnection(SocketTransport):
    """One TCP connection to the running Blender addon's command server."""

    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
        super().__init__(host, port)
