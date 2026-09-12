"""MCP tools for producing output files (renders, exports)."""

from ..core.errors import EngineCommandError, EngineConnectionError


def register(mcp, engine):
    @mcp.tool()
    def render_still(output_path: str) -> dict:
        """Render the current scene to a still image file."""
        try:
            return engine.render_still(output_path)
        except (EngineConnectionError, EngineCommandError) as exc:
            return {"ok": False, "error": str(exc)}

    @mcp.tool()
    def export_scene(path: str, file_format: str = "glb") -> dict:
        """Export the scene to a game-ready file (glb/fbx/obj)."""
        try:
            return engine.export_scene(path, file_format)
        except (EngineConnectionError, EngineCommandError, ValueError) as exc:
            return {"ok": False, "error": str(exc)}
