# Setup

## 1. Install the addon in Blender
The repo ships a ready-to-install `blender_addon.zip` at the repo root
(built from `blender_addon/` — rebuild it with
`zip -r blender_addon.zip blender_addon -x "*__pycache__*" -x "*.pyc"`
if you change the addon source).

In Blender: **Edit > Preferences > Add-ons > Install from Disk...**,
pick `blender_addon.zip`, then enable "AI Scene Bridge" in the add-on
list. It starts listening on `localhost:9876` automatically as soon as
it's enabled — no need to restart Blender.

## 2. Install the server
```bash
cd blender-mcp
uv sync
```

## 3. Sanity-check the connection (recommended before wiring up an LLM)
With Blender open and the addon enabled, run:
```bash
uv run python scripts/manual_test.py
```
This talks to the addon directly (no MCP client needed) — it adds a
cube, paints it red, and reads the scene back. If it prints a red
`TestCube` in the returned object list with no traceback, the addon
and the server-side client are wired up correctly.

> **Note:** older checkouts (before the `SocketTransport` fix) could
> fail on the second command in this script with
> `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`.
> That was a client bug (reusing a connection the addon had already
> closed) — it's fixed as of this repo's current `master`. If you see
> that error, `git pull` and retry before troubleshooting anything
> else.

## 4. Point Claude or Codex at it

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

## 5. Try it
With Blender open and the addon enabled, ask your assistant to
"add a red cube at the origin and render it".
