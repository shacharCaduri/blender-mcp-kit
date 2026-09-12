"""Blender addon: exposes a local command socket for engine_mcp to drive.

Install by zipping this folder and adding via
Blender > Edit > Preferences > Add-ons > Install.
See docs/SAFETY.md for the safe-tools-only design rationale.
"""

bl_info = {
    "name": "AI Scene Bridge",
    "author": "you",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > AI Bridge",
    "description": "Local socket bridge so an MCP server can build scenes",
    "category": "Interface",
}

from .socket_server import start_server, stop_server


def register():
    start_server()


def unregister():
    stop_server()
