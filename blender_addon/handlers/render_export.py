"""Executes 'render_still' and 'export_scene' commands."""

import bpy


def handle_render_still(params: dict) -> dict:
    bpy.context.scene.render.filepath = params["output_path"]
    bpy.ops.render.render(write_still=True)
    return {"output_path": params["output_path"]}


_EXPORTERS = {
    "glb": lambda path: bpy.ops.export_scene.gltf(filepath=path, export_format="GLB"),
    "fbx": lambda path: bpy.ops.export_scene.fbx(filepath=path),
    "obj": lambda path: bpy.ops.wm.obj_export(filepath=path),
}


def handle_export_scene(params: dict) -> dict:
    exporter = _EXPORTERS.get(params["format"])
    if exporter is None:
        raise ValueError(f"Unknown export format '{params['format']}'")
    exporter(params["path"])
    return {"path": params["path"], "format": params["format"]}
