"""Executes 'get_scene_info' commands - a read-only scene snapshot."""

import bpy


def handle_get_scene_info(params: dict) -> dict:
    objects = [
        {"name": obj.name, "type": obj.type, "location": list(obj.location)}
        for obj in bpy.context.scene.objects
    ]
    return {"objects": objects, "count": len(objects)}
