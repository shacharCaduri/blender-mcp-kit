"""Maps a command's 'type' string to the handler function that runs it.

Every handler runs on Blender's main thread (see queue_bridge.py) and
must return a plain dict - never raise past this point.
"""

from .handlers import camera_light, materials, primitives, render_export, scene_query

_HANDLERS = {
    "add_primitive": primitives.handle_add_primitive,
    "set_material": materials.handle_set_material,
    "set_camera": camera_light.handle_set_camera,
    "add_light": camera_light.handle_add_light,
    "render_still": render_export.handle_render_still,
    "export_scene": render_export.handle_export_scene,
    "get_scene_info": scene_query.handle_get_scene_info,
}


def dispatch(command: dict) -> dict:
    handler = _HANDLERS.get(command.get("type"))
    if handler is None:
        return {"ok": False, "error": f"Unknown command type '{command.get('type')}'"}
    try:
        return {"ok": True, "result": handler(command.get("params", {}))}
    except Exception as exc:  # noqa: BLE001 - must never crash Blender's main loop
        return {"ok": False, "error": str(exc)}
