# Safety design

Compared to community Blender-MCP projects, two choices on purpose:

1. **No raw code execution tool.** Every action is a named, typed command
   (`add_primitive`, `set_material`, ...). The LLM cannot ask Blender to
   run arbitrary Python. Smaller surface, easy to audit `handlers/`.
2. **Localhost only, single command per connection.** The socket server
   never binds beyond `127.0.0.1` and doesn't keep a session open. Keep
   it that way - don't add auth-less remote access.

If you later want a "run custom code" escape hatch, make it its own
opt-in tool, behind a config flag, reviewed like the rest - not the default.
