"""Pure command-builder for reading current scene state."""


def build_get_scene_info() -> dict:
    return {"type": "get_scene_info", "params": {}}
