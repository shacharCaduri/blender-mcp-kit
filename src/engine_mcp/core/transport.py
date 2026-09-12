"""Generic JSON-over-TCP-socket transport, reusable by any engine adapter.

Engine-specific code (Blender, Unreal) should not open sockets itself -
it should use this class. See docs/ARCHITECTURE.md.
"""

import json
import socket

from ..config import RECV_BUFFER_BYTES, SOCKET_TIMEOUT_SECONDS
from .errors import EngineConnectionError


class SocketTransport:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._sock: socket.socket | None = None

    def connect(self) -> None:
        try:
            self._sock = socket.create_connection(
                (self._host, self._port), timeout=SOCKET_TIMEOUT_SECONDS
            )
        except OSError as exc:
            raise EngineConnectionError(
                f"Cannot reach {self._host}:{self._port} - is the addon running? ({exc})"
            ) from exc

    def send_json(self, payload: dict) -> dict:
        if self._sock is None:
            self.connect()
        assert self._sock is not None
        self._sock.sendall(json.dumps(payload).encode("utf-8"))
        raw = self._sock.recv(RECV_BUFFER_BYTES)
        return json.loads(raw.decode("utf-8"))

    def close(self) -> None:
        if self._sock is not None:
            self._sock.close()
            self._sock = None
