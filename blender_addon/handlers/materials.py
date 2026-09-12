"""Executes 'set_material' commands: a plain principled-BSDF color."""

import bpy


def handle_set_material(params: dict) -> dict:
    obj = bpy.data.objects.get(params["object_name"])
    if obj is None:
        raise ValueError(f"No object named '{params['object_name']}'")
    mat = bpy.data.materials.new(name=f"{obj.name}_mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = tuple(params["color"])
    bsdf.inputs["Metallic"].default_value = params["metallic"]
    bsdf.inputs["Roughness"].default_value = params["roughness"]
    obj.data.materials.append(mat)
    return {"material": mat.name}
