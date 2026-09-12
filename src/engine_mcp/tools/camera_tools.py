"""MCP tools for camera placement and lighting."""

from ..core.errors import EngineCommandError, EngineConnectionError


def register(mcp, engine):
    @mcp.tool()
    def set_camera(x: float, y: float, z: float,
                    look_x: float = 0, look_y: float = 0, look_z: float = 0) -> dict:
        """Move the camera and point it at a target location."""
        try:
            return engine.set_camera((x, y, z), (look_x, look_y, look_z))
        except (EngineConnectionError, EngineCommandError) as exc:
            return {"ok": False, "error": str(exc)}

    @mcp.tool()
    def add_light(kind: str, x: float, y: float, z: float, energy: float = 1000.0) -> dict:
        """Add a light (point/sun/spot/area) to the scene."""
        try:
            return engine.add_light(kind, (x, y, z), energy)
        except (EngineConnectionError, EngineCommandError, ValueError) as exc:
            return {"ok": False, "error": str(exc)}
