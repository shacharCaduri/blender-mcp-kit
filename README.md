# blender-mcp-kit

A small, modular MCP server that lets an LLM (Claude, Codex, ...) build
3D scenes in Blender through a fixed set of safe tools - no raw code
execution allowed by default.

Built for it to grow into: more Blender tools -> animation -> a second
adapter for Unreal Engine, all behind one `SceneEngine` interface.

## Read next
- [Architecture](docs/ARCHITECTURE.md) - how the pieces fit together
- [Setup](docs/SETUP.md) - install the addon, wire up Claude/Codex
- [Safety](docs/SAFETY.md) - why it's built this way
- [Roadmap](docs/ROADMAP.md) - what's next (animation, Unreal, ...)
