"""Local-only TCP server: one connection = one JSON command = one reply.

Deliberately simple (no auth, no concurrency) - see docs/SAFETY.md for
why this must stay bound to localhost only.
"""

from __future__ import annotations

import json
import socket
import threading

from .queue_bridge import start_timer, stop_timer, submit

_HOST, _PORT = "localhost", 9876
_server_socket: socket.socket | None = None
_accept_thread: threading.Thread | None = None
_running = False


def _handle_client(conn: socket.socket):
    with conn:
        raw = conn.recv(65536)
        if not raw:
            return
        try:
            command = json.loads(raw.decode("utf-8"))
            response = submit(command)
        except Exception as exc:  # noqa: BLE001
            response = {"ok": False, "error": str(exc)}
        conn.sendall(json.dumps(response).encode("utf-8"))


def _accept_loop():
    while _running:
        try:
            conn, _ = _server_socket.accept()
        except OSError:
            break
        threading.Thread(target=_handle_client, args=(conn,), daemon=True).start()


def start_server():
    global _server_socket, _accept_thread, _running
    start_timer()
    _server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _server_socket.bind((_HOST, _PORT))
    _server_socket.listen(5)
    _running = True
    _accept_thread = threading.Thread(target=_accept_loop, daemon=True)
    _accept_thread.start()


def stop_server():
    global _running
    _running = False
    stop_timer()
    if _server_socket:
        _server_socket.close()
