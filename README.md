# blender-mcp-kit

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![Blender](https://img.shields.io/badge/Blender-4.x-F5792A?logo=blender&logoColor=white)](https://www.blender.org/)
[![MCP](https://img.shields.io/badge/MCP-server-6E56CF)](https://modelcontextprotocol.io)
[![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)](tests/)

A small, modular **MCP server** that lets an LLM (Claude, Codex, ...)
build 3D scenes in Blender through a fixed set of safe, typed tools —
**no raw code execution** allowed by default.

```
Claude / Codex  --MCP (stdio)-->  engine_mcp server  --TCP/JSON-->  Blender addon
```

Built to grow into: more Blender tools → animation → a second adapter
for Unreal Engine, all behind one `SceneEngine` interface. See the
[Roadmap](docs/ROADMAP.md).

## Why this instead of raw code execution

Most Blender-MCP integrations give the LLM a `run_python` tool. This
one doesn't. Every action is a named, typed command
(`add_primitive`, `set_material`, `render_still`, ...) implemented by
a small, auditable handler. Smaller attack surface, easier review, no
surprise `bpy` calls. See [Safety](docs/SAFETY.md) for the reasoning.

## Quickstart

```bash
# 1. Install the addon in Blender: Edit > Preferences > Add-ons >
#    Install from Disk... -> select blender_addon.zip -> enable
#    "AI Scene Bridge". It listens on localhost:9876 automatically.

# 2. Install the server
cd blender-mcp
uv sync

# 3. Sanity-check the connection (no LLM client needed)
uv run python scripts/manual_test.py

# 4. Wire it up to Claude / Codex - see docs/SETUP.md
```

Full walkthrough, including client config for Claude Desktop, Claude
Code, and Codex: [Setup](docs/SETUP.md).

## Read next
- [Setup](docs/SETUP.md) — install the addon, wire up Claude/Codex
- [Architecture](docs/ARCHITECTURE.md) — how the pieces fit together
- [Safety](docs/SAFETY.md) — why it's built this way
- [Roadmap](docs/ROADMAP.md) — what's next (animation, Unreal, ...)

## Status

Phase 1 (static scenes: primitives, materials, camera, lights,
render/export) is done and tested end-to-end against a live Blender
instance. Animation, an asset pipeline, and an Unreal adapter are
planned — see the [Roadmap](docs/ROADMAP.md).
