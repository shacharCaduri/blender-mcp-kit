"""MCP tool for assigning a color/material to an object."""

from ..core.errors import EngineCommandError, EngineConnectionError


def register(mcp, engine):
    @mcp.tool()
    def set_material(object_name: str, r: float, g: float, b: float,
                      metallic: float = 0.0, roughness: float = 0.5) -> dict:
        """Set an object's base color (0-1 RGB) and metallic/roughness."""
        try:
            return engine.set_material(object_name, (r, g, b, 1.0), metallic, roughness)
        except (EngineConnectionError, EngineCommandError) as exc:
            return {"ok": False, "error": str(exc)}
