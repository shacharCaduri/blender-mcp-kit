"""Single place that wires every tool module into the MCP server.

Add a new tool module? Import it and add one line here - nothing else
in this file should ever need to change.
"""

from . import camera_tools, material_tools, render_tools, scene_tools


def register_all(mcp, engine) -> None:
    scene_tools.register(mcp, engine)
    material_tools.register(mcp, engine)
    camera_tools.register(mcp, engine)
    render_tools.register(mcp, engine)
