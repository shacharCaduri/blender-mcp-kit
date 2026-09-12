"""MCP tools for creating and inspecting scene objects."""

from ..core.errors import EngineCommandError, EngineConnectionError


def register(mcp, engine):
    @mcp.tool()
    def add_primitive(kind: str, x: float = 0, y: float = 0, z: float = 0,
                       scale: float = 1.0, name: str | None = None) -> dict:
        """Add a primitive shape (cube/sphere/cylinder/cone/plane) to the scene."""
        try:
            return engine.add_primitive(kind, (x, y, z), (scale, scale, scale), name)
        except (EngineConnectionError, EngineCommandError, ValueError) as exc:
            return {"ok": False, "error": str(exc)}

    @mcp.tool()
    def get_scene_info() -> dict:
        """List objects currently in the Blender scene."""
        try:
            return engine.get_scene_info()
        except (EngineConnectionError, EngineCommandError) as exc:
            return {"ok": False, "error": str(exc)}
