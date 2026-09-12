# Architecture

Two processes talk over a local TCP socket:

```
Claude/Codex --MCP(stdio)--> engine_mcp server --TCP/JSON--> Blender addon
```

## Layers (`src/engine_mcp/`)
- `core/` - `SceneEngine` interface + shared errors/transport. Engine-agnostic.
- `blender/` - implements `SceneEngine` for Blender.
  - `commands/` - pure functions that build a JSON command dict. No I/O.
  - `connection.py` - the actual socket.
  - `adapter.py` - glues commands + connection into `SceneEngine` methods.
- `unreal/` - stub `SceneEngine` implementation, not wired up yet.
- `tools/` - one file per MCP tool group. Each just calls the engine and
  catches errors. No business logic lives here.
- `server.py` - thin entrypoint. Creates the engine, registers tools, runs.

## Blender addon (`blender_addon/`)
Runs inside Blender's own Python. Mirrors the same command names.
- `socket_server.py` - accepts connections, one JSON command per connection.
- `queue_bridge.py` - hands commands to Blender's main thread (required -
  bpy is not thread-safe).
- `dispatcher.py` - looks up the right handler by command type.
- `handlers/` - one file per command group, the only files that call `bpy`.

## Why split this way
Adding a tool = one command builder + one handler + one MCP tool function,
each in its own small file. Nothing else changes. Adding an engine = one
new adapter implementing `SceneEngine`; `tools/` never changes.
