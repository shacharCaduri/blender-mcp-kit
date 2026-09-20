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
        # The addon's socket server is one-connection-per-command: it closes
        # the connection right after writing its reply (see
        # blender_addon/socket_server.py). A persistent client socket would
        # be reading from a connection the peer already closed on every call
        # after the first, which yields an empty recv() (EOF) and a
        # `json.loads("")` crash. So reconnect fresh for every request.
        self.connect()
        assert self._sock is not None
        try:
            self._sock.sendall(json.dumps(payload).encode("utf-8"))
            raw = self._read_full_response()
        finally:
            self.close()
        if not raw:
            raise EngineConnectionError(
                f"{self._host}:{self._port} closed the connection without a reply"
            )
        return json.loads(raw.decode("utf-8"))

    def _read_full_response(self) -> bytes:
        """Read until the peer closes the connection (end of one reply)."""
        assert self._sock is not None
        chunks: list[bytes] = []
        while True:
            chunk = self._sock.recv(RECV_BUFFER_BYTES)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)

    def close(self) -> None:
        if self._sock is not None:
            self._sock.close()
            self._sock = None
