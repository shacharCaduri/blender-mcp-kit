"""Executes 'set_camera' and 'add_light' commands."""

import bpy
import mathutils


def handle_set_camera(params: dict) -> dict:
    cam = bpy.context.scene.camera
    if cam is None:
        bpy.ops.object.camera_add(location=tuple(params["location"]))
        cam = bpy.context.active_object
        bpy.context.scene.camera = cam
    else:
        cam.location = tuple(params["location"])
    direction = mathutils.Vector(params["look_at"]) - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return {"camera": cam.name}


def handle_add_light(params: dict) -> dict:
    bpy.ops.object.light_add(type=params["kind"].upper(), location=tuple(params["location"]))
    light = bpy.context.active_object
    light.data.energy = params["energy"]
    return {"light": light.name}
