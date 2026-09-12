"""Bridges the socket thread to Blender's main thread.

bpy must only be touched on the main thread. The socket thread drops
commands here and blocks until this module's timer (running on the
main thread) has executed them.
"""

import queue
import threading

import bpy

from .dispatcher import dispatch

_QUEUE: "queue.Queue[tuple[dict, threading.Event, dict]]" = queue.Queue()
_POLL_INTERVAL = 0.05


def submit(command: dict) -> dict:
    """Called from the socket thread. Blocks until dispatched on main thread."""
    done = threading.Event()
    box: dict = {}
    _QUEUE.put((command, done, box))
    done.wait()
    return box["response"]


def _drain_queue():
    while not _QUEUE.empty():
        command, done, box = _QUEUE.get_nowait()
        box["response"] = dispatch(command)
        done.set()
    return _POLL_INTERVAL


def start_timer():
    bpy.app.timers.register(_drain_queue, persistent=True)


def stop_timer():
    if bpy.app.timers.is_registered(_drain_queue):
        bpy.app.timers.unregister(_drain_queue)
