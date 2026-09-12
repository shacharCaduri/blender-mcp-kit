"""Pure command-builders for producing output files."""

VALID_EXPORT_FORMATS = {"fbx", "glb", "obj"}


def build_render_still(output_path: str) -> dict:
    return {"type": "render_still", "params": {"output_path": output_path}}


def build_export_scene(path: str, file_format: str) -> dict:
    if file_format not in VALID_EXPORT_FORMATS:
        raise ValueError(f"Unknown format '{file_format}'. Use one of {sorted(VALID_EXPORT_FORMATS)}")
    return {"type": "export_scene", "params": {"path": path, "format": file_format}}
