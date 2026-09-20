"""Regression test: SocketTransport must work against a one-shot-per-
connection server, matching blender_addon/socket_server.py's real behavior
(it closes the connection after every reply).
"""

import json
import socket
import threading

from engine_mcp.core.transport import SocketTransport


def _serve_one_shot_per_connection(server_sock: socket.socket, replies: list[dict]):
    for reply in replies:
        conn, _ = server_sock.accept()
        with conn:
            conn.recv(65536)
            conn.sendall(json.dumps(reply).encode("utf-8"))


def test_send_json_survives_server_closing_connection_after_each_reply():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", 0))
    server_sock.listen(5)
    host, port = server_sock.getsockname()

    replies = [{"ok": True, "result": {"name": "TestCube"}}, {"ok": True, "result": {"material": "TestCube_mat"}}]
    thread = threading.Thread(target=_serve_one_shot_per_connection, args=(server_sock, replies), daemon=True)
    thread.start()

    transport = SocketTransport(host, port)
    first = transport.send_json({"type": "add_primitive", "params": {}})
    second = transport.send_json({"type": "set_material", "params": {}})

    thread.join(timeout=2)
    server_sock.close()

    assert first == replies[0]
    assert second == replies[1]
