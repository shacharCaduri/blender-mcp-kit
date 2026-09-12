# Setup

## 1. Install the addon in Blender
Zip `blender_addon/` and install via Blender > Edit > Preferences >
Add-ons > Install, then enable "AI Scene Bridge". It starts listening
on `localhost:9876` automatically.

## 2. Install the server
```bash
cd blender-mcp
uv sync
```

## 3. Point Claude or Codex at it

Claude Desktop (`claude_desktop_config.json`):
```json
{ "mcpServers": { "blender-mcp-kit": {
  "command": "uv", "args": ["--directory", "/absolute/path/to/blender-mcp", "run", "blender-mcp-kit"]
} } }
```

Claude Code:
```bash
claude mcp add blender-mcp-kit -- uv --directory /absolute/path/to/blender-mcp run blender-mcp-kit
```

Codex (`~/.codex/config.toml`):
```toml
[mcp_servers.blender-mcp-kit]
command = "uv"
args = ["--directory", "/absolute/path/to/blender-mcp", "run", "blender-mcp-kit"]
```

## 4. Try it
With Blender open and the addon enabled, ask your assistant to
"add a red cube at the origin and render it".
