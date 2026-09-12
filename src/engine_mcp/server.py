"""MCP server entrypoint. Keep this file thin - logic lives elsewhere.

Run directly (`python -m engine_mcp.server`) or via the
`blender-mcp-kit` console script installed by pyproject.toml.
"""

from mcp.server.fastmcp import FastMCP

from .blender.adapter import BlenderEngineAdapter
from .tools.register import register_all

mcp = FastMCP("blender-mcp-kit")
_engine = BlenderEngineAdapter()
register_all(mcp, _engine)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
