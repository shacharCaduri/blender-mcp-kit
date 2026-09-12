"""Executes 'add_primitive' commands using bpy. Runs on the main thread."""

import bpy

_ADD_OPS = {
    "cube": bpy.ops.mesh.primitive_cube_add,
    "sphere": bpy.ops.mesh.primitive_uv_sphere_add,
    "cylinder": bpy.ops.mesh.primitive_cylinder_add,
    "cone": bpy.ops.mesh.primitive_cone_add,
    "plane": bpy.ops.mesh.primitive_plane_add,
}


def handle_add_primitive(params: dict) -> dict:
    kind = params["kind"]
    add_op = _ADD_OPS.get(kind)
    if add_op is None:
        raise ValueError(f"Unknown primitive '{kind}'")
    add_op(location=tuple(params["location"]))
    obj = bpy.context.active_object
    obj.scale = tuple(params["scale"])
    if params.get("name"):
        obj.name = params["name"]
    return {"name": obj.name}
